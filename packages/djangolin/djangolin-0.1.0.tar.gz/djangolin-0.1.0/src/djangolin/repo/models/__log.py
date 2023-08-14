from django.utils.translation import gettext_lazy as _
from django.db import models


class Log(models.Model):
    request = models.ForeignKey(
        verbose_name=_('Request'),
        to='djangolin.Request',
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    typ = models.CharField(
        verbose_name=_('Type'),
        max_length=15,
        blank=False,
        null=False,
    )
    msg = models.TextField(
        verbose_name=_('Message'),
        blank=False,
    )
    datetime = models.DateField(
        verbose_name=_('Created Date Time'),
        blank=False,
        null=False,
    )
    extra = models.JSONField(
        verbose_name=_('Extra Information'),
        blank=True,
        null=True,
    )

