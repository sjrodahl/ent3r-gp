from django.contrib.auth.models import User, Group
from pages.models import MentorPair
from django.core.management.base import BaseCommand, CommandError
import csv

class Command(BaseCommand):
    help = 'Add mentor-pairs from a csv-file'

    def add_arguments(self, parser):
        parser.add_argument('file', nargs = '+', type=str)

    def handle(self, *args, **options):
        filename = options['file'][0]
        with open(filename, 'r') as f:
            user_reader = csv.reader(f, delimiter=',')
            next(user_reader)   #Skip the header
            for row in user_reader:
                groupname, mentor_1, mentor_2, room, campus, comment = row
                mentor_1_last_name = mentor_1.split()[-1]
                mentor_2_last_name = mentor_2.split()[-1]
                user_1 = User.objects.get(last_name=mentor_1_last_name)
                user_2 = User.objects.get(last_name=mentor_2_last_name)
                pair = MentorPair.objects.create(name=groupname, mentor_1=user_1, mentor_2=user_2)








