from django.core.management.base import BaseCommand, CommandError
from pages.models import Activity
import csv

class Command(BaseCommand):
    help = 'add new activities form a specified csv-file'

    def add_arguments(self, parser):
        parser.add_argument('file', nargs = '+', type=str)

    def handle(self, *args, **options):
        filename = options['file'][0]
        with open(filename, 'r') as f:
            activity_reader = csv.reader(f, delimiter=',')
            next(activity_reader) # skip header
            for row in activity_reader:
                points, tag, _, description = row
                points = [int(s) for s in points.split() if s.isdigit()][0]
                tag = tag.strip('( )')
                description = description.strip()
                Activity.objects.create(name=description, tag=tag, points = points)


