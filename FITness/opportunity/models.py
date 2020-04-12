import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _
from FITness.candidate.models import TechnologyExpertise, SeniorityLevel


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
    mandatory_english = models.BooleanField(default=False)
    more_info = models.TextField(_('info'), blank=True, null=True)
    rate = models.CharField(_('rate'), max_length=256, blank=True, null=True)
    date = models.DateField(_('date'), default=datetime.date.today)

    @property
    def mode_description(self):
        return self.OpportunityMode(self.mode).label

    def __str__(self):
        return self.client.name


class OpportunityProfile(models.Model):
    opportunity = models.ForeignKey(Opportunity, on_delete=models.CASCADE, blank=False, null=False,
                                    verbose_name=_('opportunity'))
    profiles_qty = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return "Cliente: {} - Perfiles: {}".format(self.opportunity.client.name, self.profiles_qty)


class ProfileExpertise(TechnologyExpertise):
    opportunity_profile = models.ForeignKey(OpportunityProfile, on_delete=models.CASCADE, blank=False, null=False,
                                            verbose_name=_('opportunity_profile'))

    def __str__(self):
        return "{} profiles: {} / {}".format(self.opportunity_profile.profiles_qty, self.technology.name,
                                             SeniorityLevel(self.seniority).label)
