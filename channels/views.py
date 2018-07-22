from django.shortcuts import render
from .models import Channel
# Create your views here.
def index(request):
    channels = Channel.objects.all()
    context = {
        'channels': channels
    }
    return render(request, 'channels/index.html', context)