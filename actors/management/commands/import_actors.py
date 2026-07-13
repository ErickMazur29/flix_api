import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from actors.models import Actors


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help='Nome do arquivo CSV com os atores'
        )

    def handle(self, *args, **options):
        file_name = options['file_name']

        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name']
                birthday = datetime.strptime(row['birthday'], '%Y-%m-%d').date()  # conversor de str para date
                nationality = row['nationality']
                age = row['age']

                self.stdout.write(self.style.NOTICE(name))

                Actors.objects.create(
                    name=name,
                    birthday=birthday,
                    nationality=nationality,
                    age=age
                )

        self.stdout.write(self.style.SUCCESS('ATORES IMPORTADOS COM SUCESSO!!!'))
