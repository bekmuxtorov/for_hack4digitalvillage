from django.contrib.auth.forms import UserCreationForm as OldUserCreationForm, UserChangeForm as OldUserChangeForm

from .models import Account


class UserCreationForm(OldUserCreationForm):
    class Meta:
        model = Account
        fields = ("phone_number", "full_name")


class UserChangeForm(OldUserChangeForm):
    class Meta:
        model = Account
        fields = '__all__'
