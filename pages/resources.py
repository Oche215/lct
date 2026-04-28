from import_export import resources
from .models import Sales

class SalesResources(resources.ModelResource):
    class Meta:
        model = Sales
