from django.db import models
from django.utils.translation import gettext_lazy as _


class Cooperative(models.Model):
    name = models.CharField(_('name'), max_length=256)

    def __str__(self):
        return self.name
