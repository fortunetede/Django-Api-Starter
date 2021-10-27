from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from rest_framework.authtoken.models import Token
from datetime import datetime
from django.utils import timezone
# Create your models here.

class APPUserManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, password=None):
        """
        Creates and saves a User with the given email,
        first_name, last_name and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, first_name, last_name):
        """
        Creates and saves a superuser with the given email, password,
        first_name and last_name.
        """
        user = self.create_user(email,
                                password=password,
                                first_name=first_name,
                                last_name=last_name)
        user.is_admin = True
        user.save(using=self._db)
        return user


class APPUser(AbstractBaseUser):

    USER_TYPES = (
        ('APP USER', 'APP USER'),
        ('ADMIN', 'ADMIN'),
    )
    email = models.EmailField(verbose_name=_('email address'), unique=True, max_length=255 )
    username = models.CharField(verbose_name=_('username'), blank=True, null=True, max_length=100 )
    first_name = models.CharField(default=' ', max_length=100)
    last_name = models.CharField(default=' ', max_length=100)
    phone_number = models.CharField(blank=True, null=True, max_length=100)
    user_type = models.CharField(blank=True, null=True, max_length=500, choices=USER_TYPES)
    last_login = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now)
    is_admin = models.BooleanField(default=False)
    objects = APPUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return '''{} {}'''.format(self.first_name, self.last_name)

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def __str__(self):
        return '%s %s' % (self.email, self.id)

    class Meta:
        ordering = ('-id',)
        verbose_name = _('user')
        verbose_name_plural = _('users')


@receiver(post_save, sender=APPUser)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

