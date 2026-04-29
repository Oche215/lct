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


def import_excel_data(request):
    form = UploadForm()
    if request.method == 'POST':
        resource = SalesResources()
        dataset = Dataset()

        new_data = request.FILES['file']
        import_data = dataset.load(new_data.read(), format='xlsx', )

        for data in import_data:
            value = Sales(
                data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8]
            )
            value.save()

    return render(request, 'dashboard/dataform.html', {'form': form})
