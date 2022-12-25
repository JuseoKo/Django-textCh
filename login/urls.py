from django.urls import path
from django.contrib.auth import views as loginview
app_name = 'login'

urlpatterns = [
    path('', loginview.LoginView.as_view(template_name='login/login.html') , name='login'),
    path('logout/', loginview.LogoutView.as_view(), name='logout'),
    # path('sign/', views.sign, name='sign'),
]