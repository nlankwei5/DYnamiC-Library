from django.shortcuts import render
from .serializer import * 
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter
from .models import *
from rest_framework import viewsets
from rest_framework.decorators import action
from django.http import FileResponse




class MusicSheetViewSet(viewsets.ModelViewSet):
    queryset = MusicSheet.objects.all()
    serializer_class = MusicSheetSerializer
    filter_backends = [filters.DjangoFilterBackend, SearchFilter, filters.OrderingFilter]
    filterset_fields = ['categories']
    search_fields = ['title']
    ordering_fields = ['date_uploaded']
    
    def get_permissions(self):

        if self.action == ['create','update', 'partial_update', 'destroy']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def perform_create(self, serializer):
        serializer.save(uploaded_by = self.request.user)


    @action(detail=True, methods=['get'], permission_classes=[IsAuthenticated])
    def download(self, request, pk=None):
        music_sheet = self.get_object()

        
        DownloadLog.objects.create(user=request.user, sheet=music_sheet)

        response = FileResponse(music_sheet.file.open('rb'), as_attachment=True)
        return response

    
    

