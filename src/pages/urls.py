from django.urls import path
from .views import front_page, post_page, search_results,vote, topic_page,comment_vote

urlpatterns = [
    
    path('post/<id>/', post_page, name='post'),
    path('search/', search_results, name='search'),
    path('vote/', vote, name='vote'),
    path('comment-vote/', comment_vote, name='comment_vote'),
    path('topic/<id>/', topic_page, name='topic'),
]