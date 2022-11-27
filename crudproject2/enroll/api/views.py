from enroll.models import User
from enroll.api.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle


class UserViewSet(viewsets.ModelViewSet):
 queryset = User.objects.all()
 serializer_class = UserSerializer
 authentication_classes = [SessionAuthentication]
 permission_classes = [IsAuthenticated]
 permission_classes = [IsAuthenticatedOrReadOnly]
 throttle_classes = [AnonRateThrottle, UserRateThrottle]