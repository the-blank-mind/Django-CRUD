
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name='index'),
    path('deletedata/<int:id>/', views.delete, name='deletedata'),
    path('<int:id>/', views.update, name='update'),


]