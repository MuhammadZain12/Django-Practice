from django.urls import path
from . import views

# For relative Url Use
app_name='myApp'

# In-app url patterns

urlpatterns=[
  path('sign_up/',views.sign_up,name='sign_up'),
  path('login/',views.user_login,name='login'),
  path('logout/',views.user_logout,name='logout'),
  path('home/',views.home,name='home'),
  path('other/',views.other,name='other'),
  path('welcome/',views.welcome,name='welcome'),
]