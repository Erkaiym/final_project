from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from project.decorators import profile_required
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


@profile_required
def create_trip(request):
    form = TripForm(request.POST or None)
    title = 'Create a trip'
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                trip = form.save(commit=False)
                trip.user = request.user.profile
                trip.save()
                return redirect('trip-list')
    else:
        messages.info(request, 'Войдите в свой аккаунт')
        return redirect('login-page')
    return render(request, "trip/create_trip.html", locals())


def update_trip(request, id):
    trip = get_object_or_404(Trip, id=id)
    form = TripForm(request.POST or None, instance=trip)
    title = 'Update a product'
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('trip-detail')
    return render(request, "trip/update_trip.html", locals())


def confirm_delete_trip(request, id):
    trip = get_object_or_404(Trip, id=id)
    return render(request, "trip/delete_trip.html", locals())


def delete_trip(request, id):
    trip = get_object_or_404(Trip, id=id)
    trip.delete()
    messages.info(request, 'Поездка удалена')
    return redirect("trip-list")


class SearchView(ListView):
    template_name = 'trip/list.html'

    def get_queryset(self):
        request = self.request
        qstart = request.GET.get('qstart')
        qend = request.GET.get('qend')
        qs = Trip.objects.all()

        if qstart:
            qs = qs.filter(start__icontains=qstart)

        if qend:
            qs = qs.filter(end__icontains=qend)

        return qs


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q-start') and self.request.GET.get('q-end')
        return context