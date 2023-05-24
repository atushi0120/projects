from django.urls import path
from . import views


app_name = 'map'

urlpatterns = [
    path('',views.IndexView.as_view(), name ='index'),
    path('post/',views.CreateArticleView.as_view(), name ='post'),
    path('delete_article/<int:article_id>/', views.delete_article, name='delete_article'),
    path('get_article/<int:article_id>/', views.get_article, name='get_article')
]