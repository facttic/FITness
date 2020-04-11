from django.db import models
from django.utils.translation import gettext_lazy as _
from FITness.cooperative.models import Cooperative
from django.contrib.auth.models import User

class CooperativeUser(models.Model):
      user = models.OneToOneField(User, on_delete=models.CASCADE)
      cooperative = models.ForeignKey(Cooperative, on_delete=models.CASCADE, blank=False, null=False,
                                     verbose_name=_('cooperative'))
      other_contact = models.CharField(_('contact'),max_length=500)

      def __str__(self):
          return self.user.first_name
