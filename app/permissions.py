from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.views import APIView
from .models import App
from rest_framework.authentication import TokenAuthentication
from django.core.exceptions import ObjectDoesNotExist

class IsAdminOf(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user in obj.admins.all()

class AppView(APIView):
    permission_classes = (permissions.IsAuthenticated, IsAdminOf)

    def get_app(self, app_id):
        app = get_object_or_404(App, id=app_id)
        self.check_object_permissions(self.request, app)
        return app


def is_app(user):
    try:
        App.objects.get(credenciales=user)
        return True
    except App.DoesNotExist:
        return False
