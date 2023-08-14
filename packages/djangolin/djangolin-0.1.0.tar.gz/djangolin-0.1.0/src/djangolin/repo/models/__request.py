from django.utils.translation import gettext_lazy as _
from django.db import models


class Request(models.Model):
    path = models.TextField(
        verbose_name=_('Path'),
        blank=False,
        null=False,
    )
    datetime = models.DateField(
        verbose_name=_('Create Date Time'),
        blank=False,
        null=False,
    )
    extra = models.JSONField(
        verbose_name=_('Extra Information'),
        blank=True,
        null=True,
    )

