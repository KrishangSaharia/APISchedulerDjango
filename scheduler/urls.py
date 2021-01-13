from django.urls import path

from .views import schedule_url, ping_status

app_name = 'scheduler'

urlpatterns = [
    path('', schedule_url, name='schedule_url'),
    path('ping', ping_status, name = "ping_status")
]