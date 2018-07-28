from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
	title = models.TextField(null =True, blank= True)
	status = models.CharField(default = "inactive",max_length = 10)
	created_by = models.ForeignKey(User,null =True,blank = True,on_delete = "cascade")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	start_date = models.DateTimeField(null =True,blank =True)
	end_date = models.DateTimeField(null =True,blank =True)


	def __str__(self):
		return self.title


class choice(models.Model):
	question = models.ForeignKey('polls.Question',on_delete = "cascade")
	text = models.TextField(null =True, blank = True)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.text
