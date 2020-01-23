from django.urls import path
from .views import BooksListApiView

urlpatterns = [
    path('',BooksListApiView.as_view())
]