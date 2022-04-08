from django.urls import path
# これ忘れないようにする！！
from . import views

app_name = 'attendance'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('result/', views.ResultView.as_view(), name='result'),
]
