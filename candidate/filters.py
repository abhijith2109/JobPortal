import django_filters
from employer.models import Jobs

class JobFilter(django_filters.FilterSet):
    salary=django_filters.NumberFilter(field_name="salary",lookup_expr="lt")
    job_title=django_filters.CharFilter(field_name="job_title",lookup_expr="contains")
    location=django_filters.CharFilter(field_name="location",lookup_expr="contains")
    class Meta:
        model=Jobs
        fields=["posted_by",
                "job_title",
                "location",
                "salary",
                "qualification"]
