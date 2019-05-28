from django.shortcuts import render

from request.forms import RequestForm


def request(request):
    form = RequestForm(request.POST or None,
                    instance{'name':user.profile.name})
