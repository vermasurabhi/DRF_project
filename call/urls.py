from django.urls import path
from call import views


urlpatterns = [
    path('show/',views.show, name='show'),
]