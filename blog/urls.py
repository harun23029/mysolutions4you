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
    path('c',views.c,name='c'),
    path('cpp',views.cpp,name='cpp'),
    path('java',views.java,name='java'),
    path('kotlin',views.kotlin,name='kotlin'),
    path('python',views.python,name='python'),
    path('html',views.html,name='html'),
    path('css',views.css,name='css'),
    path('js',views.js,name='js'),
    path('datastructure',views.datastructure,name='datastructure'),
    path('algorithms',views.algorithms,name='algorithms'),
    path('database',views.database,name='database'),
    path('computerarchitecture',views.computerarchitecture,name='computerarchitecture'),
    path('computernetwork',views.computernetwork,name='computernetwork'),
    path('computergraphics',views.computergraphics,name='computergraphics'),
    path('artificialintelligence',views.artificialintelligence,name='artificialintelligence'),
    path('operatingsystem',views.operatingsystem,name='operatingsystem'),
     path('compiler',views.compiler,name='compiler'),

]