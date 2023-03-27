# from collections import UserDict
from django.contrib.auth.models import User
from django.shortcuts import  render, redirect
from django.contrib.auth import login, authenticate


from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib import messages


# def login(request):
#     return render(request, 'login.html')

def admin_login(request):
    current_user=request.user
    print(current_user)
    user_details=User.objects.get(username=current_user)
    print(user_details)
    return render(request, 'weather_page.html',{'user_details':user_details})

def favo(request):
    return render(request, 'favo.html')

def delhi_page(request):
    return render(request, 'delhi_page.html')

def bengaluru_page(request):
    return render(request, 'bengaluru_page.html')

def hyderabad_page(request):
    return render(request, 'hyderabad_page.html')




def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request,user)
			messages.success(request, "Registration successful." )
			return redirect('login')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})



def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request,user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect('weather_page')
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name='login.html', context={"login_form":form})



# def profile(request):
#     current_user=request.user
#     user_details=User.objects.get(username=current_user)
#     return render(request,'profile.html',{'user_details':user_details})

def profile(request):
	return render(request,'profile.html')
