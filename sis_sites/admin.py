from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.db import models
from django.utils.translation import ugettext_lazy as _

from pagedown.widgets import AdminPagedownWidget
from .models import Snippet, ContentBlock


@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    list_display = ['name']


class ContentBlockInline(admin.StackedInline):
    model = ContentBlock
    extra = 1
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }

# Define a new FlatPageAdmin
class FlatPageAdmin(FlatPageAdmin):
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
        (_('Advanced options'), {
            'classes': ('collapse', ),
            'fields': (
                # 'enable_comments',
                # 'registration_required',
                'template_name',
            ),
        }),
    )
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }
    inlines = [ContentBlockInline]


# Re-register FlatPageAdmin
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
