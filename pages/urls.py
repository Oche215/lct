from django.urls import path
from .views import home, chart_data, chart_view

urlpatterns = [
    path('chart-data/', chart_data, name='chart_data'),
    path('chart-view/', chart_view, name='chart_view'),
    path("", home, name="home"),

]