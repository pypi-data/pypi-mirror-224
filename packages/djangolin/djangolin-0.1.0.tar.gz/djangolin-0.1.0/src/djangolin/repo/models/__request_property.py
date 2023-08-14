from django.utils.translation import gettext_lazy as _
from django.db import models


class RequestProperty(models.Model):
    request = models.ForeignKey(
        verbose_name=_('Request'),
        to='djangolin.Request',
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    key = models.CharField(
        verbose_name=_('Key'),
        max_length=255,
        blank=False,
        null=False,
    )
    value = models.TextField(
        verbose_name=_('Value'),
        blank=True,
        null=True,
    )

