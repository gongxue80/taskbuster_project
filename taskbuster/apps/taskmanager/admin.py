from django.contrib import admin
from . import models


class ProjectsInline(admin.TabularInline):
    model = models.Project
    extra = 0


class TagsInline(admin.TabularInline):
    model = models.Tag
    extra = 0


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = (
        'username',
        'interaction',
        '_projects',
        '_tags')
    search_fileds = ['user__useranme']

    inlines = [
        ProjectsInline,
        TagsInline,
    ]

    def _projects(self, obj):
        return obj.projects.all().count()

    def _tags(self, obj):
        return obj.tags.all().count()

