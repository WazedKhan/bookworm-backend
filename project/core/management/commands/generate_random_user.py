import random
from tqdm import tqdm

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import IntegrityError

from faker import Faker

User = get_user_model()


class Command(BaseCommand):
    help = "Create thousands of users"

    def add_arguments(self, parser):
        parser.add_argument("count", type=int, help="Number of users to create")

    def handle(self, *args, **options):
        fake = Faker()
        count = options["count"]
        for _ in tqdm(range(count)):
            phone = "+8801"+ str(random.randint(111111111, 999999999))
            username = fake.user_name()
            email = fake.email()
            first_name = fake.first_name()
            last_name = fake.last_name()
            password = "password123"
            date_of_birth = fake.date()
            try:
                User.objects.create_user(
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    phone=phone,
                    date_of_birth=date_of_birth,
                    password=password,
                )
            except IntegrityError:
                self.stdout.write(self.style.WARNING(f"{username} Already Exists!"))