from django.shortcuts import render
from  .models import Mobiles

# Create your views here.
def index(request):

    mobs = Mobiles.objects.all()

    return render(request, 'index.html', {'mobs':mobs})