from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import re
import joblib
import os
from django.conf import settings
from .models import LiverCirrhosisPrediction

# Load the prediction model
model_path = os.path.join(settings.BASE_DIR, 'base', 'ml_models', 'liver_cirrhosis_model.pkl')
model = joblib.load(model_path)

# Home page view
def HomePage(request):
    # Render the home page with general content, no prediction form
    return render(request, 'homepage.html')

# Prediction page view
@login_required(login_url='login')
def PredictionPage(request):
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

        # Save prediction result to the database
        LiverCirrhosisPrediction.objects.create(
            n_days=n_days,
            hepatomegaly=hepatomegaly,
            albumin=albumin,
            platelets=platelets,
            prothrombin=prothrombin,
            status=status,
            prediction=prediction
        )

    return render(request, 'prediction.html', {'prediction': prediction})

# Signup page view
def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        password_pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

        if not re.match(email_pattern, email):
            return HttpResponse("Invalid email format")

        if pass1 != pass2:
            return HttpResponse("Your passwords do not match")

        if not re.match(password_pattern, pass1):
            return HttpResponse(
                "Password must be at least 8 characters long, "
                "include at least one uppercase letter, one lowercase letter, "
                "one number, and one special character"
            )

        my_user = User.objects.create_user(uname, email, pass1)
        my_user.save()
        return redirect('login')

    return render(request, 'signup.html')

# Login page view
def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('username or password is incorrect!!')

    return render(request, 'login.html')

# Logout page view
def LogoutPage(request):
    logout(request)
    return redirect('login')
