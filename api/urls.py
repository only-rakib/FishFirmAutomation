
from django.urls import path
from .views import *

urlpatterns = [
    path('r/',StatesViews.as_view()),
    
]
