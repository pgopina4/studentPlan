from django import forms
from .models import Post1
from random import randint
from .models import Update
from .models import Update1
from .models import Progress
from django.utils import timezone


class PostForm(forms.Form):
    Name = forms.CharField(max_length=200)
    Standard = forms.CharField(max_length=200)
    My_goal_for_this_week = forms.CharField(max_length=200,label="My goal for this week")
    What_I_did_today_towards_my_goals = forms.CharField(max_length=200,label="What I did today towards my goals")
    How_did_I_feel_after_my_assessment = forms.CharField(max_length=200,label="How did I feel after my assessment")
    Work_I_did_at_home = forms.CharField(max_length=200,label="What I did at home yesterday")
    What_can_I_do_now_that_I_could_not_do_last_week = forms.CharField(max_length=200,label="What can I do now that I could not do last week")

   

class UpdateForm(forms.Form):
    What_did_I_do_at_home = forms.CharField(max_length=200,label="What did I do at home")
    What_I_did_towards_my_goals = forms.CharField(max_length=200, label="What I did towards my goals")
    What_did_I_learn_new =  forms.CharField(max_length=200, label="What did I learn new")


class Update1Form(forms.Form):
    How_do_I_feel_after_my_assessment = forms.CharField(max_length=200, label="How do I feel after my assessment")
    What_I_will_do_different_next_week = forms.CharField(max_length=200, label="What will I do differently next week")

class ProgressForm(forms.Form):
    Assessment_Marks = forms.CharField(max_length=200, label="Assessment Marks")
