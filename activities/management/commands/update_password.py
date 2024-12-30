from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Update a user password'

    def handle(self, *args, **kwargs):
        username = 'nahom_fitness'
        new_password = 'CLASHROYALE123*'

        try:
            user = User.objects.get(username=username)
            user.set_password(new_password)
            user.save()
            self.stdout.write(self.style.SUCCESS(f"Password for {username} updated successfully!"))
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR(f"User {username} does not exist."))
