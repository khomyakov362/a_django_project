from django.core.management import BaseCommand
from users.models import User

class Command(BaseCommand):

    def handle(self, *args, **options):
        admin_user = User.objects.create(
            email='admin@web.top',
            first_name='Admin',
            last_name='Admin',
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )

        admin_user.set_password('qwerty')
        admin_user.save()
        print('Admin created')