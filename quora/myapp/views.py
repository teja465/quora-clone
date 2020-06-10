from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
# Create your views here.
def index_view(request):
    questions=questions_model.objects.all()
    return render(request,'home.html',{'questions':questions})
    print(request.user.id,'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
def question_detail_view(request,id):
    question=questions_model.objects.get(id=id)
    answers=question.answers.all()
    return render(request,'questionDetail.html',{'question':question,'answers':answers})
def Ask_question(request):
    form=question_form()
    if request.method=='POST':
        qn=request.POST.get('question', None)
        user=User.objects.get(id=request.user.id)
        an=questions_model.objects.create(question=qn,author=user)
        an.save()
        return HttpResponseRedirect('/')
    return render(request,'ask.html',{'form':form})

def answer_view(request,id):


    form=answer_form()

    if request.method=='POST':
        ans=request.POST.get('answer', None)
        qu=questions_model.objects.get(id=id)
        a=answers_model.objects.create(answer=ans,question=qu)
        a.save()
        return HttpResponseRedirect('/')
    return render(request,'answer.html',{'form':form})
#  bio email college  profession
def user_profile(request,id):
    user=User.objects.get(id=id)
    bio=user.profile.bio
    bio=user.profile.bio
    email=user.profile.email
    college=user.profile.college
    profession=user.profile.profession
    return render(request,'profile.html',{'name':user.username,'bio':bio,'email':email,'college':college,'profession':profession})



def dbprint():

    te=User.objects.get(id=1)
    print('dbprintaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    print(te.username,te.profile.bio)
dbprint()
