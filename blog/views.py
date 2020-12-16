from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Solution,Contacts
import random
from random import shuffle
from bs4 import BeautifulSoup
import urllib.request
import requests

# Create your views here.
def index(request):
    solution = Solution.objects.all()
    return render(request,'index.html',{'solution':solution,'title':'My Solutions For You Computer Science','meta':'This we is about solutions of programing problems of online judges and other CSE related subjects'})
def codeforces(request):
    solution = Solution.objects.all().filter(category='CODEFORCES')
    return render(request,'ojproblem.html',{'can':'codeforces','name':'Codeforces','solution':solution,'title':'Codeforces Online Judges problems Solutions','meta':'This we is about solutions of programing problems of online judge Codeforces. Codeforces solutions'})
def uri(request):
    solution = Solution.objects.all().filter(category='URI')
    return render(request,'ojproblem.html',{'can':'uri','name':'URI','solution':solution,'title':'URI Online Judges problems Solutions','meta':'This we is about solutions of programing problems of online judge URI. URI solutions'})
def uva(request):
    solution = Solution.objects.all().filter(category='UVA')
    return render(request,'ojproblem.html',{'can':'uva','name':'UVA','solution':solution,'title':'UVA Online Judges problems Solutions','meta':'This we is about solutions of programing problems of online judge UVA. UVA solutions'})
def hackerrank(request):
    solution = Solution.objects.all().filter(category='HACKERRANK')
    return render(request,'ojproblem.html',{'can':'hackerrank','name':'Hacker Rank','solution':solution,'title':'Hackerrak Online Judges problems Solutions','meta':'This we is about solutions of programing problems of online judge HackerRank. HackerRank solutions'})
def loj(request):
    solution = Solution.objects.all().filter(category='LIGHT Oj')
    return render(request,'ojproblem.html',{'can':'loj','name':'Light Oj','solution':solution,'title':'LightOj Online Judges problems Solutions','meta':'This we is about solutions of programing problems of online judge Light Oj. Light Oj solutions'})
def ojsolution(request):
    id=request.GET['id']
    solution = Solution.objects.all().filter(title=id)
    cat = solution[0].category
    solution_related = Solution.objects.order_by('?').all().filter(category=cat)[:3]
    link_text=solution[0].title.replace('solution','').replace('Solution','').replace('solutions','').replace('Solutions','').replace('sloution','')
    cat_text='ojsolution?id='+solution[0].title.replace(' ','%20')
    return render(request,'ojsolution.html',{'can':cat_text,'sol_rel':solution_related,'sol':solution,'link_text':link_text,'title':solution[0].title,'meta':solution[0].title+solution[0].explaination+solution[0].code})
def submitContact(request):
    name=request.POST['name']
    email=request.POST['email']
    phone=request.POST['phone']
    message=request.POST['message']

    contacts=Contacts(name=name,email=email,phone=phone,message=message)
    contacts.save()

    return redirect('/')




# def qa(request):
#     return render(request,'ojproblem.html',{'name':'Question + Answer'})
# def mathematics(request):
#     return render(request,'ojproblem.html',{'name':'Mathematics'})
# def c(request):
#     return render(request,'ojproblem.html',{'name':'C'})
# def cpp(request):
#     return render(request,'ojproblem.html',{'name':'C++'})
# def java(request):
#     return render(request,'ojproblem.html',{'name':'JAVA'})
# def python(request):
#     return render(request,'ojproblem.html',{'name':'PYTHON'})
# def kotlin(request):
#     return render(request,'ojproblem.html',{'name':'KOTLIN'})
# def html(request):
#     return render(request,'ojproblem.html',{'name':'HTML'})
# def css(request):
#     return render(request,'ojproblem.html',{'name':'CSS'})
# def js(request):
#     return render(request,'ojproblem.html',{'name':'JAVA SCRIPT'})
# def datastructure(request):
#     return render(request,'ojproblem.html',{'name':'Data Structure'})
# def algorithms(request):
#     return render(request,'ojproblem.html',{'name':'Algorithoms'})
# def database(request):
#     return render(request,'ojproblem.html',{'name':'Database'})
# def computerarchitecture(request):
#     return render(request,'ojproblem.html',{'name':'Computer Architecture'})
# def computernetwork(request):
#     return render(request,'ojproblem.html',{'name':'Computer Network'})
# def computergraphics(request):
#     return render(request,'ojproblem.html',{'name':'Computer Graphics'})
# def artificialintelligence(request):
#     return render(request,'ojproblem.html',{'name':'Artificial intelligence'})
# def operatingsystem(request):
#     return render(request,'ojproblem.html',{'name':'Operating System'})
# def compiler(request):
#     return render(request,'ojproblem.html',{'name':'Compiler'})

