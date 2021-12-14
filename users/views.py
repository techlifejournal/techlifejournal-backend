from users.serializer import UserInfoSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from users.serializer import UserSerializer, AuthorDetailsSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics
from users.models import User
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from django.conf import settings
import environ

env = environ.Env()
environ.Env.read_env()


class UserCreate(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def post(self, request, format="json"):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserDetails(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserInfoSerializer

    def get_queryset(self):
        user = self.request.user
        user_details = User.objects.filter(id=user.id)
        return user_details


class GetAuthor(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = AuthorDetailsSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        id_string = self.request.GET.get("id")
        uname = self.request.GET.get("uname")
        if id_string is not None:
            ids = [int(id) for id in id_string.split(",")]
            return User.objects.filter(id__in=ids)
        if uname is not None:
            return User.objects.filter(user_name=uname)
        return queryset


class GoogleLoginView(SocialLoginView):
    authentication_classes = []
    adapter_class = GoogleOAuth2Adapter
    callback_url = env("CALLBACK_URL")
    client_class = OAuth2Client
