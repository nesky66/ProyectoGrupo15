from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Usuario(AbstractUser):
	score = models.IntegerField(default=0)

	def __gt__(self,otro):

		return self.username > otro.username