from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('postjob/', views.postjob, name='postjob'),
    path('accounts/', include('accounts.urls')),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
