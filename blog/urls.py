from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('<str:arg>/', views.HomeView.as_view(), name='index'),
    path('example/<str:arg>/', views.example_view, name='example_name'),
    path('example2/<str:arg>/', views.example_view_2, name='example_name_2'),
    path('example3/<str:my_arg>/', views.example_view_3, name='example_name_3'),
    path('example4/<str:arg>/', views.example_view_4, name='example_name_4'),
    path('example5/<str:arg>/', views.example_view_5, name='example_name_5'),
]