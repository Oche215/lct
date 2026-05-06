from django.shortcuts import render
from django.http import JsonResponse
from .models import Product, Sales, Inventory, SampleSales
from .forms import ContactUsForm, SalesForm, UploadForm
from django.contrib import messages
from django.db.models import Sum
from django.db.models.functions import TruncMonth

from tablib import Dataset
from .resources import SalesResources


# Create your views here.
def home(request):
    form = ContactUsForm()
    eform = ContactUsForm()
    if request.method == 'POST':
        form = ContactUsForm(request.POST, )
        if form.is_valid():
            form.save()
            messages.success(request, 'Your messages was sent successfully!')
            return render(request, 'home.html', {'form': eform })

        else:
            return render(request, 'home.html', {'form': form})

    return render(request, 'home.html', {'form': form})


def chart_data(request):
    labels = []
    data = []

    for product in Product.objects.all():
        labels.append(product.name)
        data.append(float(product.stock))

    return JsonResponse({'labels': labels, 'data': data})

def chart_view(request):
    return render(request, 'chart.html', {})


def import_data(request):
    form = UploadForm()

    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            uploaded_file = form.cleaned_data['file']

            # 1. Validate file presence
            if not uploaded_file:
                messages.error(request, "No file uploaded.")
                return render(request, 'dashboard/dataform.html', {'form': form})

            # 2. Validate file extension
            valid_extensions = ('.xlsx', '.xls')
            if not uploaded_file.name.lower().endswith(valid_extensions):
                messages.error(request, "Invalid file format. Please upload an Excel file.")
                return render(request, 'dashboard/dataform.html', {'form': form})

            # 3. Load dataset
            try:
                dataset = Dataset()
                file_format = 'xlsx' if uploaded_file.name.lower().endswith('.xlsx') else 'xls'
                imported_data = dataset.load(uploaded_file.read(), format=file_format)

                # 4. Determine target model and mapping
                if 'inventory_submit' in request.POST:
                    _process_inventory(imported_data)
                elif 'sales_submit' in request.POST:
                    _process_sales(imported_data)
                elif 'sample_sales_submit' in request.POST:
                    _process_sample_sales(imported_data)
                else:
                    messages.error(request, "No valid action specified.")
                    return render(request, 'dashboard/dataform.html', {'form': form})

                messages.success(request, "Data imported successfully!")

            except Exception as e:
                messages.error(request, f"Error importing data: {e}")

    return render(request, 'dashboard/dataform.html', {'form': form})


def _process_inventory(imported_data):
    for row in imported_data:
        Inventory.objects.update_or_create(
            id=row[0],  # Assuming first column is ID
            defaults={
                'product_code': row[1],
                'name': row[2],
                'initial_stock': row[3],
                'stock_in': row[4],
                'stock_sold': row[5],
                'available_stock': row[6],
                'unit_price': row[7],
                'total_amount': row[8],
            }
        )


def _process_sales(imported_data):
    for row in imported_data:
        Sales.objects.update_or_create(
            id=row[0],  # Assuming first column is ID
            defaults={
                'order_date': row[1],
                'region': row[2],
                'manager': row[3],
                'salesman': row[4],
                'product': row[5],
                'unit': row[6],
                'price': row[7],
                'amount': row[8]
            },
        )


def _process_sample_sales(imported_data):
    for row in imported_data:
        SampleSales.objects.update_or_create(
            id=row[0],  # Assuming first column is ID
            defaults={
                'order_no': row[1],
                'order_date': row[2],
                'customer_name': row[3],
                'ship_date': row[4],
                'price': row[5],
                'qty': row[6],
                'tax': row[7],
                'total': row[8]
            },
        )


def chart_page(request):

    sales = SampleSales.objects.all().order_by('order_date')

    return render(request, 'dashboard/chart.html', {'sales': sales})

def sales_chart_data(request):
    # Fetch data from database
    data = SampleSales.objects.all().order_by('order_date')
    labels = [entry.order_date.strftime('%Y-%m-%d') for entry in data]
    values = [entry.total for entry in data]

    return JsonResponse({'labels': labels, 'values': values})

def sales_chart_month_total_data(request):
    try:
        # Aggregate sales totals by month
        sales_data = (
            SampleSales.objects
            .annotate(month=TruncMonth('order_date'))  # Extract month
            .values('month')
            .annotate(total_sales=Sum('total'))       # Sum totals per month
            .order_by('month')                        # Chronological order
        )

        # Prepare labels and values
        labels = [entry['month'].strftime('%b') for entry in sales_data]
        values = [float(entry['total_sales']) for entry in sales_data]

        return JsonResponse({'labels': labels, 'values': values})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
