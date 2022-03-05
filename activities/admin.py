from django.contrib import admin
from .models import Experience, Review


class ExperienceAdmin(admin.ModelAdmin):

    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Review)