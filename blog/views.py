from django.shortcuts import render
from .models import Makale

def anasayfa(request):
    # Veritabanındaki tüm makaleleri alıyoruz
    yazilar = Makale.objects.all() 
    # Bu makaleleri 'anasayfa.html' dosyasına gönderiyoruz
    return render(request, 'anasayfa.html', {'yazilar': yazilar})