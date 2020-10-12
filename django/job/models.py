import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext_lazy as _

from django_countries.fields import CountryField
from ckeditor.fields import RichTextField


class Job(models.Model):
    """ Job Model """

    class Kind(models.TextChoices):
        FULL_TIME = 'FULLTIME', _('Full-Time'),
        PART_TIME = 'PARTTIME', _('Part-Time')
        FREE_LANCE = 'FREELANCE', _('Freelance')
        TEMPORARY = 'TEMPORARY', _('Temporary')

    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    title = models.CharField(verbose_name=_('Job'), max_length=240)
    identified_at = models.DateTimeField(verbose_name=_('Identified'), auto_now_add=True)
    kind = models.CharField(max_length=240, choices=Kind.choices, default=Kind.FULL_TIME)
    category = models.ForeignKey('job.Category', verbose_name=_('Category'), on_delete=models.CASCADE,
                                 related_name='jobs')
    company = models.ForeignKey('company.Company', verbose_name=_('Company'), on_delete=models.CASCADE,
                                related_name='jobs')
    position = models.CharField(verbose_name=_('Position'), max_length=240)
    tags = ArrayField(models.CharField(max_length=240), blank=True)
    link = models.URLField(verbose_name=_('Link'), blank=True, null=True)
    content = RichTextField()
    restrict_country = CountryField()
    
    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'

    def __str__(self):
        return f'{self.company.name} - {self.title}'


class Category(models.Model):
    """ Category Model """

    class Position(models.TextChoices):
        FIRST = 'FIRST', _('First'),
        SECOND = 'SECOND', _('Second')
        THIRD = 'THIRD', _('Third')
        FOURTH = 'FOURTH', _('Fourth')

    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    name = models.CharField(verbose_name=_('Category'), max_length=240)
    is_top = models.BooleanField(verbose_name=_('Is top'), default=False)
    front_position = models.CharField(max_length=6, choices=Position.choices, blank=True, null=True)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
