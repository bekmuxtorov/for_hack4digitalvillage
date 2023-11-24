from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

from rest_framework.authtoken.models import TokenProxy as Token
from rest_framework.authtoken.admin import TokenAdmin
from .models import Account, TokenProxy
from .forms import UserChangeForm, UserCreationForm

admin.site.site_header = "Karer Project Admin"
admin.site.index_title = 'Karer Site Administration'

admin.site.unregister(Token)

admin.site.register(TokenProxy, TokenAdmin)


@admin.register(Account)
class AccountAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('phone_number', 'full_name', 'farm_name', 'is_staff')
    search_fields = ('phone_number', 'full_name', 'farm_name')
    list_filter = ('is_staff',)
    ordering = ('-id',)

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("phone_number", "full_name", "password1", "password2"),
            },
        ),
    )
