from django.contrib import admin
from .models import ContactRequest, ShortContact

@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "project_type", "created_at")
    search_fields = ("name", "email")

@admin.register(ShortContact)
class ShortContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    search_fields= ("name", "email")

# Register your models here.
