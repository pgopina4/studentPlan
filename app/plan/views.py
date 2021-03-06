from django.shortcuts import render
from datetime import datetime, timedelta
from django.utils import timezone
from plan.forms import PostForm
from plan.models import Post1
from plan.models import allstudent
from plan.models import Update
from plan.forms import UpdateForm
from plan.models import Update1
from plan.forms import Update1Form
from plan.models import Progress as Prog
from plan.forms import ProgressForm
from plan.Output import *
import json
import re

#the function executes with the make_plan url to take the inputs 
def make_plan(request):
    if request.method == 'POST':  # if the form has been filled
        form = PostForm(request.POST)
        Standard = request.POST.get('standard', '')
        Name = request.POST.get('name', '')
        Chapter = request.POST.get('chapter', '')
        Goal_old1 = request.POST.getlist('goal1', '')
        Goal_old1 = "\n".join(Goal_old1)
        Goal_old2 = request.POST.get('goal2', '')
        Goal_now1 = request.POST.getlist('goal3', '')
        Goal_now1 = "\n".join(Goal_now1)
        Goal_now2 = request.POST.get('goal4', '') 
        Goal_now3 = request.POST.get('goal5', '') 
        Goal_now4 = request.POST.get('goal6', '') 
        if Standard=='' or Name =='' or Chapter=='':
            user_obj = Post1( Standard='Grade 7th', 
                    Name='',
                    Chapter='',
                    Goal_old1='',
                    Goal_old2='', Goal_now1='',
                    Goal_now2='', Goal_now3='',
                    Goal_now4='')
                    #date='')
            return render(request, 'plan/make_plan.html', {'user_obj': user_obj,'is_registered':False }) # Redirect after POST
        else:
            user_obj = Post1( Standard=Standard, 
                    Name=Name,
                    Chapter=Chapter,
                    Goal_old1=Goal_old1,
                    Goal_old2=Goal_old2,Goal_now1=Goal_now1,
                    Goal_now2=Goal_now2,Goal_now3=Goal_now3,
                    Goal_now4=Goal_now4) # date=date)
            # saving all the data in the current object into the database
            user_obj.save()
         
            return render(request, 'plan/make_plan.html', {'user_obj': user_obj,'is_registered':True }) # Redirect after POST
    else:
        # form = PostForm()  # an unboundform
        form = {}
        return render(request, 'plan/make_plan.html', {'form': form})
 
#the function executes with the showdata url to display the list of registered users
#def showdataSpecific(request):
 #   standard = request.GET.get('Standard')
  #  name = request.GET.get('Name')
#    all_plan = Post1.objects.filter(Standard=standard,Name=name)
 #   return render(request, 'plan/showdataSpecific.html', {'all_plan': all_plan, })

#  Displays chapters and associated outcomes of the student in their make_plan, daily update and weekly update view
def showdataSpecific(request):
    standard = request.GET.get('Standard')
    name = request.GET.get('Name')
    N = 7
    date_N_days_ago = datetime.now() - timedelta(days=N)
    all_plan = Post1.objects.filter(created_date__range=[date_N_days_ago, datetime.now()], Standard=standard,Name=name)
    return render(request, 'plan/showdataSpecific.html', {'all_plan': all_plan})

#  Displays chapters and associated outcomes of the student in the past 12 days in the Progress Template so that teachers can evaluate it
def showdataSpecificMarks(request):
    standard = request.GET.get('Standard')
    name = request.GET.get('Name')
    N = 12
    date_N_days_ago = datetime.now() - timedelta(days=N)
    all_plan = Post1.objects.filter(created_date__range=[date_N_days_ago, datetime.now()], Standard=standard,Name=name)
    goals=[]
    for i in all_plan:
        goals.append(i.Goal_old1.split('\n'))
        goals.append(i.Goal_now1.split('\n'))
    global goals_num
    goals_num=0
    for i in range(len(goals)):
        if(goals[i] != ['']):
            goals_num+=len(goals[i])
    return render(request, 'plan/showdataSpecificMarks.html', {'all_plan': all_plan, 'goals_num': goals_num})

# To enable storing the outcomes in the required format in the database
def showdataSpecificSimple(request):
    standard = request.GET.get('Standard')
    name = request.GET.get('Name')
    N = 12
    date_N_days_ago = datetime.now() - timedelta(days=N)
    all_plan = Post1.objects.filter(created_date__range=[date_N_days_ago, datetime.now()], Standard=standard,Name=name)
    return render(request, 'plan/showdataSpecificSimple.html', {'all_plan': all_plan, })

