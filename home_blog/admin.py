from django.contrib import admin
from .models import Art

class artAdmin(admin.ModelAdmin):
    ...

admin.site.register(Art,artAdmin)