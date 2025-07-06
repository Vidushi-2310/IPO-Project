from django.shortcuts import render,get_object_or_404
from .models import IPO 

def home(request):
    ipos = IPO.objects.all()
    return render(request,'home.html',{'ipos':ipos})

def ipo_detail(request,pk):
    ipo = get_object_or_404(IPO,pk=pk)
    return render(request,'detail.html',{'ipo':ipo})



# Create your views here.
