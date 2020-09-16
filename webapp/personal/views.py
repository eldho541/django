from django.shortcuts import render
from account.models import Account 

# Create your views here.
def home_screen_view(request):
    # print(request.headers)
    context = {}
    # # context['somestring'] ="this is some string pass to view"
    # # context ={
    # #     'somestring':"this is some string pass to view/..............."
    # # # }
    # # question = Questions.objects.all()
    # # context['question']=question
    accounts = Account.objects.all()
    context['accounts'] = accounts 
    return render(request,"personal/home.html", context)
 