def wp(request):
    url = "https://www.espn.in/cricket/series/8048/game/1216520/kolkata-knight-riders-vs-kings-xi-punjab-46th-match-indian-premier-league-2020-21"
    response = requests.get(url,verify=False)
    soup = BeautifulSoup(response.text, "html.parser")

    detail = soup.find('div',attrs={'class':'cscore_info-overview'})
    team = soup.find_all('span',attrs={'class':'cscore_name cscore_name--long'})
    score = soup.find_all('div',attrs={'class':'cscore_score'})
    toss = soup.find('span',attrs={'class':'cscore_notes_game'})
    crr = soup.find('p',attrs={'data-reactid':'45'})

    x1 = soup.find_all('span',attrs={'class':'over-score'})

    overdata = soup.find('div',attrs={'class':'recent-overs-wrapper'})
    mystring = str(overdata.text)
    overdata = ' '.join(mystring.split())
    overdata = overdata.replace("Recent","")
    ballbyball = []
    overdata=overdata+"     "
    for x in range(len(overdata)):
        if overdata[x]=='.':
            ballbyball.append(overdata[x])
        elif overdata[x]=='|':
            ballbyball.append(overdata[x])
        elif overdata[x]=='W':
            ballbyball.append(overdata[x])
        elif overdata[x]=='1' and overdata[x+1]=='w':
            ballbyball.append(overdata[x:x+1])
        elif overdata[x]=='2' and overdata[x+1]=='w':
            ballbyball.append(overdata[x:x+1])
        elif overdata[x]=='3' and overdata[x+1]=='w':
            ballbyball.append(overdata[x:x+1])
        elif overdata[x]=='1' and overdata[x+1:x+2]=='lb':
            ballbyball.append(overdata[x:x+2])
        elif overdata[x]=='2' and overdata[x+1:x+2]=='lb':
            ballbyball.append(overdata[x:x+2])
        elif overdata[x]=='3' and overdata[x+1:x+2]=='lb':
            ballbyball.append(overdata[x:x+2])
        elif overdata[x]=='1' and overdata[x+1]=='b':
            ballbyball.append(overdata[x:x+1])
        elif overdata[x]=='2' and overdata[x+1]=='b':
            ballbyball.append(overdata[x:x+1])
        elif overdata[x]=='3' and overdata[x+1]=='b':
            ballbyball.append(overdata[x:x+1])
        elif overdata[x]=='4' and overdata[x+1]=='b':
            ballbyball.append(overdata[x:x+1])
        elif overdata[x]=='1' and overdata[x+1:x+2]=='nb':
            ballbyball.append(overdata[x:x+2])
        elif overdata[x]=='2' and overdata[x+1:x+2]=='nb':
            ballbyball.append(overdata[x:x+2])
        elif overdata[x]=='3' and overdata[x+1:x+2]=='nb':
            ballbyball.append(overdata[x:x+2])
        elif overdata[x]=='4' and overdata[x+1:x+2]=='nb':
            ballbyball.append(overdata[x:x+2])
        elif overdata[x]=='6' and overdata[x+1:x+2]=='nb':
            ballbyball.append(overdata[x:x+2])
        elif overdata[x]=='1':
            ballbyball.append(overdata[x])
        elif overdata[x]=='2':
            ballbyball.append(overdata[x])
        elif overdata[x]=='3':
            ballbyball.append(overdata[x])
        elif overdata[x]=='4':
            ballbyball.append(overdata[x])
        elif overdata[x]=='6':
            ballbyball.append(overdata[x])

    try:
        mystring = str(x1[0].text)
        x1 = ' '.join(mystring.split())
    except IndexError:
        x1=""
    mystring = str(toss.text)
    toss = ' '.join(mystring.split())
    # mystring = str(crr.text)
    # crr = ' '.join(mystring.split())
    mystring = str(detail.text)
    match = ' '.join(mystring.split())
    mystring = str(team[0].text)
    team1 = ' '.join(mystring.split())
    mystring = str(team[1].text)
    team2 = ' '.join(mystring.split())
    mystring = str(score[0].text)
    score1 = ' '.join(mystring.split())
    mystring = str(score[1].text)
    score2 = ' '.join(mystring.split())

    tbody = soup.find_all('tbody')

    tr_bat = tbody[0].find_all('tr')
    td_bat1 = tr_bat[0].find_all('td')
    b1 = td_bat1[0].find('a')
    mystring = str(b1.text)
    b1 = ' '.join(mystring.split())
    mystring = str(td_bat1[1].text)
    run1 = ' '.join(mystring.split())
    mystring = str(td_bat1[2].text)
    bf1 = ' '.join(mystring.split())
    mystring = str(td_bat1[3].text)
    h41 = ' '.join(mystring.split())
    mystring = str(td_bat1[4].text)
    h61 = ' '.join(mystring.split())
    mystring = str(td_bat1[5].text)
    sr1 = ' '.join(mystring.split())
    b2=""
    run2=""
    bf2=""
    h42=""
    h62=""
    sr2=""
    bo2=""
    ov2=""
    m2=""
    r2=""
    w2=""
    eco2=""
    if 'W' not in x1:
        try:
            td_bat2 = tr_bat[1].find_all('td')
            b2 = td_bat2[0].find('a')
            mystring = str(b2.text)
            b2 = ' '.join(mystring.split())
            mystring = str(td_bat2[1].text)
            run2 = ' '.join(mystring.split())
            mystring = str(td_bat2[2].text)
            bf2 = ' '.join(mystring.split())
            mystring = str(td_bat2[3].text)
            h42 = ' '.join(mystring.split())
            mystring = str(td_bat2[4].text)
            h62 = ' '.join(mystring.split())
            mystring = str(td_bat2[5].text)
            sr2 = ' '.join(mystring.split())
        except IndexError:
            b2=""
            run2=""
            bf2=""
            h42=""
            h62=""
            sr2=""


    tr_bowl = tbody[1].find_all('tr')
    td_bowl1 = tr_bowl[0].find_all('td')
    bo1 = td_bowl1[0].find('a')
    mystring = str(bo1.text)
    bo1 = ' '.join(mystring.split())
    mystring = str(td_bowl1[1].text)
    ov1 = ' '.join(mystring.split())
    mystring = str(td_bowl1[2].text)
    m1 = ' '.join(mystring.split())
    mystring = str(td_bowl1[3].text)
    r1 = ' '.join(mystring.split())
    mystring = str(td_bowl1[4].text)
    w1 = ' '.join(mystring.split())
    mystring = str(td_bowl1[5].text)
    eco1 = ' '.join(mystring.split())
    if '0.' or '1.0' not in score2:
        try:
            tr_bowl = tbody[1].find_all('tr')
            td_bowl2 = tr_bowl[1].find_all('td')
            bo2 = td_bowl2[0].find('a')
            mystring = str(bo2.text)
            bo2 = ' '.join(mystring.split())
            mystring = str(td_bowl2[1].text)
            ov2 = ' '.join(mystring.split())
            mystring = str(td_bowl2[2].text)
            m2 = ' '.join(mystring.split())
            mystring = str(td_bowl2[3].text)
            r2 = ' '.join(mystring.split())
            mystring = str(td_bowl2[4].text)
            w2 = ' '.join(mystring.split())
            mystring = str(td_bowl2[5].text)
            eco2 = ' '.join(mystring.split())
        except IndexError:
            bo2=""
            ov2=""
            m2=""
            r2=""
            eco2=""
            w2=""



    return render(request,'world_population.html',{'ballbyball':ballbyball,'toss':toss,'match_detail':match,"team1": team1,"team2":team2,"score1": score1,"score2":score2,'b1':b1,'run1':run1,'bf1':bf1,'h41':h41,'h61':h61,'sr1':sr1,'b2':b2,'run2':run2,'bf2':bf2,'h42':h42,'h62':h62,'sr2':sr2,'bo1':bo1,'ov1':ov1,'r1':r1,'m1':m1,'w1':w1,'eco1':eco1,'bo2':bo2,'ov2':ov2,'r2':r2,'m2':m2,'w2':w2,'eco2':eco2,'x1':x1})
    #return render(request,'world_population.html')

    
def liu(request):
    return render(request,'live_internet_user.html')
