from django.urls import path
from .views import front_page, post_page, search_results,vote, topic_page

urlpatterns = [
    path('front/', front_page, name='front'),
    path('post/<id>/', post_page, name='post'),
    path('search/', search_results, name='search'),
    path('vote/', vote, name='vote'),
    path('topic/<id>/', topic_page, name='topic'),
]