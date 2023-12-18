from django.contrib import admin
from .models import User, Token

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["mail", "name", "surname"]

@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ["user", "key"]