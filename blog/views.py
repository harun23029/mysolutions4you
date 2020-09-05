from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
def home(request):
    return render(request,'index.html')
def codeforces(request):
    return render(request,'ojproblem.html',{'name':'Codeforces'})
def uri(request):
    return render(request,'ojproblem.html',{'name':'URI'})
def uva(request):
    return render(request,'ojproblem.html',{'name':'UVA'})
def hackerrank(request):
    return render(request,'ojproblem.html',{'name':'Hacker Rank'})
def loj(request):
    return render(request,'ojproblem.html',{'name':'Light Oj'})
def qa(request):
    return render(request,'ojproblem.html',{'name':'Question + Answer'})
def mathematics(request):
    return render(request,'ojproblem.html',{'name':'Mathematics'})

