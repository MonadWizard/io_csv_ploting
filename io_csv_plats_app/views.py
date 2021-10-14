from django.shortcuts import redirect, render
from .forms import CSVsModelForm
from .models import CSVs
# Create your views here.


def upload_file_view(request):
    if request.method == 'POST':
        upload_csv = request.FILES.getlist('file_name')
        for csvs in upload_csv:
            CSVs.objects.create(file_name=csvs)
    upload_csv = CSVs.objects.all()

    return render(request, 'upload_csvs/upload.html', {'upload_csv': upload_csv})



def view_delete(request, id):
    csvs = CSVs.objects.get(id=id)
    csvs.delete()
    return redirect('/')


def view_detail(request, id):
    csvs = CSVs.objects.get(id=id)
    
    return render(request, 'Detail_csvs/detail_csvs.html', {'csvs':csvs})
