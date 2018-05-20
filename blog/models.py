from django.db import models

# Create your models here.
class BlogPost(models.Model):
	title=models.CharField(max_length= 250)
	slug= models.SlugField()
	date= models.DateTimeField(auto_now_add=True)
	body= models.TextField()

	def __str__(self):
		return self.title

	def peekpost(self):
		return self.body[:60] + '...'
