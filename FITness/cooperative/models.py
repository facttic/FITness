from django.db import models
from django.utils.translation import gettext_lazy as _


class Cooperative(models.Model):

    class CooperativeStatus(models.TextChoices):
        INACTIVE = 'IN', _('Inactive')
        REGULAR = 'RG', _('Regular')
        NICE = 'NC', _('Nice')
        CRITICAL = 'CR', _('Critical')

    name = models.CharField(_('name'), max_length=256)
    status = models.CharField(
        max_length=2,
        choices=CooperativeStatus.choices,
        default=CooperativeStatus.INACTIVE,
    )

    def __str__(self):
        return "{}: {}".format(self.name, self.CooperativeStatus(self.status).label)
