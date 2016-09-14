from django.contrib import admin
from guest.models import Event, Guest


# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ["name", "status", "start_time", "address"]


class GuestAdmin(admin.ModelAdmin):
    list_display = ["id", "realname", "phone", "email", "type", "sign", "event"]
    list_display_links = ('realname', 'phone')  # œ‘ æ¡¥Ω”
    search_fields = ['realname','phone']

admin.site.register(Event, EventAdmin)
admin.site.register(Guest, GuestAdmin)


