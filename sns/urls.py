from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
#untitled/url에서 trans/url을 참조하게끔 설정했기 때문에 html에서 {% url 'xx' %} 를 사용하려면 app_name을 설정해주고 {% url 'app_name:xx' %}
#으로 등록한다
app_name = 'sns'
urlpatterns = [
    #name은 html에서 지정할때 필요
    #게시글 리스트
    path('', views.index, name='index'),
    #게시글 내용
    path('<int:content_id>/', views.contents, name='contents'),
    #댓글 작성
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    #게시글 작성
    path('create/', views.sns_create, name='sns_create'),
    #수정 페이지로 넘어가게
    path('revise/<int:question_id>/', views.revise, name='revise_page'),
    #제거
    path('del/<int:question_id>/', views.dl, name='del_page'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)