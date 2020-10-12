import django_filters

from job.models import Job


class JobFilter(django_filters.FilterSet):
    category = django_filters.NumberFilter(field_name='category', lookup_expr='name')
    title = django_filters.CharFilter(lookup_expr='iexact')
    restrict_country = django_filters.CharFilter(lookup_expr='iexact')
    kind = django_filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = Job
        fields = ['category', 'title', 'restrict_country', 'kind']
