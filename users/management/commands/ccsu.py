from django.core.management import BaseCommand
from users.models import User

class Command(BaseCommand):

    def handle(self, *args, **options):
        admin_user = User.objects.create(
            email='admin@web.top',
            first_name='Admin',
            last_name='Admin',
            role='admin',
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )

        admin_user.set_password('qwerty')
        admin_user.save()
        print('Admin created')
    
        moderator = User.objects.create(
                email='mod@web.top',
                first_name='Moderator',
                last_name='Moderator',
                role='moderator',
                is_staff=True,
                is_superuser=False,
                is_active=True,
            )
        
        moderator.set_password('querty')
        moderator.save()
        print('Moderator created')
    
        user = User.objects.create(
                email='user@web.top',
                first_name='User',
                last_name='User',
                role='user',
                is_staff=False,
                is_superuser=False,
                is_active=True,
            )
        
        user.set_password('querty')
        user.save()
        print('User created')
    