from django.shortcuts import render
from . models import Place,Members
# Create your views here.
def home(request):
    obj=Place.objects.all()
    mem=Members.objects.all()
    return render(request,'index.html',{'result':obj,'res':mem})