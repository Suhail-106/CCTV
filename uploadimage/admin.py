from django.contrib import admin
from uploadimage.models import ImageURL, contactinfo,CCTVElectrical,datasave

admin.site.register(ImageURL)
admin.site.register(contactinfo)
admin.site.register(CCTVElectrical)

class DataSaveAdmin(admin.ModelAdmin):
    list_display = ('username','email','updated_at')
    readonly_fields = ('updated_at',)
admin.site.register(datasave, DataSaveAdmin)

# Register your models here.
