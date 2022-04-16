from django import forms
from django.contrib.auth.models import User
from accounts.models import Profile
from django.contrib.auth import get_user_model


# Create your views here.
class UserCreationForm(forms.ModelForm):
    password = forms.CharField(
        label='Пароль', strip=False, required=True,
        widget=forms.PasswordInput
    )
    password_confirm = forms.CharField(
        label='Подтвердить пароль', strip=False, required=True, widget=forms.PasswordInput
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            self.add_error('password', 'Пароли не совпадают')
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = [
            'username', 'password', 'password_confirm'
        ]


class ProfileCreateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['email', 'phone', 'avatar', 'user_or_company']


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username']


class ProfileChangeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email', 'phone', 'avatar']
        exclude = ['user']


class PasswordChangeForm(forms.ModelForm):
    password = forms.CharField(strip=False, widget=forms.PasswordInput)
    password_confirm = forms.CharField(strip=False, widget=forms.PasswordInput)
    password_old = forms.CharField(strip=False, widget=forms.PasswordInput)

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают')
        return password_confirm

    def clean_password_old(self):
        old_password = self.cleaned_data.get('password_old')
        if not self.instance.check_password(old_password):
            raise forms.ValidationError('Неправильно указан старый пароль')
        return old_password

    def save(self, commit=True):
        user = self.instance
        user.set_password(self.cleaned_data['password_confirm'])
        if commit:
            user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ['password', 'password_confirm', 'password_old']
