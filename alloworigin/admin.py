from django.contrib import admin
from .models import Request

class RequestAdmin(admin.ModelAdmin):
    list_display = ('dest','ip','date')
admin.site.register(Request, RequestAdmin)
