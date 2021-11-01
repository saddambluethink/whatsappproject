from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import request
#import pywhatkit as kit

import webbrowser as web
import pyautogui as pg
import time

#Create your views here.

def send_whatsapp_massage(request):
    if request.method=="POST":
        phone="91"+request.POST['mobile']
        msg=request.POST['massage']
        print(phone,msg)
        web.open('https://web.whatsapp.com/send/?phone='+phone+'&text='+msg)
        time.sleep(10)
        pg.press('enter')
        # kit.sendwhatmsg("+918814024487", "I love coding!",13,15) 
        msg="massage send successfully"
        return render(request, 'form.html',{'msg':msg})
   
    return render(request, 'form.html')
