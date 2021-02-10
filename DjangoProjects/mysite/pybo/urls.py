# 요청받은 url을 처리하는 파일
from django.urls import path
from . import views

app_name = "pybo"

urlpatterns = [
    path('', views.index, name='index'),#config/url.py에서 이미 경로처리를 한 상태이므로 첫 번째 인자로 ''를 넣어준다.
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
]
