from django.shortcuts import render
from .models import Stories
from django.views.generic import ListView, TemplateView, DetailView

# Create your views here.
class HomePageView(TemplateView):
	model = Stories
	template_name = 'home.html'

class StoryListView(ListView):
	model = Stories
	template_name = 'list_page.html'

class StoryDetailView(DetailView):
	model = Stories
	template_name = 'story_detail.html'
