from django.urls import path
from .views import square_view


#put url beneath it

urlpatterns = [
    path('square/',  square_view, name='square_view')
]