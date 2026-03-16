from django.contrib import admin
from django.urls import path
from blog import views # Yazdığım views dosyasını içeri aktardım

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.anasayfa, name='anasayfa'), # Ana sayfayı benim kodlara bağladım
]