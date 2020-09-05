from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('codeforces',views.codeforces,name='codeforces'),
    path('uri',views.uri,name='uri'),
    path('uva',views.uva,name='uva'),
    path('hackerrank',views.hackerrank,name='hackerrank'),
    path('loj',views.loj,name='loj'),
    path('qa',views.qa,name='qa'),
    path('mathematics',views.mathematics,name='mathematics'),
    path('ojsolution',views.ojsolution,name='ojsolution'),

]