from django.urls import path, include

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
from api import views

app_name = 'api'

urlpatterns = [
    path('cleaner/', views.CleanerListCreateView.as_view(), name='cleaner-list-create'),
    path('appointment/', views.AppointmentListCreateView.as_view(), name='appointment-list-create'),

]
