from django.urls import path
from apps.userreg.views import (UserRegView)
                                # UserListView
                                

urlpatterns = [
    path('register/',UserRegView.as_view(), name = 'user-register'),
    # path('users/', UserListView.as_view(), name = 'user-list)'),
]