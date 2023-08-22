# -*- encoding: utf-8 -*-

# Django
from django.shortcuts import render
from django.contrib.auth.models import User
from internal.models import Brand, Car
from internal.permissions import OwnObject

# Django Rest
from rest_framework import viewsets, permissions, mixins
from rest_framework.filters import OrderingFilter, SearchFilter


# Serializers
from internal.serializers import BrandSerializer, CarSerializer, UserSerializer

# Extras
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter

class SignUpViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

class CurrentUserViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):

        queryset = self.queryset
        return queryset.filter(id=self.request.user.id)

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
class CarFilter(FilterSet):

    brand__name = CharFilter(
        field_name="brand__name",
        lookup_expr="icontains"
    )
    class Meta:
        model = Car
        fields = [
            'id',
            'model',
            'brand__name',
            'state__name'
        ]

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)
    permission_classes = (OwnObject,)
    lookup_field = ('url_slug')
    filterset_class = CarFilter
    search_fields = ('model', 'state__name')
    
    def get_queryset(self):

        queryset = self.queryset

        return queryset.filter(state_id=1)

    def perform_destroy(self, instance):
        instance.state_id = 2
        instance.save()


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)
    permission_classes = (permissions.AllowAny,)
    lookup_field = ('url_slug')
    search_fields = ('model', 'state__name')
    
    def get_queryset(self):

        queryset = self.queryset

        return queryset.filter(state_id=1)

    def perform_destroy(self, instance):
        instance.state_id = 2
        instance.save()