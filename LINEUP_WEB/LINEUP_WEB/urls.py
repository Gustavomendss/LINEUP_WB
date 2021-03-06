"""LINEUP_WEB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""LINEUP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from core import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('new-todo', views.new_todo, name="new_todo"),
    path('mark-as-done/<int:id>', views.mark_as_done, name="mark_as_done"),

]
if settings.DEBUG:
   urlpatterns += staticfiles_urlpatterns()
   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



'''

from django.contrib import admin
from django.urls import path
#from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('lineupapp.urls')),

]

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
OUUUU

from django.contrib import admin
from django.urls import include, path
#from django.urls import include
from LINEUPAPP import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('LINEUPAPP/', include ("LINEUPAPP.urls")),# Isso est?? direcionando para o seu aplicativo
    path('', views.index, name='index'),
    path('new-todo', views.new_todo, name="new_todo"),
    path('mark-as-done/<int:id>', views.mark_as_done, name="mark_as_done"),

]

'''