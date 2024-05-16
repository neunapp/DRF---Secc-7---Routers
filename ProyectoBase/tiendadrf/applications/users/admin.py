from typing import Any
from django.contrib import admin

from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'full_name',
        'gender',
        'is_staff',
        'is_active',
    )
    fields = (
        'email',
        'full_name',
        'gender',
        'is_staff',
        'is_active',
        'password',
        'user_permissions',
    )
    #
    search_fields = ('email', 'full_name',)
    
    #
    # def get_form(self, request: Any, obj: Any | None = ..., change: bool = ..., **kwargs: Any) -> Any:
    #     if obj:
    #         obj.password = ''
    #     return super().get_form(request, obj, change, **kwargs)
    
    # def save_model(self, request: Any, obj: Any, form: Any, change: Any):
    #     print(obj.gender)
    #     if (not obj.is_superuser) and (not change):
    #         obj.set_password(obj.password)
    #     return super().save_model(request, obj, form, change)