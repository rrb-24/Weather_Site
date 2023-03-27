# from django import forms
# # from django.forms import ModelForm
# # from .models import account
# from django.contrib.auth.forms import AuthenticationForm



# class LoginForm(AuthenticationForm):
#     username = forms.CharField(max_length=254,
#                                widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': True}))
#     password = forms.CharField(label="Password",
#                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))





from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user