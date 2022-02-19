from django.contrib import admin
from .models import CustomUser, Transaction

admin.site.register(CustomUser)
admin.site.register(Transaction)
