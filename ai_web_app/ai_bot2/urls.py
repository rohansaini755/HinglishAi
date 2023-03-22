"""ai_bot2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from Text import views as tv
from Auth import views as au
from django.conf.urls.static import static
from django.conf import settings
from Submition import views as sa

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/text/',tv.get_text),
    path('api/signup/',au.signup),
    path('api/signin/',au.signin),
    path('api/signout/',au.signout),
    path('api/add_text/',tv.add_text),
    path('api/get_demo_text/',tv.get_demo_text),
    path('api/update_text/',tv.update_text),
    path('api/text/',tv.text),
    path('api/submit/',tv.submit_analysis),
    path('api/submit_answer/',sa.submit_answer),
    path('api/submition_list/',sa.submission_list),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
