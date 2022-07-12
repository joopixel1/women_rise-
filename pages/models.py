from django.db import models

# Create your models here.
class Stories(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	image = models.ImageField(upload_to="images/", default='/images/default.jpg')

	def __str__(self):
		return self.title
		
	def get_absolute_url(self): # new
		return reverse('post_detail', args=[str(self.id)])
