import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _


class Company(models.Model):
    """ Company Model """
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    name = models.CharField(verbose_name=_('Company Name'), max_length=120)
    website = models.URLField(verbose_name=_('Website'), blank=True, null=True)
    image = models.ImageField(verbose_name=_('Image'), upload_to='companies/')

    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')

    def __str__(self):
        return self.name
