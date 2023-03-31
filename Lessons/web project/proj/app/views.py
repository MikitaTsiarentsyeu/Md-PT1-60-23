from django.shortcuts import render
import datetime
import time

# Create your views here.
def test(request):
    current = datetime.datetime.now()
    time.sleep(10)
    return render(request, 'testPage.html', {"ct":current})