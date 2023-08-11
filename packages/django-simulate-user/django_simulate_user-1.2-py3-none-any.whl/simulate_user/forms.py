from typing import Type
from django import forms
from django.contrib.auth import get_user_model
from django.db.models import ForeignKey


UserModel = get_user_model()


# noinspection PyProtectedMember
class UserSwitchForm(forms.Form):
    """
    Form for switching or simulating users based on their primary key (PK), username, or email.

    Fields:
    - user_pk: The primary key of the user. Its form field type is determined by the nature of the primary key
               of the custom user model (either a ForeignKey or CharField).
    - username: The username of the user to switch/simulate.
    - email: The email of the user to switch/simulate.
    - unauthenticated: A boolean field indicating if the user wants to simulate as an unauthenticated user.
    - enabled: A boolean field indicating if the user simulation feature should be enabled.
    - hide: A boolean field for deciding whether to hide the simulation UI components, e.g., a control bar.

    Usage:
    This form can be used in views to decide which user to simulate or switch to. It also controls settings like
    whether to show a simulation control bar (through the 'hide' field) and whether the simulation feature is active
    (through the 'enabled' field).
    """
    # Determine the name and form field class of the primary key based on the custom user model's configuration.
    primary_key_name: str = UserModel._meta.pk.name
    primary_key_field_class: Type[forms.ModelChoiceField | forms.CharField] = forms.ModelChoiceField if isinstance(
        UserModel._meta.pk, ForeignKey
    ) else forms.CharField

    user_pk: primary_key_field_class = primary_key_field_class(
        required=False,
        label=primary_key_name.capitalize().replace('_', ' ')
    )
    username: str | None = forms.CharField(required=False, label='Username')
    email: str | None = forms.EmailField(required=False, label='Email')
    unauthenticated: bool = forms.BooleanField(required=False, label='Unauthenticated')
    enabled: bool = forms.BooleanField(required=False, label='Enabled')
    hide: bool = forms.BooleanField(required=False, label='Hide')
