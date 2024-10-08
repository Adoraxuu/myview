from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('FBV/<slug:slug>/', views.post_detail, name='FBV_post_detail'),
]