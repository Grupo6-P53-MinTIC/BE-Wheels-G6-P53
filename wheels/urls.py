
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
# Import Travel Views
from authApp.views import TravelListCreateView, TravelRetrieveUpdateDeleteView, TravelFkView

from django.urls import path, include
from django.contrib.sites.models import Site

urlpatterns = [
    path('admin/', admin.site.urls),
    # Travel routes 
    path('travels/', TravelListCreateView.as_view()),
    path('travel/<int:pk>', TravelRetrieveUpdateDeleteView.as_view()),
    path('travel_by/<int:id_manager>', TravelFkView.as_view()), #Search travel by fk
    # Rest-auth routes
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('auth/confirm-email/', TemplateView.as_view(), name='account_email_verification_sent'),
]

admin.site.unregister(Site)
