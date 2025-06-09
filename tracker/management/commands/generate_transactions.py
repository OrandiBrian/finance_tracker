import random
from decimal import Decimal
from faker import Faker
from django.core.management.base import BaseCommand
from tracker.models import User, Transaction, Category 

class Command(BaseCommand):
    help = "Generate random transactions for testing purposes"

    def handle(self, *args, **options):
        fake = Faker()

        # Create categories
        category_names = ['Bills', 'Food', 'Clothes', 'Medical', 'Housing', 'Salary', 'Social', 'Transport', 'Vacation']
        for name in category_names:
            Category.objects.get_or_create(name=name)

        # Get or create the user
        user = User.objects.filter(username="admin").first()
        if not user:
            user = User.objects.create_superuser(username='admin', email='admin@example.com', password='admin123')

        categories = Category.objects.all()
        types = [x[0] for x in Transaction.TRANSACTION_TYPE_CHOICES]

        # Create transactions
        for _ in range(20):
            Transaction.objects.create(
                category=random.choice(categories),
                user=user,
                amount=Decimal(str(round(random.uniform(1, 2500), 2))),
                date=fake.date_between(start_date='-1y', end_date='today'),
                type=random.choice(types)
            )