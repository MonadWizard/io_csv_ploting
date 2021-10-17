from io import BytesIO
from django import template
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
import uuid
from django.conf import settings

def save_pdf(params:dict):
    template = get_template('detail_csvs/Scatter_view.html')

    html = template.render(params)
    response = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode('UTF-8')), response)
    file_name = uuid.uuid4
    # try:
    #     with open(str(settings))