from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model

import json

User = get_user_model()

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        email = data['email']
        password = data['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'})
        else:
            return JsonResponse({'message': 'Invalid credentials'}, status=401)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)
    
@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        email = data['email']
        password = data['password']
        username = data['username']
        print('email',email)
        if email and password:
            if User.objects.filter(email=email).exists():
                return JsonResponse({'message': 'Email already exists'}, status=400)
            user = User.objects.create_user(email=email, password=password, username=username)
            return JsonResponse({'message': 'Registration successful'})
        else:
            return JsonResponse({'message': 'Invalid data'}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)
