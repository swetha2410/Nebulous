from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from io import StringIO,BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys


# Create your models here.
class Article(models.Model):
	title=models.CharField(max_length=100)
	slug=models.SlugField()
	body=models.TextField()
	date=models.DateTimeField(auto_now_add=True)
	author=models.ForeignKey(User,default=None, on_delete=models.PROTECT)
	thumb=models.ImageField(default="default.png", blank="True")
	def __str__(self):
		return self.title

	def snippet(self):
		return self.body[:50]+'...'

	