from django.contrib import admin
from tracker.models import User, Category, Transaction

# Register your models here.
@admin.site.register(User)
@admin.site.register(Category)
@admin.site.register(Transaction)