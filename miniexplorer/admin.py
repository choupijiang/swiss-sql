from django.contrib import admin
from .models import Question

# Register your models here.

# admin.site.register(Question)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("title", "created", "author")
    list_filter = ('status', 'created', 'publish', 'author')
    ordering = ('status', 'publish')

