"""iabs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
    url(r'^', include('iabs_main.urls', namespace='iabs', app_name='iabs')),
    url(r'^usuario/', include('usuario.urls', namespace='usuario', app_name='usuario')),
    url(r'^iabs/', include('iabs_main.urls', namespace='iabs', app_name='iabs')),
    url(r'^projeto/', include('projeto.urls', namespace='projeto', app_name='projeto')),
    

]
