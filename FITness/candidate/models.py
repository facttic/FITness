from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from FITness.cooperative.models import Cooperative


class SeniorityLevel(models.TextChoices):
    JUNIOR = 'JR', _('Junior')
    SEMI_SENIOR = 'SSR', _('Semisenior')
    SENIOR = 'SR', _('Senior')
    NINJA = 'NJ', _('Ninja')


class EnglishLevel(models.TextChoices):
    JUNIOR = 'JR', _('Junior')
    ADVANCED = 'AD', _('Advanced')
    NATIVE = 'NT', _('Native')


class CandidateAvailability(models.TextChoices):
        BUSY = 'BS', _('Busy')
        FREE = 'FR', _('Free')
        COULD_BE_FREE = 'CBF', _('Could be free')


class Candidate(models.Model):
    cooperative = models.ForeignKey(Cooperative, on_delete=models.CASCADE, blank=False, null=False,
                                    verbose_name=_('cooperative'))
    name = models.CharField(_('name'), max_length=256)
    english_level = models.CharField(
        max_length=2,
        choices=EnglishLevel.choices,
        default=EnglishLevel.JUNIOR,
    )
    availability = models.CharField(
        max_length=3,
        choices=CandidateAvailability.choices,
        default=CandidateAvailability.FREE,
    )

    __original_availability = None

    def __init__(self, *args, **kwargs):
        super(Candidate, self).__init__(*args, **kwargs)
        self.__original_availability = self.availability

    def save(self, *args, **kwargs):
        new = not self.pk
        super().save(*args, **kwargs)
        if new or self.availability != self.__original_availability:
            candidates = Candidate.objects.filter(cooperative=self.cooperative)
            all_candidates = candidates.count()
            free_candidates = candidates.filter(availability=CandidateAvailability.FREE).count()
            self.cooperative.set_status(all_candidates, free_candidates)

    def __str__(self):
        return "{}: {}".format(self.name, CandidateAvailability(self.availability).label)


class Technology(models.Model):
    name = models.CharField(_('name'), max_length=256)

    def __str__(self):
        return self.name


class TechnologyExpertise(models.Model):
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE, blank=False, null=False,
                                   verbose_name=_('technology'))
    seniority = models.CharField(
        max_length=3,
        choices=SeniorityLevel.choices,
        default=SeniorityLevel.JUNIOR,
    )
    experience_years = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        abstract = True


class CandidateExpertise(TechnologyExpertise):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, blank=False, null=False,
                                  verbose_name=_('candidate'))

    def __str__(self):
        return "{} ({}): {}-{}".format(self.candidate.name, self.candidate.cooperative.name, self.technology.name, SeniorityLevel(self.seniority).label)
