from django.urls import path, include

from hike import views

urlpatterns = [

    path('',views.home,name='home')
]
