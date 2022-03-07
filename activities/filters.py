from .models import Experience
import django_filters


class ExperienceFilter(django_filters.FilterSet):

    class Meta:
        model = Experience
        fields = ['category', 'city', 'price', ]