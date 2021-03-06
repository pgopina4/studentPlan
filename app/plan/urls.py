from django.conf.urls import url
from . import views
 
app_name = 'plan'
 
urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^make_plan$', views.make_plan, name='make_plan'),
    url(r'^show7thGrade$', views.show7thGrade, name='show7thGrade'),
    url(r'^show8thGrade$', views.show8thGrade, name='show8thGrade'),
    url(r'^show9thGrade$', views.show9thGrade, name='show9thGrade'),
    url(r'^show7thTeacher$', views.show7thTeacher, name='show7thTeacher'),
    url(r'^show8thTeacher$', views.show8thTeacher, name='show8thTeacher'),
    url(r'^show9thTeacher$', views.show9thTeacher, name='show9thTeacher'),
    url(r'^showdataSpecific$', views.showdataSpecific, name='showdataSpecific'),
    url(r'^showdataSpecificSimple$', views.showdataSpecificSimple, name='showdataSpecificSimple'),
    url(r'^showdataSpecificMarks$', views.showdataSpecificMarks, name='showdataSpecificMarks'),
    url(r'^showdata$', views.showdata, name='showdata'),
    url(r'^makedailyupdate$', views.makedailyupdate, name='makedailyupdate'),
    url(r'^showdailyupdate$', views.showdailyupdate, name='showdailyupdate'),
    url(r'^makeweeklyupdate$', views.makeweeklyupdate, name='makeweeklyupdate'),
    url(r'^checkProgress$', views.CheckProgress, name='CheckProgress'),
    #url(r'^showweeklyupdate$', views.showweeklyupdate, name='showweeklyupdate'), ]
    url(r'^Progress$', views.Progress, name='Progress'), ]
