from django.contrib import admin
from .models import Experience, Review
from django_summernote.admin import SummernoteModelAdmin


class ExperienceAdmin(SummernoteModelAdmin):

    list_display = ('name', 'city', 'category')
    search_fields = ('city', 'category')
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ('city', 'category')
    summernote_fields = ('description')


admin.site.register(Experience, ExperienceAdmin)


class ReviewAdmin(admin.ModelAdmin):

    list_display = ('title', 'experience', 'rating')
    search_fields = ('experience', 'username')
    list_filter = ('experience', 'rating')


admin.site.register(Review, ReviewAdmin)
