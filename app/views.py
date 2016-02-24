from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
from .utils import raw_sql_search, secret_key_gen
from .permissions import AppView
from claims.views import login

@api_view(['POST'])
def apptoken(request, format=None):
    app_id = request.data.get('app_id','')
    password = request.data.get('secret_key','')

    if not app_id or not password:
        return Response({'message': 'Incorrect params'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        app = App.objects.get(id=app_id)
    except App.DoesNotExist:
        return Response({'message': 'No such app'}, status=status.HTTP_404_NOT_FOUND)

    user = authenticate(username=app.credenciales.username, password=password)
    if not user:
        return Response({'message': 'Invalid credentials_'+app.credenciales.username+'_'+password}, status=status.HTTP_401_UNAUTHORIZED)

    token, _ = Token.objects.get_or_create(user=user)

    return Response({'token': token.key}, status=status.HTTP_200_OK)

@api_view(['POST'])
def validate_token(request, format=None):
    token = request.data.get('token','')

    if not token:
        return Response({'message': 'Incorrect params'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        Token.objects.get(key=token)
    except Token.ObjectDoesNotExist:
        return Response({'message': 'No such app'}, status=status.HTTP_404_NOT_FOUND)

    return Response({'message': "OK"}, status=status.HTTP_200_OK)

@login_required
def select_app(request, format=None):
    apps = App.objects.filter(admins__id__exact=request.user.id)

    if not apps:
        return render(request, 'no_apps.html', {})

    return redirect("/apps/%d/" % apps[0].id)

class AppHomeView(AppView):
    def get(self, request, app_id, format=None):
        app = self.get_app(app_id)
        return render(request, 'app/home.html', {'app': app})

class AppResetKeyView(AppView):
    def get(self, request, app_id, format=None):
        app = self.get_app(app_id)

        show = request.GET.get('show', '')
        key = app.get_key() if show == 'yes' else ''

        return render(request, 'app/reset.html', {'app':app, 'key': key})

    def post(self, request, app_id, format=None):
        app = self.get_app(app_id)
        key = secret_key_gen()
        app.set_key(key)
        return render(request, 'app/reset.html', {'app':app, 'key':key})
