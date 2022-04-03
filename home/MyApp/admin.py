from django.contrib import admin
from .models import Contact



admin.site.site_header = 'Apparal Shop'
admin.site.index_title = 'Useful Information'
admin.site.site_title = 'Apparel Shop'

# Register your models here.
admin.site.register(Contact)



