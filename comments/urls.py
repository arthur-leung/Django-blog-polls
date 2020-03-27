from django.urls import path
from . import views

app_name = 'comments'
urlpatterns = [
    path('comment/<int:post_id>/', views.comment, name='comment'),
]
