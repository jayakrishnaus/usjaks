from django.urls import path
from . import views
from django.conf.urls import url,include

from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [
    path('explorer',views.explorer,name='explorer' ),
    path('questions',views.thequestions,name="questions" ),
    path('Posts',views.Posts,name="Posts" ),
    path('redy',views.redy,name="unansweredquestions" ),
    path('solved',views.solved,name="solvedquestions" ),
    path('theanswers/<name>/',views.theanswers, name="answers" ),
    path('answerpages/<name>/', views.answerpages, name="answerpages" ),
    path('data_pages/<name>/', views.data_pages, name='data_pages')
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
