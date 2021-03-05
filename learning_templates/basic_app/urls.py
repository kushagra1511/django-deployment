from django.urls import path
from basic_app import views

# TEMPLATE TAGGINR
app_name = 'basic_app'

urlpatterns =[
    path('relative/',views.relative , name = 'index'),
    path('other/',views.other , name = 'other'),
]