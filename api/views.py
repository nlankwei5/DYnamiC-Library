from django.shortcuts import render
from .serializer import * 
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import *
from rest_framework import viewsets



# Create your views here.

class MusicSheetViewSet(viewsets.ModelViewSet):
    queryset = MusicSheet.objects.all()
    serializer_class = MusicSheetSerializer
    
    def get_permissions(self):

        if self.action == ['create','update', 'partial_update', 'destroy']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def perform_create(self, serializer):
        serializer.save(uploaded_by = self.request.user)

    
    

