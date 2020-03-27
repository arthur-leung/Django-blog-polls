from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('blog/<int:pk>/', views.detail, name='detail'),
    path('archives/<int:year>/<int:month>/', views.archives, name='archives'),
    path('category/<int:category_id>/', views.category, name='category'),
    path('tag/<int:tag_id>/', views.tag, name='tag'),
]
