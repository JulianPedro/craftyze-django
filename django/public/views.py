from django.shortcuts import render
from django.views.generic import TemplateView

from company.models import Company
from job.models import Job, Category


class Home(TemplateView):
    template_name = "public/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['companies'] = Company.objects.all()
        context['jobs'] = Job.objects.all()
        context['categories'] = Category.objects.all()
        return context

