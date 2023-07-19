from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

import json

User = get_user_model()


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        # email = data['email']
        password = data['password']
        username = data['username']

        user = authenticate(request, 
                            password=password, username=username)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'})
        else:
            return JsonResponse({'message': 'Invalid credentials'}, status=401)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)

@csrf_exempt
def logout_view(request):
    print(request)
    logout(request)
    return JsonResponse({'message': 'logout successful'})

@csrf_exempt
def check_login_view(request):
    if request.user.is_authenticated:
        # User is logged in
        # Do something for authenticated users
        print(request.user.email)
        data = {
            'username': request.user.username,
            'message': 'You are logged in.',
        }
    else:
        # User is not logged in
        # Do something for anonymous users
        data = {
            'message': 'You are not logged in.',
        }

    return JsonResponse(data)

@csrf_exempt
def get_data_test_view(request):
    if request.user.is_authenticated:
        user = User.objects.filter(email="test1@gmail.com").first()
        print(user)
        data = {
            'username': user.username,
            'message': 'get test data.',
        }
    else:
        # User is not logged in
        # Do something for anonymous users
        data = {
            'message': 'You are not logged in to get data.',
        }

    return JsonResponse(data)

@csrf_exempt
def register_view(request):
    if request.method == 'POST':

        data = json.loads(request.body)

        email = data['email']
        password = data['password']
        username = data['username']
        print('email', email)
        if email and password:
            if User.objects.filter(email=email).exists():
                return JsonResponse({'message': 'Email already exists'}, status=400)
            user = User.objects.create_user(
                email=email, password=password, username=username)
            return JsonResponse({'message': 'Registration successful'})
        else:
            return JsonResponse({'message': 'Invalid data'}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)