def showdata(request):
    all_plan = Post1.objects.all()
    return render(request, 'plan/showdata.html', {'all_plan': all_plan, })

# For printing out goals for each child at the start of the week
def show7thGrade(request):
    students_of_a_grade = allstudent.objects.filter(Standard="7th")
    N =7
    date_N_days_ago = datetime.now() - timedelta(days=N)
    all_plan = Post1.objects.filter(created_date__range=[date_N_days_ago, datetime.now()], Standard="7th")
    return render(request, 'plan/showdata.html', {'all_plan': all_plan, 'students_of_a_grade':students_of_a_grade})

def show8thGrade(request):
    students_of_a_grade = allstudent.objects.filter(Standard="8th")
    N =7
    date_N_days_ago = datetime.now() - timedelta(days=N)
    all_plan = Post1.objects.filter(created_date__range=[date_N_days_ago, datetime.now()], Standard="8th")
    return render(request, 'plan/showdata.html', {'all_plan': all_plan, 'students_of_a_grade':students_of_a_grade})

def show9thGrade(request):
    students_of_a_grade = allstudent.objects.filter(Standard="9th")
    N =7
    date_N_days_ago = datetime.now() - timedelta(days=N)
    all_plan = Post1.objects.filter(created_date__range=[date_N_days_ago, datetime.now()], Standard="9th")
    return render(request, 'plan/showdata.html', {'all_plan': all_plan, 'students_of_a_grade':students_of_a_grade})

# For printing out goals for each child to be sent to the teacher so that they are able to evaluate the assessments accordingly
def show7thTeacher(request):
    students_of_a_grade = allstudent.objects.filter(Standard="7th")
    N = 12
    date_N_days_ago = datetime.now() - timedelta(days=N)
    all_plan = Post1.objects.filter(created_date__range=[date_N_days_ago, datetime.now()], Standard="7th")
    return render(request, 'plan/showdataTeacher.html', {'all_plan': all_plan, 'students_of_a_grade':students_of_a_grade})

def show8thTeacher(request):
    students_of_a_grade = allstudent.objects.filter(Standard="8th")
    N = 12
    date_N_days_ago = datetime.now() - timedelta(days=N)
    all_plan = Post1.objects.filter(created_date__range=[date_N_days_ago, datetime.now()], Standard="8th")
    return render(request, 'plan/showdataTeacher.html', {'all_plan': all_plan, 'students_of_a_grade':students_of_a_grade})

def show9thTeacher(request):
    students_of_a_grade = allstudent.objects.filter(Standard="9th")
    N = 12
    date_N_days_ago = datetime.now() - timedelta(days=N)
    all_plan = Post1.objects.filter(created_date__range=[date_N_days_ago, datetime.now()], Standard="9th")
    return render(request, 'plan/showdataTeacher.html', {'all_plan': all_plan, 'students_of_a_grade':students_of_a_grade})

def showdailyupdate(request):
    all_Update = Update.objects.all()
    return render(request, 'plan/showdailyupdate.html', {'all_Update': all_Update, })

def index(request):
    all_Update = Update.objects.all()
    return render(request, 'plan/index.html', {'all_Update': all_Update,})

#def allstudent(request):
    #all_Update = Update.objects.all()
    #return render(request, 'plan/allstudent.html', {'all_Update': all_Update,})



def makedailyupdate(request):
    if request.method == 'POST':  # if the form has been filled
        form = UpdateForm(request.POST)
        Standard = request.POST.get('standard', '')
        Name = request.POST.get('name', '')
        What_did_I_do_at_home = request.POST.get('What_did_I_do_at_home', '')
        What_I_did_towards_my_goals = request.POST.get('What_I_did_towards_my_goals', '')
        What_did_I_learn_new = request.POST.get('What_did_I_learn_new', '')
           
#        date = request.POST.get('date', '')
        if What_I_did_towards_my_goals =='' or Standard =='' or Name =='' or What_did_I_learn_new =='':
           user_obj = Update( Standard ='', Name ='', What_did_I_do_at_home='', What_I_did_towards_my_goals='', What_did_I_learn_new='')
               
           return render(request, 'plan/makedailyupdate.html', {'user_obj': user_obj,'is_registered':False }) # Redirect after POST
        else:
            user_obj = Update( Standard = Standard, Name =Name, What_did_I_do_at_home = What_did_I_do_at_home, What_I_did_towards_my_goals =  What_I_did_towards_my_goals, What_did_I_learn_new=What_did_I_learn_new )
                    
            # saving all the data in the current object into the database
            user_obj.save()
         
            return render(request, 'plan/makedailyupdate.html', {'user_obj': user_obj,'is_registered':True }) # Redirect after POST
    else:
        form = UpdateForm()  # an unboundform
        #form = {}
        return render(request, 'plan/makedailyupdate.html', {'form': form})



