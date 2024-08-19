from django.contrib import admin
from.models import Program, Category

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("title","isActive","slug","category")
    list_display_links = ("title","slug")
    prepopulated_fields = {"slug": ("title",),}
    list_filter = ("title","isActive","category")
    list_editable = ("isActive",)
    search_fields = ("title","description")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
     list_display = ("name","slug",)
     prepopulated_fields = {"slug": ("name",),}