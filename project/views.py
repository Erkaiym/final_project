from django.shortcuts import render, redirect
from django.urls import reverse


def main_page(request):
    return render(request, 'home.html', locals())




