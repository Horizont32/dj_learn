from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='index'),
    path('categs/<slug:id>/', views.categs, name='categs')
]