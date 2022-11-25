from django.contrib import admin
from. models import Persona, Phone
from import_export import resources
from import_export.admin import ExportActionMixin

class PhoneResources(resources.ModelResource):
    class Meta:
        model = Phone
        fields = ('phone', 'contack')

class PhoneAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = PhoneResources




admin.site.register(Persona)
admin.site.register(Phone, PhoneAdmin)


