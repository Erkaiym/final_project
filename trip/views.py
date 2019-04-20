from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect


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
    form = TripForm(request.POST or None, )
    #trip = Trip.objects.create(id=request.user.profile.id)
    title = 'Create a trip'
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                trip = form.save(commit=False)
                trip.user = request.user.profile
                trip.save()
                return redirect('trip-list')
    else:
        messages.warning(request, 'Войтите в свой акаунт')
        return redirect('login-page')
    return render(request, "trip/create_trip.html", locals())

#def search(request):
