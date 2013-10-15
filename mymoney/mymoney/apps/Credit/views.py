# Create your views here.

from django.contrib.auth.models import User
from apps.Credits.models import Credit
from apps.Sources.models import Source


def viewCredit(request):

    if request.method = 'POST':
        if request.user.is_authenticated():
        
            user_obj = User.objects.get(user=request.user)

            credits =  Credit.objects.filter(user=user_obj)

            render_to_response('',{"credits":"credits"}, context_instane=RequestContext(request))


def gaveCredit(request):
    if request.method = 'POST':
       if request.user.is_authenticated():
           
           
           source_name = request.POST["deductFromSource"]
           sources = Source.objects.filter(user=request.user, title=source_name)
           
           #Post Data
           to = request.POST["to"]
           amount = request.POST["amount"]
           status = request.POST["status"]
           user_obj = request.user         
           credit = Credit.objects.create(to=to, amount=amount, status=status, user=user_obj, issued_date=request.POST["issued_date"], expected_clearance_date=clearance_date) 

           redirect("/Credits/view/")       
