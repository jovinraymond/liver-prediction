from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import  authenticate,login,logout
# Create your views here.
from django.contrib.auth.decorators import login_required
import re

import joblib

from .models import LiverCirrhosisPrediction
import os
from django.conf import settings


model_path = os.path.join(settings.BASE_DIR, 'base', 'ml_models', 'liver_cirrhosis_model.pkl')
model = joblib.load(model_path)


@login_required(login_url='login')
def HomePage(request):
    prediction = None
    if request.method == 'POST':
        n_days = float(request.POST.get('n_days'))
        hepatomegaly = float(request.POST.get('hepatomegaly'))
        albumin = float(request.POST.get('albumin'))
        platelets = float(request.POST.get('platelets'))
        prothrombin = float(request.POST.get('prothrombin'))
        status = float(request.POST.get('status'))

        # Model prediction
        prediction = model.predict([[n_days, hepatomegaly, albumin, platelets, prothrombin, status]])[0]

        # Save to database
        LiverCirrhosisPrediction.objects.create(
            n_days=n_days,
            hepatomegaly=hepatomegaly,
            albumin=albumin,
            platelets=platelets,
            prothrombin=prothrombin,
            status=status,
            prediction=prediction
        )

    return render(request, 'home.html', {'prediction': prediction})
    

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        # Email validation regex pattern
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        # Password validation regex pattern
        password_pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

        # Check if email is valid
        if not re.match(email_pattern, email):
            return HttpResponse("Invalid email format")

        # Check if passwords match
        if pass1 != pass2:
            return HttpResponse("Your passwords do not match")

        # Check if password meets the criteria
        if not re.match(password_pattern, pass1):
            return HttpResponse(
                "Password must be at least 8 characters long, "
                "include at least one uppercase letter, one lowercase letter, "
                "one number, and one special character"
            )

        # Create and save the user if validations pass
        my_user = User.objects.create_user(uname, email, pass1)
        my_user.save()
        return redirect('login')

    return render(request, 'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('username or password is incorrect!!')
        
    return render(request,'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def RetrievalPage(request):
    # Retrieve all entries from the database
    predictions = LiverCirrhosisPrediction.objects.all().order_by('-id')  # Order by latest

    # Pass the predictions to the template
    return render(request, 'retrieval.html', {'predictions': predictions})