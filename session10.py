from typing import List
import time
import sys
import weakref
import random
from time import perf_counter
import statistics
from statistics import mode
from statistics import mean
import datetime
from datetime import date
from faker import Faker
from decimal import Decimal
from collections import namedtuple


def dict_approach_for_solution():
    
    start=perf_counter()
    fake = Faker()
    total=0
    z=[]
    dob=[]
    lat=[]
    lon=[]
    q=[]
    for i in range(0,10000):
        q.append(fake.profile())
    for i in q:
        z.append(i['blood_group'])
        days_in_year = 365.2425 
        age = int((date.today() - i['birthdate']).days / days_in_year) 
        dob.append(age)
        avg_dob=mean(dob)
        lat.append(i['current_location'][0])
        lon.append(i['current_location'][1])
        mean_latitude=mean(lat)
        mean_longitude=mean(lon)
    k=mode(z) 
    print(k)
    s=max(dob)
    print(s)
    print(avg_dob)
    print(f'Decimal({mean_latitude},{mean_longitude})') 
    end=perf_counter()
    total+=end-start
    print(total)
    return k,s,avg_dob


def named_tuple_approach_fo_solution():
    z=[]
    dob=[]
    lat=[]
    lon=[]
    total=0
    fake = Faker()

    for i in range(10000):
        
        c=fake.profile()
        Data = namedtuple('Data',sorted(c) )
        d=Data(**c)
        z.append(d[2])
        days_in_year = 365.2425 
        age = int((date.today() - d[1]).days / days_in_year)
        dob.append(age)
        lat.append(d[4][0])
        lon.append(d[4][1])
        mean_latitude=mean(lat)
        mean_longitude=mean(lon)
         



    x=mode(z) 
    k=max(dob)
    l=mean(dob)
    m= f'Decimal({mean_latitude},{mean_longitude})'

    print(x)
    print(k)
    print(l)
    #print(f'Decimal({mean_latitude},{mean_longitude})')
    print(m)
    end=perf_counter()  
    total+=end-start
    print(total)
    return x,k,l,m


def gen_data(company, sym, date, openn, close, high):
    return Stock(company, sym, date, openn, close, high)


def gen_stock_weight(weight):
    return StockWeight(weight)


def stock_exchange_creation():
    Stock = namedtuple('Stock','company sym date openn close high')
    data = []

    for i in range(10):
        company = fake.company()
        sym = company[0:2]+company[-2]
        openn = random.randrange(250,500)
        date = '28.09.2020'
        #cont= random.uniform(0.10,0.90)*openn
       
        high  = random.randrange(openn,int(1.2*openn))
        close = random.randrange(int(0.8*openn),high)
        data.append(gen_data(company, sym, date, openn,close, high))
        print('comp-Sym Open High Close')

    for i in data:
        print(i.sym,i.openn,i.high,i.close)
    StockWeight = namedtuple('StockWeight','weight')
    stock_weight = [ gen_stock_weight( weight = random.uniform(0.01,0.9) ) for _ in range(10) ]
    open=[data[i].openn for i in range(10)]
    cont_s  = [ data[i].openn * stock_weight[i].weight for i in range(10) ]
    index_high  = [ data[i].high  * stock_weight[i].weight for i in range(10) ]
    index_close = [ data[i].close * stock_weight[i].weight for i in range(10) ]
    a=sum(open)
    b=sum(cont_s)
    c=sum(index_high)
    d=sum(index_close)
    Exchange=namedtuple('Exchange','open cont_s index_high index_close')
    l=Exchange(a,b,c, d)
    return b,c,d

