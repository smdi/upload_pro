from django.contrib import admin

from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name' ,'image')
    search_fields = ('name',)
    ordering = ('name',)


admin.site.register(Student ,StudentAdmin)
