from django.urls import path
from .views import home, chart_data, chart_view, import_excel_data

urlpatterns = [
    path("import_data/", import_excel_data, name="import"),
    path('chart-data/', chart_data, name='chart_data'),
    path('chart-view/', chart_view, name='chart_view'),
    path("", home, name="home"),

]