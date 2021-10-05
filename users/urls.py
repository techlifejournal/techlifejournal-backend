from django.urls import path
from .views import UserCreate,GetAuthor, BlacklistTokenUpdateView, UserDetails

app_name = 'users'

urlpatterns = [
    path('create/', UserCreate.as_view(), name="create_user"),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist'),
    path('', UserDetails.as_view(),
         name='blacklist'),
     path('authors/', GetAuthor.as_view() ,name = "authors" )
]
