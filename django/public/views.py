from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from company.models import Company
from job.models import Job, Category
from job.forms import PostForm
from job.filters import JobFilter


class Home(TemplateView):
    template_name = 'public/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['companies'] = Company.objects.all()
        context['jobs'] = Job.objects.all()
        context['categories'] = Category.objects.all()
        return context


class BrowserJob(ListView):
    model = Job
    paginate_by = 10
    template_name = 'public/browsejobs.html'

    def get_queryset(self):
        queryset = self.model.objects.all()
        filtered = JobFilter(self.request.GET, queryset=queryset)
        return filtered.qs


class PostJob(FormView):
    form_class = PostForm
    template_name = 'public/new-post.html'