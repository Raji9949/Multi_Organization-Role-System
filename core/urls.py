from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    # Admin site
    path('admin/', admin.site.urls),

    # Include app-level URLs
    path('organization/', include('organization.urls')),  # URLs for the `organization` app

    # Redirect root URL to the organization list view 
    path('', RedirectView.as_view(url='/organization/', permanent=False)),
]