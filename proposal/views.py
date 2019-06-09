from django.shortcuts import render

from proposal.models import Proposal


def list(request):
    queryset = Proposal.objects.all()
    return queryset