def makeweeklyupdate(request):
    if request.method == 'POST':  # if the form has been filled
        form = Update1Form(request.POST)
        Standard = request.POST.get('standard', '')
        Name = request.POST.get('name', '')
        goalcompleted = request.POST.get('goal', '')
        How_do_I_feel_after_my_assessment = request.POST.get('How_do_I_feel_after_my_assessment', '')
        What_I_will_do_different_next_week = request.POST.get('What_I_will_do_different_next_week', '')
    
#        date = request.POST.get('date', '')
        if How_do_I_feel_after_my_assessment =='' or What_I_will_do_different_next_week =='' or Standard =='' or Name =='':
           user_obj = Update1( Standard ='', Name ='', How_do_I_feel_after_my_assessment='', What_I_will_do_different_next_week='', goalcompleted='')
               
           return render(request, 'plan/makeweeklyupdate.html', {'user_obj': user_obj,'is_registered':False }) # Redirect after POST
        else:
            user_obj = Update1( Standard = Standard, Name =Name, How_do_I_feel_after_my_assessment = How_do_I_feel_after_my_assessment, What_I_will_do_different_next_week =  What_I_will_do_different_next_week, goalcompleted=goalcompleted)
                    
            # saving all the data in the current object into the database
            user_obj.save()
         
            return render(request, 'plan/makeweeklyupdate.html', {'user_obj': user_obj,'is_registered':True }) # Redirect after POST
    else:
        form = Update1Form()  # an unboundform
        #form = {}
        return render(request, 'plan/makeweeklyupdate.html', {'form': form})

def Progress(request):
    if request.method == 'POST':  # if the form has been filled
        form = ProgressForm(request.POST)
        Standard = request.POST.get('standard', '')
        Name = request.POST.get('name', '')
        Assessment_Marks = request.POST.get('Assessment_Marks', '')
        Marks_num = Assessment_Marks.count(",")+1 
        Outcomes = request.POST.get('Outcomes', '')

        if Marks_num != goals_num:
           # if the number of marks entered does not match with the number of goals, then: 
           return render(request, 'plan/Progress.html', {'is_wrong_data':True }) # Redirect after POST
        elif Assessment_Marks =='' or Standard =='' or Name =='':
           user_obj = Prog( Standard ='', Name ='', Assessment_Marks='')
           return render(request, 'plan/Progress.html', {'user_obj': user_obj,'is_registered':False }) # Redirect after POST
        else:
            user_obj = Prog( Standard = Standard, Name = Name, Assessment_Marks= Assessment_Marks, Outcomes = Outcomes)
            # saving all the data in the current object into the database
            user_obj.save()
            return render(request, 'plan/Progress.html', {'user_obj': user_obj,'is_registered':True }) # Redirect after POST
    else:
        form = ProgressForm()  # an unboundform
        return render(request, 'plan/Progress.html', {'form': form})


