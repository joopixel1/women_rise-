from django import template
#from .models import Article
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

register = template.Library()
  
@register.simple_tag
def any_function(value, monkey):
	value = str(value).strip()
	monkey = str(monkey).strip()
	return value==monkey
	
	
@register.simple_tag
def some_body(value):
	return value[:40]
	

@register.simple_tag
def rearrange(value):
	my_list=[]
	
	for word in value.split():
		if word.endswith(':'):
			my_dict = {'speaker': word, 'speech': ""}
			my_list.append(my_dict)
			
		elif my_list:
			my_list[-1]['speech'] += word
			my_list[-1]['speech'] += " "
			
	return my_list
	

@register.simple_tag
def some_author(*value):
	return value[0]
