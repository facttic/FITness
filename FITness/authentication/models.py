from django.db import models
from django.utils.translation import gettext_lazy as _
from FITness.cooperative.models import Cooperative
from django.contrib.auth.models import AbstractUser

class CooperativeUser(AbstractUser):
        email = models.EmailField(_('email address'), unique=True)
        cooperative = models.ForeignKey(Cooperative, on_delete=models.CASCADE, blank=True, null=True,
                                     verbose_name=_('cooperative'))
        other_contact = models.CharField(_('contact'),max_length=500)

        REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

        USERNAME_FIELD = 'email'

        def __str__(self):
         return '%s - %s' % (self.email, self.cooperative)
