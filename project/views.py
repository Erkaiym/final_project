from django.shortcuts import render, redirect
from django.urls import reverse


def main_page(request):
    return render(request, 'home.html', locals())


def about(request):
    return render(request, 'about.html', locals())


def blog(request):
    return render(request, 'blog.html', locals())


def contact(request):
    return render(request, 'contact.html', locals())



