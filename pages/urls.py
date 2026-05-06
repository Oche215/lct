from django.urls import path
from .views import home, chart_data, chart_view, chart_page, import_data, sales_chart_data, sales_chart_month_total_data

urlpatterns = [
    path('api/sales-mon-total-data/', sales_chart_month_total_data, name='sales_mon_tot'),
    path('api/sales-chart-data/', sales_chart_data, name='sales_chart-data'),

    path('import/', import_data, name='import'),
    path("chart-page/", chart_page, name="chart-page"),
    path('chart-data/', chart_data, name='chart_data'),
    path('chart-view/', chart_view, name='chart_view'),
    path("", home, name="home"),

]