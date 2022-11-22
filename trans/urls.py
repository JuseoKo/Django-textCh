from django.urls import path
from . import views
#untitled/url에서 trans/url을 참조하게끔 설정했기 때문에 html에서 {% url 'xx' %} 를 사용하려면
# app_name을 설정해주고 {% url 'app_name:xx' %} 으로 등록한다
app_name = 'trans'
urlpatterns = [
    #name은 html에서 지정할때 필요
    path('<str:file_name>/', views.main, name='tr'),
    path('add/<str:file_name>/', views.main_add, name='add'),
]