from django.contrib import admin
from .models import post
# Register your models here.

@admin.register(post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "state", "fecha_publicacion", "type"]
    list_filter = ["state", "type"]
    raw_id_fields = ["author"]
    ordering = ["-fecha_publicacion"]
