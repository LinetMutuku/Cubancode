from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView
from django.shortcuts import render, redirect, get_object_or_404

from app.form import loginform, GuestForm
from app.models import Guest


# Create your views here.

def signin(request):
    if request.method == 'GET':
        form = loginform()
        return render(request, 'login.html', {'form': form})
    elif request.method == 'POST':
        form = loginform(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)

                messages.success(request, 'Successfully logged in')
                return redirect('home')

        messages.error(request, 'Invalid username or password')
        return render(request, 'login.html', {'form': form})


class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    email_template_name = 'registration/password_reset_email.html'
    success_url = '/password-reset/done/'


@login_required
def about(request):
    return render(request, 'about.html')


@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def rooms(request):
    return render(request, 'rooms.html')


@login_required
def blog(request):
    return render(request, 'blog.html')


@login_required
def contact(request):
    return render(request, 'contact.html')



def signout(request):
    logout(request)
    return redirect('signin')


def search_rooms(request):
    search_query = request.GET.get('search', '')

    data = [
        {'name': 'Room 1', 'price': 10000},
        {'name': 'Room 2', 'price': 55000},
    ]
    results = [room for room in data if
               search_query.lower() in room['name'].lower() or str(search_query) in str(room['price'])]
    return render(request, 'search.html', {'results': results, 'search_query': search_query})


@login_required
def guest_delete(request, guest_id):
    guest = get_object_or_404(Guest, pk=guest_id)
    guest.delete()
    messages.warning(request, 'The reservation was deleted permanently.')
    return redirect('all')


@login_required
def guest_update(request, guest_id):
    guest = get_object_or_404(Guest, pk=guest_id)  # SELECT * FROM employees  WHERE id=1
    if request.method == 'POST':
        form = GuestForm(request.POST, request.FILES, instance=guest)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reservation updated successfully!')
            return redirect('details', guest_id)
    else:
        form = GuestForm(instance=guest)
    return render(request, 'update.html', {'form': form})


def booknow(request):
    if request.method == 'POST':
        form = GuestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, 'Your reservation is  saved!')
            return redirect('all')
    else:
        form = GuestForm()
    return render(request, 'booknow.html', {'form': form})


def all_guests(request):
    guests = Guest.objects.all()
    return render(request, 'all_guests.html', {"guests": guests})


def guest_details(request, guest_id):
    guest = Guest.objects.get( pk=guest_id)
    return render(request, 'guest_details.html', {"guest": guest})


def view_rooms(request):
    return render(request, 'view_rooms.html')


def room_details(request):
    return render(request, 'room_details.html')