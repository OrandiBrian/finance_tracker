import random
from faker import Faker
from django.core.management.base import BaseCommand
from tracker.models import User, Transaction, Category


class Command(BaseCommand):
    help = "Generate random transactions for testing purposes"

    def handle(self, *args, **options):
        fake = Faker()

        # createing categories for application
        categories = [
            "Bills",
            "Food",
            "Clothes",
            "Medical",
            "Housing",
            "Salary",
            "Social",
            "Transport",
            "Vacation",
        ]
