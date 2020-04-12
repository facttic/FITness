from django.db import models
from django.utils.translation import gettext_lazy as _


class Cooperative(models.Model):

    class CooperativeStatus(models.TextChoices):
        INACTIVE = 'IN', _('Inactive')
        CRITICAL = 'CR', _('Critical')
        REGULAR = 'RG', _('Regular')
        NICE = 'NC', _('Nice')

    name = models.CharField(_('name'), max_length=256)
    status = models.CharField(
        max_length=2,
        choices=CooperativeStatus.choices,
        default=CooperativeStatus.INACTIVE,
    )

    def __str__(self):
        return "{}: {}".format(self.name, self.CooperativeStatus(self.status).label)

    def set_status(self, all_candidates, free_candidates):
        if all_candidates:
            availability = free_candidates / all_candidates * 100
            if availability < 33:
                self.status = self.CooperativeStatus.NICE
            elif availability < 66:
                self.status = self.CooperativeStatus.REGULAR
            else:
                self.status = self.CooperativeStatus.CRITICAL
        else:
            self.status = self.CooperativeStatus.INACTIVE
        self.save()

    @property
    def status_description(self):
        return self.CooperativeStatus(self.status).label
