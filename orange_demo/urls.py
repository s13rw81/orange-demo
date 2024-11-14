"""
URL configuration for orange_demo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import include
from responsive import views as v

urlpatterns = [
        path('', v.index_view, name='index'),
        path('admin/', admin.site.urls),
        path('construction/', v.about_construction, name='construction'),
        path('contact/', v.contact, name='contact'),
        path('cookies/', v.cookies, name='cookies'),
        path('energy/', v.about_energy, name='energy'),
        path('impressum/', v.impressum, name='impressum'),
        path('index/', v.index_view, name='index'),
        path('newspaper/', v.newspaper, name='newspaper'),
        path('prices/', v.prices, name='prices'),
        path('privacy/', v.privacy, name='privacy'),
        path('solution/', v.solution_view, name='solution'),
        path('sustainability/', v.sustainability, name='sustainability'),
        path('terms_of_use/', v.terms_of_use, name='terms_of_use'),
]
