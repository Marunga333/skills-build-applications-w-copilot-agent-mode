from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Crea un índice único en el campo email de la colección de usuarios.'

    def handle(self, *args, **options):
        db = connection.cursor().db_conn
        result = db['octofit_tracker_user'].create_index('email', unique=True)
        self.stdout.write(self.style.SUCCESS(f'Índice único creado en email: {result}'))
