from django.urls import path
from .views import upload_file_view , view_detail, view_delete

app_name = 'io_csv_plats_app'

urlpatterns = [
    path('', upload_file_view, name='upload-view'),
    path('go/<int:id>', view_detail, name='detail-view'),
    path('delete/<int:id>', view_delete, name='delete-view'),

]