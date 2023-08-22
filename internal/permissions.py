# -*- encoding: utf-8 -*-
from rest_framework.permissions import BasePermission
from django.utils.translation import gettext_lazy as _


class OwnObject(BasePermission):
    def has_permission(self, request, view):
        ret = False
        if request.method == 'GET':
                ret = True
        elif request.method == 'PATCH' or request.method == 'POST' and request.user.is_authenticated:
            ret = True
        else:
            ret = False
                
        return ret
                
    def has_object_permission(self, request, view, obj):

        ret = False

        if request.method == 'DELETE':
            if obj.id == request.user.id:
                ret = True
        elif request.method == 'GET':
            ret = True
        elif request.method == 'PATCH':
            ret = obj.id == request.user.id

        return ret
