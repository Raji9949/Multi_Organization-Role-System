from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Organization

# Custom user creation form for creating new users
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'organization', 'role']
        widgets = {
            'role': forms.Select(choices=[
                ('Admin', 'Admin'),
                ('Editor', 'Editor'),
                ('Viewer', 'Viewer'),
            ]),
        }

    def __init__(self, *args, **kwargs):
        # Limit organizations to those the admin has access to
        current_user = kwargs.pop('current_user', None)
        super().__init__(*args, **kwargs)
        if current_user and not current_user.is_superuser:
            self.fields['organization'].queryset = Organization.objects.filter(
                id=current_user.organization.id
            )

# Custom user update form for editing existing users
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'organization', 'role']
        widgets = {
            'role': forms.Select(choices=[
                ('Admin', 'Admin'),
                ('Editor', 'Editor'),
                ('Viewer', 'Viewer'),
            ]),
        }

    def __init__(self, *args, **kwargs):
        # Limit organizations to those the admin has access to
        current_user = kwargs.pop('current_user', None)
        super().__init__(*args, **kwargs)
        if current_user and not current_user.is_superuser:
            self.fields['organization'].queryset = Organization.objects.filter(
                id=current_user.organization.id
            )

# Organization form for creating and updating organizations
class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['name', 'address', 'is_main']
        widgets = {
            'is_main': forms.CheckboxInput(),
        }

    def __init__(self, *args, **kwargs):
        # Prevent non-superusers from creating main organizations
        current_user = kwargs.pop('current_user', None)
        super().__init__(*args, **kwargs)
        if current_user and not current_user.is_superuser:
            self.fields['is_main'].widget = forms.HiddenInput()
