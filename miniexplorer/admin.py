from django.contrib import admin
from .models import Question
from django import forms
from django_ace import AceWidget

# Register your models here.

# admin.site.register(Question)


class QuestionAdminForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["title", "sql"]
        widgets = {
            "sql": AceWidget(mode='pgsql', theme='twilight'),
        }


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    form = QuestionAdminForm
    list_filter = ('status', 'created', 'publish', 'author')
    list_display = ("title", "created", "author")
    ordering = ('status', 'publish')
