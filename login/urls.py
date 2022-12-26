from django.urls import path
from django.contrib.auth import views as loginview
from . import views
app_name = 'login'

urlpatterns = [
    path('', views.logins, name='login'),
    path('logout/', loginview.LogoutView.as_view(), name='logout'),
    path('sign/', views.sign, name='sign'),
]