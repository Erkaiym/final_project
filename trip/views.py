from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from .models import Trip
from .forms import TripForm


def trip_list(request):
    queryset = Trip.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "trip/list.html", context)


def trip_detail(request, id):
    instance = get_object_or_404(Trip, id=id)
    context = {
        'object': instance
    }
    return render(request, "trip/detail.html", context)


def create_trip(request):
    form = TripForm(request.POST or None)
    title = 'Create a trip'
    if request.user.is_authenticated:
        # if not request.user.profile:
        if request.method == 'POST':
        #     messages.warning(request, 'Заполните свой профайл')
        #     return redirect('register-profile-page')
        # else:
            if form.is_valid():
                trip = form.save(commit=False)
                trip.user = request.user.profile
                trip.save()
                return redirect('trip-list')
    else:
        messages.info(request, 'Войдите в свой аккаунт')
        return redirect('login-page')
    return render(request, "trip/create_trip.html", locals())


class SearchView(ListView):
    template_name = 'trip/list.html'

    def get_queryset(self):
        request = self.request
        qstart = request.GET.get('qstart')
        qend = request.GET.get('qend')
        if qstart and qend:
            res = Trip.objects.filter(Q(start__icontains=qstart) | Q(end__icontains=qend))
            return res
        else:
            return Trip.objects.none()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q-start') and self.request.GET.get('q-end')
        return context