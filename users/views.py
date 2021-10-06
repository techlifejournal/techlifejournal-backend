from users.serializer import UserInfoSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView 
from users.serializer import UserSerializer ,AuthorDetailsSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics
from users.models import User

class UserCreate(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    def post(self, request, format='json'):
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
        user =  self.request.user
        return User.objects.filter(id = user.id)

class GetAuthor(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = AuthorDetailsSerializer
    def get_queryset(self):
        queryset = User.objects.all()
        id_string = self.request.GET.get('id')
        if id_string is not None:
            ids = [int(id) for id in id_string.split(',')]
            return User.objects.filter(id__in=ids)
        return queryset