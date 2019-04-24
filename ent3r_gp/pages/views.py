from datetime import datetime

from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.db.models import Sum
from django.shortcuts import redirect, render

from .forms import NewActivityForm
from .models import Activity, Achievement, MentorPair


HIGHSCORE_LIMIT = 5


MONTHS = {
    1: 'januar',
    2: 'februar',
    3: 'mars',
    4: 'april',
    5: 'mai',
    6: 'juni',
    7: 'juli',
    8: 'august',
    9: 'september',
    10: 'oktober',
    11: 'november',
    12: 'desember'
    }


def index(request):
    if request.user.is_authenticated:
        return redirect('pages_hiscore')
    else:
        return redirect('login')


#######################
# Periods:
# 1: 16. jan - 15. feb
# 2: 16. feb - 15. mars
# etc...
# .
# .
# 12: 16. des - 15. jan
########################
def get_start_and_end_date(year=None, period=None):
    if year is None:
        year = datetime.now().year
    if period is None:
        period = datetime.now().month
        if datetime.now().day <= 15:
            period -= 1
    year = int(year)
    period = int(period)
    start = datetime(year, period, 16)
    if period == 12:
        end = datetime(year+1, 1, 15, 23, 59, 59)
    else:
        end = datetime(year, period+1, 15, 23, 59, 59)
    return start, end


def get_pair_list(user, is_total=False, year=None, period=None):
    pair_list = Achievement.objects \
        .values('user__mentorpair1__name') \
        .annotate(score=Sum('activity__points'))
    if not is_total:
        start, end = get_start_and_end_date(year, period)
        pair_list = pair_list.filter(date_added__gte=start, date_added__lte=end)

    if user.is_superuser:
        pair_list = pair_list.order_by('-score')
        # The highscore template needs a 'group' property for each pair.
        for p in pair_list:
            pair = MentorPair.objects.filter(name=p['user__mentorpair1__name']).first()
            if pair:
                p['group'] = User.objects.get(id=pair.mentor_1_id).groups.first().name
    else:
        group = user.groups.first().name  # Get location, eg. Trondheim
        pair_list = pair_list \
            .filter(user__groups__name=group) \
            .order_by('-score')[:HIGHSCORE_LIMIT]

    # Get mentor info for each pair
    for p in pair_list:
        pair = MentorPair.objects.filter(name=p['user__mentorpair1__name']).first()
        if pair:
            p['user1'] = User.objects.values().get(id=pair.mentor_1_id)
            p['user2'] = User.objects.values().get(id=pair.mentor_2_id)
    return pair_list


@login_required
def hiscore(request, year=None, period=None):
    group = 'alle lokasjoner' if request.user.is_superuser else request.user.groups.first().name
    start, end = get_start_and_end_date(year, period)
    my_score = Achievement.objects.filter(user_id=request.user.id).aggregate(score=Sum('activity__points'))
    pair_list = get_pair_list(request.user, is_total=False, year=year, period=period)
    return render(request, 'pages/highscore.html', {
            'ps': pair_list,
            'ms': my_score,
            'start': start,
            'end': end,
            'group': group,
            'monthly': True,
            'month': MONTHS[end.month],
        })


@login_required
def hiscore_total(request):
    group = 'alle lokasjoner' if request.user.is_superuser else request.user.groups.first().name
    my_score = Achievement.objects.filter(user_id=request.user.id).aggregate(score=Sum('activity__points'))
    pair_list = get_pair_list(request.user, is_total=True)
    return render(request, 'pages/highscore.html', {
            'ps': pair_list,
            'ms': my_score,
            'group': group,
            'monthly': False,
        })


@login_required
def activities(request):
    act = Activity.objects.all()
    if request.method == "POST":
        checked = request.POST.getlist('choices')
        for ach in checked:
            completed_activity = Activity.objects.get(id=ach)
            new_achievement = Achievement.objects.create(activity=completed_activity, user=request.user)
            new_achievement.save()
        return redirect('pages_hiscore')
    else:
        act = act.order_by('points')
        return render(request, 'pages/activities.html', {'act': act})


@user_passes_test(lambda u: u.is_superuser)
def activity_new(request):
    if request.method == "POST":
        form = NewActivityForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('pages_activities')
    else:
        form = NewActivityForm()
        return render(request, 'pages/activity_new.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def delete_activities(request):
    acts = Activity.objects.all()
    if request.method == "POST":
        checked = request.POST.getlist('delete')
        for act_id in checked:
            act_to_delete = Activity.objects.get(id=act_id)
            act_to_delete.delete()
        return redirect('pages_activities')
    else:
        acts = acts.order_by('points')
        return render(request, 'pages/del_activities.html', {'act': acts})


@login_required
def my_achievements(request):
    my_ach = Achievement.objects.filter(user_id=request.user.id)
    return render(request, 'pages/my_achievements.html', {'my_ach': my_ach})


@login_required
def delete_achievements(request):
    my_ach = Achievement.objects.filter(user_id=request.user.id)
    if request.method == "POST":
        checked = request.POST.getlist('delete')
        for ach_id in checked:
            ach_to_delete = Achievement.objects.get(id=ach_id)
            ach_to_delete.delete()
        return redirect('pages_hiscore')
    else:
        return render(request, 'pages/del_achievements.html', {'my_ach': my_ach})
