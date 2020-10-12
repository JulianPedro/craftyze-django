from django import forms
from django.utils.translation import gettext_lazy as _


JOB_KIND = (
    ('FULLTIME', _('Full-Time')),
    ('PARTTIME', _('Part-Time')),
    ('FREELANCE', _('Freelance')),
    ('TEMPORARY', _('Temporary')),
)


class PostForm(forms.Form):
    title = forms.CharField()
    company = forms.CharField()
    kind = forms.ChoiceField(choices=JOB_KIND)
    location = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)