from django.db import models
from django.utils.translation import gettext_lazy as _


class SeniorityLevel(models.TextChoices):
    JUNIOR = 'JR', _('Junior')
    SEMI_SENIOR = 'SSR', _('Semisenior')
    SENIOR = 'SR', _('Senior')
    NINJA = 'NJ', _('Ninja')


class EnglishLevel(models.TextChoices):
    JUNIOR = 'JR', _('Junior')
    ADVANCED = 'AD', _('Advanced')
    NATIVE = 'NT', _('Native')


class Candidate(models.Model):

    class Availability(models.TextChoices):
        BUSY = 'BS', _('Busy')
        FREE = 'FR', _('Free')
        COULD_BE_FREE = 'CBF', _('Could be free')

    name = models.CharField(_('name'), max_length=256)
    english_level = models.CharField(
        max_length=2,
        choices=EnglishLevel.choices,
        default=EnglishLevel.JUNIOR,
    )
    availability = models.CharField(
        max_length=3,
        choices=Availability.choices,
        default=Availability.FREE,
    )

    def __str__(self):
        return self.name


class Technology(models.Model):
    name = models.CharField(_('name'), max_length=256)
    def __str__(self):
        return self.name


class CandidateExperience(models.Model):

    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, blank=False, null=False,
                                  verbose_name=_('candidate'))
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE, blank=False, null=False,
                                   verbose_name=_('technology'))

    seniority = models.CharField(
        max_length=3,
        choices=SeniorityLevel.choices,
        default=SeniorityLevel.JUNIOR,
    )

    experience_years = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return "{}-{}".format(self.technology.name, self.seniority)
