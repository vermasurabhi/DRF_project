from django.urls import path
from . import views
from .views import StudentView


urlpatterns = [
    path('',views.index, name='index'),
    path('basic/',StudentView.as_view(), name='basic'),
    path('basic/<int:id>/',StudentView.as_view()),
]

