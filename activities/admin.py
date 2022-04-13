from django.contrib import admin
from .models import Experience, Review
from django_summernote.admin import SummernoteModelAdmin

# class ExperienceAdmin(admin.ModelAdmin):
#
#    prepopulated_fields = {"slug": ("name",)}


class ExperienceAdmin(SummernoteModelAdmin):

    summernote_fields = ('description')
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Review)