def CheckProgress(request):
    Standard = request.GET.get('Standard')
    Name = request.GET.get('Name')
    if Standard is None or Name is None:
        return render(request, 'plan/checkProgress.html', {'unique_list': ' ','json_object':''})
    else:
        #dummy Python object that needs to be converted to json
        # dictexample = {'children':[{'children':[{'children':[],'data':{'description':'algebra l.o.1','$angularWidth':1000,'$color':'#B0AAF6','size':200},'id':'Source/Algebra/Classify Poly', 'name':'Classify Poly'},{'children':[],'data':{'description':'algebra l.o.2','$angularWidth':1000,'days':3,'$color':'#B0AAF6','size':200},'id':'Source/Algebra/Factoriz * Poly','name':'Factorize * Poly'}],'data':{'description':'algebra chapter','$color':'#dd3333','days':2,'$angularWidth':700,'size':2000},'id':'Source/Algebra','name':'Algebra'},{'children':[{'children':[],'data':{'description':'Stat l.o.1','$angularWidth':1000,'days':3,'$color':'#B0AAF6','size':200},'id':'Source/Statistics/Stat Graphs', 'name':'Stat. Graphs'}],'data':{'description':'Statistics chapter','$color':'#dd3333','days':2,'$angularWidth':700,'size':2000},'id':'Source/Statistics','name':'Statistics'}],'data':{'$type':'none'},'id':'Source','name':'Grade 9 Math'}
        
        #Build the cumulative list of learning outcomes fo students from start of term - Data comes from Progress table and has marks alloted by the teacher as well
        start_date = datetime(2017, 10, 16)
        cumulative_progress = Prog.objects.filter(created_date__range=[start_date, datetime.now()], Standard=Standard,Name=Name)
        cumulative_list=[]
        for iterator in cumulative_progress:
            progress_string = iterator.Outcomes
            Assessment_Marks_list = iterator.Assessment_Marks.split(',')
            progress_string = re.sub(r'\r','',progress_string)
            progress_list=progress_string.split("],")[:-1]
            k=0
            for each in progress_list:
                temp=each.split(';;',1)
                chapter=re.sub('^\s+','',temp[0])
                outcomes=temp[1].split('\n')
                for i in range(len(outcomes)):
                    cumulative_list.append([chapter,outcomes[i],Assessment_Marks_list[k]])
                    k+=1

        # print(cumulative_list)
        #Reverse the cumulative list so as to get the latest scores for any given learning outcome. 
        cumulative_list.reverse()
        
        # Get the appropriate goals corresponding to the standards from variables in output.py -- next line
        standard_data = {"7th":data_7th,"8th":data_8th,"9th":data_9th}
        sunburst_obj=standard_data[Standard]
        chapter_color_toggle=0
        learn_outcome_dict=[]
        chapter_dict = []

        # Build the sunburst JSON object for goals first, then chapters, and then append into a final_dict
        for i in (range(len(sunburst_obj))):
            learn_outcome_dict=[]
            TotalGrade=0
            for j in (range(len(sunburst_obj[i][1]))):
                Grade = CheckLearningOutcome_inCumulativelist(sunburst_obj[i][0],sunburst_obj[i][1][j][0],cumulative_list)
                if Grade>=0:
                    # To enable appropriate coloring for goals based on their associated grades from progress table
                    Grade_color="#a0"+hex(int(127 + (128/10*Grade))).split('x',1)[1]+"00"
                    TotalGrade+=Grade
                    learn_outcome_dict.append({'children':[],'data':{'description':sunburst_obj[i][1][j][0],'$angularWidth':1000,'$color': Grade_color,'size': Grade},'id':'Source/'+sunburst_obj[i][0]+'/'+sunburst_obj[i][1][j][1],'name':sunburst_obj[i][1][j][1]})
                else:
                    learn_outcome_dict.append({'children':[],'data':{'description':sunburst_obj[i][1][j][0],'$angularWidth':1000,'$color':'#CDD4D3','size': 0},'id':'Source/'+sunburst_obj[i][0]+'/'+sunburst_obj[i][1][j][1],'name':sunburst_obj[i][1][j][1]})
            # To enable alternate chapters to be colored appropriately. 
            if chapter_color_toggle == 1:
                chapter_dict.append({'children':learn_outcome_dict,'data':{'description':sunburst_obj[i][0]+' Chapter','$angularWidth':1000,'$color':'#6699ff'},'id':'Source/'+sunburst_obj[i][0],'name':sunburst_obj[i][0]})
                chapter_color_toggle=0
            else:
                chapter_dict.append({'children':learn_outcome_dict,'data':{'description':sunburst_obj[i][0]+' Chapter','$angularWidth':1000,'$color':'#ff99aa'},'id':'Source/'+sunburst_obj[i][0],'name':sunburst_obj[i][0]})
                chapter_color_toggle=1
        #encapsulating the above dictionary into a final dictionary
        final_dict={'children':chapter_dict,'data':{'$type':'none'},'id':'Source','name': Name + ' - Standard ' +  Standard}
        #Convert dictionary to JSON Object
        dictionarytoJson = json.dumps(final_dict)
        return render(request, 'plan/checkProgress.html', {'json_object':dictionarytoJson})


def CheckLearningOutcome_inCumulativelist(chapter,lo,unique_list):
    for i in (range(len(unique_list))):
        if unique_list[i][0] == chapter:
            if re.sub('^\s+','',unique_list[i][1]) == lo:
                return int(unique_list[i][2])
                break
    return -1  
