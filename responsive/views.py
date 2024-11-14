from django.shortcuts import render
from django.views.generic import TemplateView

from django.shortcuts import render


def index_view(request, *args, **kwargs):
    return render(request, "index.html", {})


def solution_view(request, *args, **kwargs):
    return render(request, "solution.html", {})


def about_energy(request, *args, **kwargs):
    return render(request, "about_energy.html", {})


def about_construction(request, *args, **kwargs):
    return render(request, "about_construction.html", {})


def sustainability(request, *args, **kwargs):
    return render(request, "sustainability.html", {})


def prices(request, *args, **kwargs):
    return render(request, "prices.html", {})


def newspaper(request, *args, **kwargs):
    return render(request, "newspaper.html", {})


def privacy(request, *args, **kwargs):
    return render(request, "privacy.html", {})


def cookies(request, *args, **kwargs):
    return render(request, "cookies.html", {})


def terms_of_use(request, *args, **kwargs):
    return render(request, "terms_of_use.html", {})


def contact(request, *args, **kwargs):
    return render(request, "contact.html", {})


def impressum(request, *args, **kwargs):
    return render(request, "impressum.html", {})


