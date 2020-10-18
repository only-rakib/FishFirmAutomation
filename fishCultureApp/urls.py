
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view,name='home' ),
    path('<value>',views.url_view,name="url_view")
]
