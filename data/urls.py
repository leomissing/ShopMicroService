from django.urls import path

from . import views

urlpatterns = [
    path('insert/', views.insert, name='insert'),
    path('find_by_id/', views.find_by_id, name='find_by_id'),
    path('sort_by_name/', views.sort_by_name, name='sort_by_name'),
    path('sort_by_param/', views.sort_by_param, name='sort_by_param'),
    path('insert_array/', views.insert_array, name='insert_array')
]