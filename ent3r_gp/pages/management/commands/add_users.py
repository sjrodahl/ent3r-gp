from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
import csv

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
                name, _, _, _, _, mail, _ = row
                name = name.split()
                first_name = name[0]
                last_name = name[-1]
                User.objects.create_user(username=mail.lower(),
                        email = mail.lower(),
                        password=pword,
                        first_name=first_name,
                        last_name = last_name)



