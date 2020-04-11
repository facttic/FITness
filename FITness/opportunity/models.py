import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _
from FITness.candidate.models import TechnologyExpertise


class Client(models.Model):
    name = models.CharField(_('name'), max_length=256)
    url = models.CharField(_('url'), max_length=256, blank=True, null=True)
    mail = models.EmailField(_('email'), max_length=256, blank=True, null=True)
    more_info = models.TextField(_('info'), blank=True, null=True)

    def __str__(self):
        return self.name


class Opportunity(models.Model):

    class OpportunityMode(models.TextChoices):
        FIXED_PRICE = 'FP', _('Fixed-price')
        STAFF_AUGMENTATION = 'SA', _('Staff-augmentation')
        NOT_DEFINED = 'ND', _('Not-defined')

    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('client'))
    mode = models.CharField(
        max_length=2,
        choices=OpportunityMode.choices,
        default=OpportunityMode.NOT_DEFINED,
    )
    candidates_qty = models.PositiveIntegerField(blank=True, null=True)
    mandatory_english = models.BooleanField(default=False)
    more_info = models.TextField(_('info'), blank=True, null=True)
    rate = models.CharField(_('rate'), max_length=256)
    date = models.DateField(_('date'), default=datetime.date.today)

    def __str__(self):
        return self.client.name


class OpportunityExpertise(TechnologyExpertise):
    opportunity = models.ForeignKey(Client, on_delete=models.CASCADE, blank=False, null=False,
                                    verbose_name=_('opportunity'))

    def __str__(self):
        return "{}-{}".format(self.technology.name, self.seniority)
