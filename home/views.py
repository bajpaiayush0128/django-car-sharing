from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.db.models import F
from .models import Post
from car_sharing import settings
from django.core.mail import send_mail, EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from .tokens import generate_token
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode


def home(request):
    return render(request, "homepage.html")


def PubRide(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            source = request.POST['source']
            destination = request.POST['destination']
            vacant_seats = request.POST['vacant_seats']
            date_of_trip = request.POST['date_of_trip']
            time_of_trip = request.POST['time_of_trip']

            post1 = Post.objects.create(
                source=source, destination=destination, vacant_seats=vacant_seats, date_of_trip=date_of_trip, time_of_trip=time_of_trip)
            post1.user = request.user
            post1.source = source
            post1.destination = destination
            post1.vacant_seats = vacant_seats
            post1.date_of_trip = date_of_trip
            post1.time_of_trip = time_of_trip

            post1.save()

            messages.success(request, "Your ride has been successfully posted")
            return render(request, "homepage.html", {'username': post1.user.username})
        else:
            messages.error(request, "Please login to post a ride.")
            return render(request, "logIn.html")
    return render(request, "PubRide.html")


def rides(request):
    if request.method == "POST":
        leave = request.POST.get('leave')
        arrive = request.POST.get('arrive')
        date = request.POST.get('date')
        number = request.POST.get('number')
        lookup = (Q(source__icontains=leave) &
                  Q(destination__icontains=arrive))
        if leave != None and arrive != None and date != None and number != None:
            rides = Post.objects.filter(lookup)
            return render(request, "rides.html", {
                'rides': rides
            })
    return render(request, "rides.html")


def decrease_counter(request, pk):
    if request.method == "POST":
        ride = Post.objects.get(id=pk)
        ride.vacant_seats = F('vacant_seats') - 1
        ride.save()
        return render(request, "success.html")


def success(request):
    return render(request, "success.html")


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(
                request, "Username already exist! Please try some other username.")
            return render(request, "register.html")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return render(request, "register.html")

        if len(username) > 20:
            messages.error(request, "Username must be under 20 charcters!!")
            return render(request, "register.html")

        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return render(request, "register.html")

        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return render(request, "register.html")

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = first_name
        myuser.last_name = last_name
        myuser.is_active = False
        myuser.save()

        messages.success(
            request, "Your account has been successfully created. Please confirm your email ID by clicking on the confirmation link sent.")

        # Welcome Email
        subject = "Welcome to Car Sharing Service!!"
        message = "Hello " + myuser.first_name + "!! \n" + \
            "Welcome to Car Sharing Service!! \nThank you for visiting our website.\n We have also sent you a confirmation email, please confirm your email address. \n\nThanking You\n Ayush Bajpai"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        # Email Address Confirmation Email
        current_site = get_current_site(request)
        email_subject = "Confirm your Email @ Car Sharing Service!!"
        message2 = render_to_string('email_confirmation.html', {

            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser),
        })
        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email],
        )
        email.fail_silently = True
        email.send()

        return render(request, "logIn.html")

    return render(request, "register.html")


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        login(request, myuser)
        messages.success(request, "Your Account has been activated!!")
        # context = {'uidb64': uidb64, 'token': token}
        return render(request, "logIn.html")
    else:
        return render(request, 'activation_failed.html')


def logIn(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']
        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            return render(request, "homepage.html", {'username': username})

        else:
            messages.error(request, "Bad credential!")
            return render(request, "homepage.html")

    return render(request, "logIn.html")


def logOut(request):
    logout(request)
    messages.success(request, "Logged out successfully !")
    return render(request, "homepage.html")
