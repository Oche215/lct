from django.urls import path
from .views import home, chart_data, chart_view, chart_page, import_data

urlpatterns = [
    path('import/', import_data, name='import'),
    path("chart-page/", chart_page, name="chart-page"),
    path('chart-data/', chart_data, name='chart_data'),
    path('chart-view/', chart_view, name='chart_view'),
    path("", home, name="home"),

]