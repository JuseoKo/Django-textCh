from django.contrib import admin
from django.urls import path, include

from trans import views as tviews

app_name = 'abouts'
urlpatterns = [
    path('admin/', admin.site.urls),
    #/trans페이지 생성하고 trans/ 로 시작하는 페이지를 요청하면 trans/urls에 등록된 매핑파일을 읽으라는 의미로 url 관리가 수월
    path('trans/', include('trans.urls')),
    #메인페이지(첫페이지)는 임포트한 trans의 views의 default를 호출한다.
    path('', tviews.abuot, name='about'),
    path('js/', tviews.pj_add, name='pj_add'),
    path('sns/', include('sns.urls')),
]
