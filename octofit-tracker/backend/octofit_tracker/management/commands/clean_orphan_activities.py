from django.core.management.base import BaseCommand
from octofit_tracker.models import Activity, User

class Command(BaseCommand):
    help = 'Elimina actividades huérfanas que referencian usuarios inexistentes.'

    def handle(self, *args, **options):
        count = 0
        for activity in Activity.objects.all():
            try:
                _ = activity.user
            except User.DoesNotExist:
                self.stdout.write(f'Orphan activity found and deleted: {activity.id}')
                activity.delete()
                count += 1
        self.stdout.write(self.style.SUCCESS(f'Eliminadas {count} actividades huérfanas.'))
