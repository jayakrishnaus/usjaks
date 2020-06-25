from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Post, questions, answers
from explorer.forms import QuestionForm, AnswerForm, PostForm

from django.shortcuts import get_object_or_404

# Create your views here.
def explorer(request):
    dests = Post.objects.all()
    categories={}
    categories = {dest.Subject for dest in dests}
    return render(request,'explorer.html',{'dests': dests,'categories':categories})


def data_pages(request, name):
    dests = Post.objects.all()
    categories={}
    categories = {dest.Subject for dest in dests}
    
    return render(request,'data_pages.html',{'name': name,'dests': dests,'categories':categories})

def answerpages(request, name):
    dests = answers.objects.all()
    categories={}
    categories = {dest.Subject for dest in dests}
    
    return render(request,'answer_pages.html',{'name': name,'dests': dests,'categories':categories})



def solved(request):
    dests = answers.objects.all()
    categories={}
    categories = {dest.Subject for dest in dests}
    return render(request,'solved.html',{'dests': dests,'categories':categories})




def redy(request):
   dests = questions.objects.all()
   return render(request,'unansweredquestions.html',{'dests': dests})




def Posts(request):
    if request.method =="POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post_item = form.save(commit=False)
            post_item.save()
            return redirect('/')
    else:
        form = PostForm()
    return render(request, 'ideas.html',{'form': form})




def thequestions(request):
    if request.method =="POST":
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            post_item = form.save(commit=False)
            post_item.save()
            return redirect('/')
    else:
        form = QuestionForm()
    return render(request, 'questions.html',{'form': form})


def edit_post(request, post_id=None):
    item = get_object_or_404(Post, id=post_id)
    form = PostForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'blog/post_form.html', {'form': form})


def theanswers(request, name):
    dests = questions.objects.all()
    answer = answers.objects.all()
    initial_data={
        'Subject': name
    }
    if request.method =="POST":
        form = AnswerForm(request.POST, request.FILES, initial=initial_data)
        form.fields["Subject"].queryset = name
        if form.is_valid():
            form.fields["Subject"].queryset = name
            post_item = form.save(commit=False)
            post_item.save()
            return redirect('/')
    else:
        form = AnswerForm(initial=initial_data)
    return render(request,'answering.html',{'name': name,'dests': dests, 'answer': answer, 'form': form})
