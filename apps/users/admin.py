from django.contrib import admin
from users.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'username', 'full_name', 'is_active', 'is_staff')
    search_fields = ('phone', 'username', 'full_name')
    list_filter = ('is_active', 'is_staff', 'date_joined')
