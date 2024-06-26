from django.forms import DateTimeInput
from django_filters import FilterSet, ChoiceFilter, DateTimeFilter,  CharFilter
from .models import Post, CATEGORY_CHOICES

class PostFilter(FilterSet):

    categoryType = ChoiceFilter(
        field_name='categoryType',
        choices=CATEGORY_CHOICES,
        label= ('Поиск по категории')
    )

    dateCreation = DateTimeFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type':'datetime-local'},
        ),
        label='Позже указываемой даты'
    )

    class Meta:
        model = Post
        fields = {
            'title': ['icontains']
        }