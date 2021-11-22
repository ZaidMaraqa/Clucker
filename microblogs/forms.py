from django import forms
from .models import User
from .models import Post
from django.core.validators import RegexValidator

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'bio']
        widgets = { "bio": forms.Textarea()}

    new_password = forms.CharField(
        label = "Password",
        widget = forms.PasswordInput(),
        validators = [RegexValidator(
        regex = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).*$',
        message = 'Password must contain a uppercase character, a lowercase'
                  'character and a number'
        )]
    )
    password_confirmation = forms.CharField(label = "Password confirmation", widget = forms.PasswordInput())


    def clean(self):
        super().clean()
        new_password = self.cleaned_data.get('new_password')
        password_confirmation = self.cleaned_data.get('password_confirmation')
        if new_password != password_confirmation:
            self.add_error('password_confirmation', 'Confirmation does not match password.')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text']
        widgets = {'text': forms.Textarea()}
    
