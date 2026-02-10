from django.contrib import admin
from .models import NewsletterSubscriber

@admin.register(NewsletterSubscriber)
class NewsletteSubcriberAdmin(admin.ModelAdmin):
    list_display = ("email", "created_at")
    ordering = ("-created_at",)

# Register your models here.
