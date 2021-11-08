from django.contrib import admin
from contact.models import contact
# Register your models here.
class contactadmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone_number', 'email']

admin.site.register(contact, contactadmin)
