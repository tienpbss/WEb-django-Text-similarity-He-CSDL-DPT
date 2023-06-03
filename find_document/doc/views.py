from django.shortcuts import render, redirect
from django.http import HttpResponse


from .forms import FileForm
from .pre_text import clean_text
from .find_file import find_similarity
from .find_file2 import find_similarity2

import fitz
import os

# Create your views here.

def index(request):
    return render(request, 'doc/home.html')

def getFindPage(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if not form.is_valid():
            error_message = "Please upload a valid PDF file."
            form = FileForm()
            return render(request, 'doc/find.html', {
                'form': form,
                'error_message': error_message,
            })
        file = form.cleaned_data['file']
        pdf_data = file.read()
        pdf_document = fitz.open(stream=pdf_data, filetype="pdf")
        text = ""

        for page in pdf_document:
            text += page.get_text()
        text = clean_text(text)

        form = FileForm()
        files = find_similarity(text)
        return render(request, 'doc/find.html', {
            'files': files,
            'form': form,
            'text': text,
        })
    else:
        form = FileForm()
    return render(request, 'doc/find.html', {
        "form": form
    })



def pdf_view(request, file_name):
    file_path = os.path.join("D:\\Document-CSDLDPT", file_name)
    with open(file_path, 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=mypdf.pdf'
        return response