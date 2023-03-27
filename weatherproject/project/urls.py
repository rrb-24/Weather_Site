from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_request, name='login'),
    path('login', views.login_request, name='login'),
    path('admin_login', views.admin_login, name='weather_page'),
    # path('favo', views.favo, name='favo'),
    path('profile', views.profile, name='profile'),
    path('delhi_page', views.delhi_page, name='delhi_page'),
    path('bengaluru_page', views.bengaluru_page, name='bengaluru_page'),
    path('hyderabad_page', views.hyderabad_page, name='hyderabad_page'),
    path("register", views.register_request, name="register"),
]
