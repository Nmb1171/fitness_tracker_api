from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Update or create a user and set the password'

    def handle(self, *args, **kwargs):
        username = 'nahom_fitness'
        email = 'nahom@example.com'
        new_password = 'CLASHROYALE123*'

        try:
            user, created = User.objects.get_or_create(username=username, email=email)
            user.set_password(new_password)
            user.is_active = True
            user.save()

            if created:
                self.stdout.write(self.style.SUCCESS(f"User {username} created successfully!"))
            else:
                self.stdout.write(self.style.SUCCESS(f"Password for {username} updated successfully!"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error: {str(e)}"))
