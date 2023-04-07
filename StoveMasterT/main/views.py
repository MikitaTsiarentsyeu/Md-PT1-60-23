from django.shortcuts import render
from .models import Regi
from .forms import RegiForm

def index(request):
    
    count_id = Regi.objects.latest('id')
    return render(request, 'main/index.html', {'count_id':count_id})

def create(request):
    form = RegiForm()
    data = {
        'form':form
    }

    return render(request, 'main/create.html', data)

