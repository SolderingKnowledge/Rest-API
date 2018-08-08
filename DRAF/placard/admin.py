from django.contrib import admin
from .models import Placard

class PlacardModelAdmin(admin.ModelAdmin):
    list_display = ["title", "updated", "timestamp"]
    list_display_links = ["updated"]
    list_editable = ["title"]
    list_filter = ["updated", "timestamp"]

    search_fields = ["title", "content"]
    class Meta:
        model = Placard


admin.site.register(Placard, PlacardModelAdmin)