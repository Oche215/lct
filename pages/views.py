from django.shortcuts import render
from django.http import JsonResponse
from .models import Product, Sales
from .forms import ContactUsForm, SalesForm, UploadForm
from django.contrib import messages

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


def import_inventory(request):
    form = UploadForm()
    if request.method == 'POST':
        # Pass both POST data and FILES to the form
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Replace 'file_field' with the actual field name in your form
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

            try:
                # 3. Load dataset
                dataset = Dataset()
                file = 'xlsx' if uploaded_file.name.lower().endswith('.xlsx') else 'xls'
                imported_data = dataset.load(uploaded_file.read(), format=file)

                # 4. Process rows
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
                            'amount': row[8],
                        }
                    )

                messages.success(request, "Data imported successfully!")

            except Exception as e:
                messages.error(request, f"Error importing data: {e}")
                return render(request, 'dashboard/dataform.html', {'form': form})

    return render(request, 'dashboard/dataform.html', {'form': form})





def import_excel_data(request):
    form = UploadForm()

    if request.method == 'POST':



        uploaded_file = request.FILES.get('file')

        # 1. Validate file presence
        if not uploaded_file:
            messages.error(request, "No file uploaded.")
            return render(request, 'dashboard/dataform.html', {'form': form})

        # 2. Validate file extension
        valid_extensions = ('.xlsx', '.xls')
        if not uploaded_file.name.lower().endswith(valid_extensions):
            messages.error(request, "Invalid file format. Please upload an Excel file.")
            return render(request, 'dashboard/dataform.html', {'form': form})

        if 'sales_submit' in request.POST:
            try:
                # 3. Load dataset
                dataset = Dataset()
                file_format = 'xlsx' if uploaded_file.name.lower().endswith('.xlsx') else 'xls'
                imported_data = dataset.load(uploaded_file.read(), format=file_format)

                # 4. Process rows
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
                            'amount': row[8],
                        }
                    )

                messages.success(request, "Data imported successfully!")

            except Exception as e:
                messages.error(request, f"Error importing data: {e}")

        else:
            if 'inventory_submit' in request.POST:
                try:
                    # 3. Load dataset
                    dataset = Dataset()
                    file_format = 'xlsx' if uploaded_file.name.lower().endswith('.xlsx') else 'xls'
                    imported_data = dataset.load(uploaded_file.read(), format=file_format)

                    # 4. Process rows
                    for row in imported_data:
                        Sales.objects.update_or_create(
                            product_id=row[0],  # Assuming first column is ID
                            defaults={
                                'name': row[1],
                                'initial_stock': row[2],
                                'stock_in': row[3],
                                'stock_sold': row[4],
                                'available_stock': row[5],
                                'unit_price': row[6],
                                'total_amount': row[7],
                            }
                        )


                    messages.success(request, "Data imported successfully!")

                except Exception as e:
                    messages.error(request, f"Error importing data: {e}")

    return render(request, 'dashboard/dataform.html', {'form': form})
