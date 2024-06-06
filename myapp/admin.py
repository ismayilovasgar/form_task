from django.contrib import admin
from .models import *

# Register your models here.


class RegisterModelAdmin(admin.ModelAdmin):
    list_display = ["firstname", "lastname", "programming_lang", "email"]


admin.site.register(Register, RegisterModelAdmin)

