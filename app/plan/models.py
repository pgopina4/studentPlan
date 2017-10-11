from django.db import models
from django.utils import timezone

class Post1(models.Model):
    Name =  models.TextField(default='Sanjeev')
    Standard = models.TextField(default='7th')
    Chapter =  models.TextField(default='Some 7th chapter')
    Goal_old1 =  models.TextField(default='')
    Goal_old2 =  models.TextField(default='')
    Goal_now1 =  models.TextField(default='')
    Goal_now2 =  models.TextField(default='')
    Goal_now3 =  models.TextField(default='')
    Goal_now4 =  models.TextField(default='')	
    created_date = models.DateTimeField(
            default=timezone.now)
    
 #   def publish(self):
     #   self.published_date = timezone.now()
      #  self.save()

class Update(models.Model):
	Name =  models.TextField(default='Sanjeev')
	Standard = models.TextField(default='7th')
	What_did_I_do_at_home = models.TextField()
	What_I_did_towards_my_goals = models.TextField()
	What_did_I_learn_new = models.TextField(default='Not much')
	created_date = models.DateTimeField(
            default=timezone.now)

class Update1(models.Model):
	Name =  models.TextField(default='Sanjeev')
	Standard = models.TextField(default='Grade 7th')
	How_do_I_feel_after_my_assessment = models.TextField()
	What_I_will_do_different_next_week = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	goalcompleted= models.TextField(default="1")

class allstudent(models.Model):
       Standard = models.TextField(default='7th')
       Name =  models.TextField(default='Sanjeev')

class Progress(models.Model):
      Standard = models.TextField(default='7th')
      Name =  models.TextField(default='Sanjeev')
      Outcomes = models.TextField(default='chosen Goals')
      created_date = models.DateTimeField(default=timezone.now)
      Assessment_Marks =  models.TextField(default='1')  
