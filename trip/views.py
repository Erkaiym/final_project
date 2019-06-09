from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView

from project.decorators import profile_required
from proposal.models import Proposal
from user.models import User
from .models import Trip
from .forms import TripForm


def trip_list(request):
    queryset = Trip.objects.all().order_by('-id')
    profile = request.user.profile
    context = {'object_list': queryset,
               'name': profile.name,
               'tel_number': profile.tel_number}

    if request.method == 'POST':
        trip_id = request.POST.get('trip_id')
        trip = Trip.objects.filter(id=trip_id).last()
        if trip:
            Proposal.objects.get_or_create(
                name=profile.name,
                tel_number=profile.tel_number,
                profile=profile,
                trip=trip,
            )
            messages.success(request, 'Запрос успешно отправлен')
            return redirect('user-detail')
        messages.error(request, 'Поездка не была найдена.')
    return render(request, "trip/list.html", context)


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
    title = 'Update a trip'
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            # return redirect(trip.get_absolute_url())
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


def trip_owner(request, id):
    owner = get_object_or_404(User, id=id)
    return owner# redirect(owner.get_absolute_url())
