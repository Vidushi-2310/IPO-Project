from django.shortcuts import render,get_object_or_404
from .models import IPO 
from .serializers import IPOSerializer
from rest_framework import generics, filters

def home(request):
    status_filter = request.GET.get('status')
    if status_filter:
        ipos = IPO.objects.filter(status=status_filter)
    else:
        ipos = IPO.objects.all()
    return render(request, 'home.html', {'ipos': ipos})


def ipo_detail(request,pk):
    ipo = get_object_or_404(IPO,pk=pk)
    return render(request,'detail.html',{'ipo':ipo})

class IPOListAPIView(generics.ListAPIView):
    queryset = IPO.objects.all()
    serializer_class = IPOSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['company_name', 'status']
    ordering_fields = ['open_date', 'listing_date', 'ipo_price']

class IPODetailAPIView(generics.RetrieveAPIView):
    queryset = IPO.objects.all()
    serializer_class = IPOSerializer

