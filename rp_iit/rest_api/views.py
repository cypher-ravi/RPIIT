from django.shortcuts import render,get_list_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import Announcement,Department
from .serializers import AnnouncementSerializer,DepartmentSerializer

# Create your views here.
class AnnouncementListView(generics.GenericAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

    def get(self, request, *args, **kwargs):
        if Department.objects.filter(name=kwargs['slug']).exists():
            announcements = Announcement.objects.filter(department__name=kwargs['slug']).order_by('-announce_date')
            if not announcements:
                return Response({'detail':'no announcements'})
            else:
                serializer = AnnouncementSerializer(announcements,many=True)
                return Response(serializer.data,status=status.HTTP_200_OK)  
        else:
            return Response({'detail':'no such department'})
    
class DepartmentListView(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer