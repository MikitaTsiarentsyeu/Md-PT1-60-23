from django.shortcuts import render, redirect
from .forms import RegiForm
from .models import Base

# Create your views here.

def index(request):
    
    try:
        count_id = Base.objects.latest('id')
    except:
        count_id = 0
    return render(request, 'main/index.html', {'count_id':count_id})

def create(request):
    error = ''
    if request.method == 'POST':
        form = RegiForm(request.POST)
        if form.is_valid() and form.clean_subtitle() == True:
            
            
            form.save()
          
            return redirect('success')     
            
        else:
            error = 'Форма была неверной'

    form = RegiForm()
    
    data = {
        'form':form,
        'error':error
    }

    return render(request, 'main/create.html', data)


def success(request):

    try:
        count_id = Base.objects.latest('id')
    except:
        count_id = 0
 
    return  render(request, 'main/success.html', {'count_id':count_id})

def add(request):

    try:
        number_id = Base.objects.latest('id')
        all = Base.objects.all()
    except:
        number_id = 0
        all = ''
    return  render(request, 'main/add.html', {'number_id':number_id, 'all':all})
   
    
    
    
    