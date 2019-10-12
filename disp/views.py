from django.shortcuts import render

# Create your views here.
# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Context, Template
from .forms import loginForm, requet, result
 
import cx_Oracle
 
        


def connection_db2(request,name,password):
           l = []
     
           db1 = cx_Oracle.connect(name, password, 'localhost:1521/orcl')
     
           try:
            dsn_tns = cx_Oracle.makedsn('localhost', 1521, 'orcl')
            cursor = db1.cursor()
           
            cursor.execute('selecht * form DEPARTMENTS')
            for row in cursor:
             print (row[0]) 
             l.append(row[0])
             return l
           except mysql.connector.Error as err:
             print('erroo',err) 
 
def connection_db(request,name,password):
    v= 0 
    try:
        db1 = cx_Oracle.connect(name, password, 'localhost:1521/orcl')
    except :
        v = 1 
        pass

        print('hii')
        #return redirect('disp:errorpage')
    #db1 = cx_Oracle.connect('hr/123456789@localhost:1521/orcl')
    l = []
    ll = []
    cl = []
    cll = []
    clll = []
    cllll = []
    clllll = []
 

    if not v:
        dsn_tns = cx_Oracle.makedsn('localhost', 1521, 'orcl')
        cursor = db1.cursor()
    
        cursor.execute('select table_name from user_tables')
        for row in cursor:
            print (row[0]) 
            l.append(row[0])

    
    
            c = db1.cursor()
            c.execute('select * from {0}'.format(row[0]))
            col_names = [row[0] for row in c.description]
            ll.append(col_names)
            print(col_names)

        c1 = db1.cursor()
        c1.execute('select view_name from user_views')
        for ro in c1:
         print (ro) 
         cl.append(ro[0])

        cll = db1.cursor()
        cll.execute('SELECT INDEX_NAME FROM USER_INDEXES')
         
        clll = db1.cursor()
        clll.execute('SELECT SEQUENCE_NAME FROM USER_SEQUENCES')
        cllll = db1.cursor()
        cllll.execute('SELECT PROCEDURE_NAME FROM USER_PROCEDURES')
        clllll = db1.cursor()
        clllll.execute('SELECT TRIGGER_NAME FROM USER_TRIGGERS')


  
    return l,ll,v,cl,cll,clll,cllll,clllll
 


    
    

def index(request, name, password):
    l = []
    tables, colunms, v, views, index, seq, tig, proc= connection_db(request,name, password)
    #return HttpResponse(tables)
    if v:
        return render(request, 'error.html')
      

    if request.method == "POST":
        form = requet(request.POST)
        if form.is_valid():
         reqeutsql = form.cleaned_data['req']
         print('data', reqeutsql)

         db1 = cx_Oracle.connect(name, password, 'localhost:1521/orcl')   
         dsn_tns = cx_Oracle.makedsn('localhost', 1521, 'orcl')
         cursor = db1.cursor()
        try:
         cursor.execute(reqeutsql)
         for row in cursor:
          l.append(row)
        except :
          l.append('vérifier votre requête')
        

    req = requet()
     
       

    return render(request, 'indexu.html' , {'tig' : tig, 'proc' : proc, 'seq' : seq, 'index' : index, 'tables' : tables, 'colunms' : colunms, 'req' : req, 'l' : l, 'views' : views})

 

def loginpage(request):
    if request.method == "POST":
        form = loginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            print('data', name , password)
            return redirect ('disp:index', name = name, password = password)
    else:
        form = loginForm()
    
    return render(request,'login.html',{'form' : form })


def errorpage(request):
    return render(request, 'error.html')



 
