from django.shortcuts import render
from django.http import HttpResponse
from .models import Solution

# Create your views here.
def index(request):
    return render(request,'index.html',{'title':'My Solutions For You Computer Science','meta':'This we is about solutions of programing problems of online judges and other CSE related subjects'})
def home(request):
    return render(request,'index.html',{'title':'My Solutions For You Computer Science','meta':'This we is about solutions of programing problems of online judges and other CSE related subjects'})
def codeforces(request):
    solution = Solution.objects.all().filter(category='CODEFORCES')
    return render(request,'ojproblem.html',{'name':'Codeforces','solution':solution,'title':'Codeforces Online Judges problems Solutions','meta':'This we is about solutions of programing problems of online judge Codeforces. Codeforces solutions'})
def uri(request):
    solution = Solution.objects.all().filter(category='URI')
    return render(request,'ojproblem.html',{'name':'URI','solution':solution,'title':'URI Online Judges problems Solutions','meta':'This we is about solutions of programing problems of online judge URI. URI solutions'})
def uva(request):
    solution = Solution.objects.all().filter(category='UVA')
    return render(request,'ojproblem.html',{'name':'UVA','solution':solution,'title':'UVA Online Judges problems Solutions','meta':'This we is about solutions of programing problems of online judge UVA. UVA solutions'})
def hackerrank(request):
    solution = Solution.objects.all().filter(category='HACKERRANK')
    return render(request,'ojproblem.html',{'name':'Hacker Rank','solution':solution,'title':'Hackerrak Online Judges problems Solutions','meta':'This we is about solutions of programing problems of online judge HackerRank. HackerRank solutions'})
def loj(request):
    solution = Solution.objects.all().filter(category='LIGHT Oj')
    return render(request,'ojproblem.html',{'name':'Light Oj','solution':solution,'title':'LightOj Online Judges problems Solutions','meta':'This we is about solutions of programing problems of online judge Light Oj. Light Oj solutions'})
def qa(request):
    return render(request,'ojproblem.html',{'name':'Question + Answer'})
def mathematics(request):
    return render(request,'ojproblem.html',{'name':'Mathematics'})
def ojsolution(request):
    id=request.GET['id']
    solution = Solution.objects.all().filter(title=id)
    return render(request,'ojsolution.html',{'sol':solution,'title':solution[0].title,'meta':solution[0].title+solution[0].explaination+solution[0].code})

