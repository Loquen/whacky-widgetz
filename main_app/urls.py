from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('widget/<int:widget_id>/', views.delete, name='delete'),
]