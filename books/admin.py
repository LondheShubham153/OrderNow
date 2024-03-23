from django.contrib import admin
from .models import Inventory

# Register your models here.
class InventoryAdmin(admin.ModelAdmin):
    list_display = ("title","quantity","status")

admin.site.register(Inventory,InventoryAdmin)
