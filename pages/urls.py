from django.urls import path
from .views import home, chart_data, chart_view, chart_page, import_data

urlpatterns = [
    path('import/', import_data, name='import'),
    path("view-chart/", chart_page, name="view_chart"),
    path('chart-data/', chart_data, name='chart_data'),
    path('chart-view/', chart_view, name='chart_view'),
    path("", home, name="home"),

]