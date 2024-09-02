from django.urls import path, include

urlpatterns = [
    path('userreg/', include('apps.userreg.urls')),
]