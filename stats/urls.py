from django.urls import path
from .views import MaxTempViewAll, MaxTempFilter

urlpatterns = [
    path('', MaxTempViewAll.as_view(), name="max-temp"),
    path('<str:filter>/', MaxTempFilter.as_view())  
]
