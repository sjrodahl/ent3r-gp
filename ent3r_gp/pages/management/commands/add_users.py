import csv

from django.contrib.auth.models import User, Group
from django.core.management.base import BaseCommand, CommandError

from account.models import Mentor
from pages.models import Location

class Command(BaseCommand):
    help = 'add new user from a csv-file with contact information for the mentors'

    def add_arguments(self, parser):
        parser.add_argument('file', nargs = '+', type=str)

    def handle(self, *args, **options):
        pword = "mentor"
        filename = options['file'][0]
        with open(filename, 'r') as f:
            user_reader = csv.reader(f, delimiter=',')
            next(user_reader)   #Skip the header
            for row in user_reader:
                name, mail,_, location = row
                name = name.split()
                first_name = name[0]
                last_name = name[-1]
                user = User.objects.create_user(username=mail.lower(),
                        email=mail.lower(),
                        password=pword,
                        first_name=first_name,
                        last_name=last_name)
                loc, created = Location.objects.get_or_create(name=location)
                mentor = Mentor(user, loc)
                mentor.save()







