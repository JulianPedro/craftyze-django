from django import template
from django.db.models import Count
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()


@register.filter
def count_category_postion(categories, name):
    print(name)
    try:
        category = categories.get(name=name)
        return category.jobs.count()
    except ObjectDoesNotExist:
        return 0


@register.filter
def category_position(categories, position):
    return categories.filter(front_position=position)[:4]


@register.filter
def top_jobs(jobs):
    return jobs.order_by('identified_at')[:8]


@register.filter
def top_companies(companies):
    return companies.annotate(total_jobs=Count('jobs')).order_by('-total_jobs')[:4]


@register.filter
def current_page(path):
    return path.split('/')[-1]
