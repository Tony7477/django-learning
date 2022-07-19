from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    name='john'
    context={
        'name':'hariharan',
        'age':18,

    }
    
    #return render(request, 'index.html',{'name':name})
    return render(request, 'index.html',context)
    
def counter(request):
    variables=request.GET['text']
    length=len(variables.split())
    return render(request,'counter.html',{'number_of_words':length})
