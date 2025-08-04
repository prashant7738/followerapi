from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response  # ✅ Fix: Correct import
from rest_framework.decorators import api_view
from .models import FacebookFollower
from .serializers import FacebookFollowerSerializer
from django.http import JsonResponse

# ✅ Class-based view for listing and posting followers
class FacebookFollowerListCreateView(generics.ListCreateAPIView):
    queryset = FacebookFollower.objects.all()
    serializer_class = FacebookFollowerSerializer

# ✅ Function-based API view for latest follower count
@api_view(['GET'])  # ✅ Fix: Tell Django it's an API endpoint
def get_latest_follower_count(request, page):
    latest = FacebookFollower.objects.filter(page_name=page).order_by('-scraped_at').first()
    
    if latest:
        return Response({
            # 'page_name': latest.page_name,
            'followers': latest.followers,  # ✅ Fix: Use correct field name
            # 'scraped_at': latest.scraped_at
        })
    else:
        return Response({"error": "Page not found"}, status=404)
