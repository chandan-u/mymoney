# Create your views here.

from mymoney.apps.Sources import Source
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.models import User


def createSource(request):
    
    if request.method == 'POST':
        if request.user.is_authenticated():    

            user_obj  = User.objects.get(user=request.user)       
     
            title = request.POST["title"]
            details = request.POST["details"]
            current_balance = request.POST["current_balance"]
            startDate = request.POST["startDate"]
            type = request.POST["type"]
            lock_date = request.POST["lock_date"]
            source  = Source.objects.create(title=title, details=detail, current_balance=current_balance, startDate=startDate, type=type, lock_date=lock_date, suser=user_obj)
        redirect("/Sources/view/")
        



def viewSources(request):
   
    sources = Source.objects.filter(user=request.user)
    
    return render_to_response('', {"sources":"sources"}, context_instance=RequestContext(request))


    
