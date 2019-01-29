from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .forms import SignUpForm
from .tokens import account_activation_token
import os
from django.conf import settings
from .models import Profile
from .models import MyUser
# Create your views here.

def profile(request): #when user is not logged in redirect to login page 
	if not request.user.is_authenticated:
	    return redirect('login')
	return render(request, 'signup/profile.html', context={}, )

def apply(request):
    if request.method == 'POST':
       form = SignUpForm(request.POST)
       if form.is_valid():
           user = form.save()
           user.is_active = False
           user.refresh_from_db()  # load the profile instance created by the signal
           user.profile.first_name = form.cleaned_data.get('first_name')
           user.profile.last_name = form.cleaned_data.get('last_name')
           user.profile.age = form.cleaned_data.get('age')
           user.profile.school = form.cleaned_data.get('school')
           user.profile.major = form.cleaned_data.get('major')
           user.profile.phoneNumber = form.cleaned_data.get('phoneNumber')
           user.profile.Gender = form.cleaned_data.get('Gender')
           user.profile.Race = form.cleaned_data.get('Race')
           user.profile.LevelofStudy = form.cleaned_data.get('LevelofStudy')
           user.profile.gradYear = form.cleaned_data.get('gradYear')
           user.profile.dietRestrictions = form.cleaned_data.get('dietRestrictions')
           #user.profile.Resume = form.cleaned_data.get('Resume')
           #user.profile.Resume = handle_file_upload(request.FILES['Resume'])
           #newResume = Profile(Resume = request.FILES['Resume'])
           user.profile.Resume = form.cleaned_data.get('Resume')
           user.profile.shareBox = form.cleaned_data.get('shareBox')
           user.profile.conductBox = form.cleaned_data.get('conductBox')
           user.profile.questions = form.cleaned_data.get('questions')
           user.profile.meme = form.cleaned_data.get('meme')
           user.save()
           raw_password = form.cleaned_data.get('password1')
           current_site = get_current_site(request)
           subject = 'Activate Your CitrusHack Account'
           message = render_to_string('account_activation/email.html', {
               'user': user,
               'domain': current_site.domain,
               'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
               'token': account_activation_token.make_token(user),
           })
           # user = authenticate(email=user.email, password=raw_password)
           user.email_user(subject, message)
           return redirect('account_activation_sent.html')
           # user = authenticate(username=user.email, password=raw_password) #directly authenticates the user
           # login(request, user)                                            #directly logs in the user 
           # return redirect('profile')                                      #directly takes the user to his/her profile page (@jZhu, these 3 lines are subject to your change I think - jihwan)
    else:
       form = SignUpForm()
    return render(request, 'signup/apply.html', {'form': form})
    # return render(request, 'index.html', context={},)

def account_activation_sent(request):
    return render(request, 'account_activation/sent.html')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = MyUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, MyUser.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'account_activation/invalid.html')
