from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import UserAccount


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = UserAccount
        fields = ("email", 'firstname', 'lastname','user_type')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = UserAccount
        fields =         fields = ("email", 'firstname', 'lastname','user_type')