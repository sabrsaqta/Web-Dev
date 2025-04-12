from django.shortcuts import render
from rest_framework import generics
from .models import Company, Vacancy
from .serializers import CompanySerializer, VacancySerializer

# Create your views here.

class CompanyList(generics.ListCreateAPIView):
    