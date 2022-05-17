from django.contrib import admin
from .models import Type

admin.site.register(Type)



"""class TypeInline(admin.TabularInline):
    model = Type
    extra = 3

class AddCalAdmin(admin.ModelAdmin):

    inlines = [TypeInline]

admin.site.register(AddCal, AddCalAdmin)"""



# Register your models here.
