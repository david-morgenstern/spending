import uuid

from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=50, blank=True, null=True, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    @property
    def get_transactions(self):
        return Transaction.objects.filter(user=self).values()

    def __str__(self):
        return str(self.email)


class Transaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_spending')
    amount = models.IntegerField()
    currency = models.CharField(max_length=5)
    target = models.CharField(max_length=150)
    comment = models.CharField(max_length=255)
    type_of_payment = models.CharField(max_length=150)
    date = models.DateField()
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{uuid.uuid1().hex}')
        super(Transaction, self).save(*args, **kwargs)

    def get_self(self):
        return Transaction.objects.filter(slug=self.slug).values()

    def __str__(self):
        return f"tr: {self.id}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=[
                'user', 'amount', 'currency', 'target', 'comment', 'type_of_payment', 'date'
            ], name='no_duplicate_transaction_constraint')
        ]

