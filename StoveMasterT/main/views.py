from django.shortcuts import render
from .models import Reg


def index(request):
    # n = Reg.objects.all()
    count_id = Reg.objects.latest('id')
    return render(request, 'main/index.html', {'count_id':count_id})

def create(request):
    return render(request, 'news/create.html')

