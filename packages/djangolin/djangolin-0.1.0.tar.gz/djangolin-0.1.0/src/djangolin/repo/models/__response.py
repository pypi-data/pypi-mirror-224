from django.utils.translation import gettext_lazy as _
from django.db import models


class Response(models.Model):
    request = models.ForeignKey(
        verbose_name=_('Request'),
        to='djangolin.Request',
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    status_code = models.PositiveSmallIntegerField(
        verbose_name=_('Status Code'),
        default=200,
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

