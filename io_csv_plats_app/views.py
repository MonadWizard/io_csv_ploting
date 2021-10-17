from django.shortcuts import redirect, render
from .forms import CSVsModelForm
from .models import CSVs
import pandas as pd
import numpy as np
import random
import os


# Create your views here.



def upload_file_view(request):
    if request.method == 'POST':
        upload_csv = request.FILES.getlist('file_name')

        for csvs in upload_csv:
            CSVs.objects.create(file_name=csvs)
        
        return redirect('/')

    upload_csv = CSVs.objects.all()

    return render(request, 'upload_csvs/upload.html', {'upload_csv': upload_csv})



def view_delete(request, id):
    csvs = CSVs.objects.get(id=id)
    print('file name ::: ',type(csvs.file_name),csvs.file_name)
    # os.remove(csvs.file_name)
    # print("Done")
    

    csvs.delete()
    return redirect('/')


def view_detail(request, id):
    csvs = CSVs.objects.get(id=id)
    # print('file name ::: ',csvs.file_name)
    # pick X and y value no need
    # if request.POST:
    #     X=request.POST['inputField_x']
    #     y=request.POST['inputField_y']
    #     print(X,type(X))
    #     print(y, type(y))

    global data
    data = pd.read_csv(csvs.file_name)
    data = data.replace(r'^\s*$', np.nan, regex=True)   # replace empty data to Nan
    data = data.dropna()   # drop Nan column

    num_data = data.select_dtypes(include=np.number)  #take only numeric columns
    # print(num_data.head())
    random_columns = num_data.sample(n=2, axis='columns', random_state=random.randint(1, 10))
    # print(random_columns.head())
    first_column = random_columns.iloc[:, 0].to_list()
    # print(first_column)
    second_column = random_columns.iloc[:, 1].tolist()
    # print(len(second_column))
    last_column = data.iloc[:,-1].tolist()

    # print(type(last_column), last_column)

    context = {
        'csvs': csvs,
        'first_column': first_column,
        'second_column': second_column,
        'last_column':last_column,

    }

    return render(request, 'detail_csvs/csv_view.html', context)



