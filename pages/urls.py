# blog/urls.py
from django.urls import path
from .views import HomePageView, StoryDetailView, StoryListView
from django.conf import settings
from django.conf.urls.static import static


#make ur urls
urlpatterns = [
	path('', HomePageView.as_view(), name='home'),
	path('list/', StoryListView.as_view(), name='list'),
	path('story/<int:pk>/', StoryDetailView.as_view(), name='detail'), # new
	
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
