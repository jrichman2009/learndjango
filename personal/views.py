from django.shortcuts import render, get_object_or_404
from django.forms import ModelForm
from .models import Site_pixel
from django.core import serializers

data = serializers.serialize( "python", Site_pixel.objects.all() )

# Create your views here.

def index(request):
	all_pixels = Site_pixel.objects.filter(id=500).values()
	return render(request, 'personal/home.html', {'Site_pixel': Site_pixel})
    
def contact(request):
	return render(request, 'personal/basic.html')
	
