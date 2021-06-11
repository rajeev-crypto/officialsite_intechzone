from django.contrib import admin
from .models import Contact,Career
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject','message','date',)
    search_fields = ('name', 'email',)
    date_hierarchy = 'date'

class CareerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','message','date',)
    search_fields = ('name', 'email',)
    date_hierarchy = 'date'

# Register your models here.
# admin.site.register(Contact)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Career, CareerAdmin)
