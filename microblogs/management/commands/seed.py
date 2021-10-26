from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from microblogs.models import User

class Command(BaseCommand):
    def __init__(self):
        #super().__init__()
        self.faker = Faker('en_GB')
    def handle(self, *args, **options):
        #print("WARNING: The SEED command has not been implemeneted yet.")
        for i in range (100):
            addFirst_name = self.faker.first_name()
            addLast_name = self.faker.last_name()

            addUser = User.objects.create_user(
            "@" + addFirst_name + addLast_name,
            first_name = addFirst_name,
            last_name = addLast_name,
            email = addFirst_name + addLast_name +"@gmail.com",
            password = self.faker.password(),
            bio = self.faker.text()
            )
            addUser.save()
