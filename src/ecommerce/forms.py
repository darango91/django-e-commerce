from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class ContactForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'form_full_name',
            'placeholder': 'Your full name'
        }), label=''
    )
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Your email you@email.com'
        }
    ), label='')
    content = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Your message'
        }), label=''
    )
    #
    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if not "gmail.com" in email:
    #         raise forms.ValidationError('Email has to be gmail.com')
    #     return email


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'col'}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'col'}
    ))


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm password')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError('Username is taken!')
        return username

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password2 != password:
            raise forms.ValidationError('Passwords must match!')

        return data
