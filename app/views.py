from django.shortcuts import render
import os
from django.shortcuts import HttpResponse
from django.conf import settings
from django.http import FileResponse
from dashboard.models import Products,Category
# Create your views here.



def index(request):
    
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')


def contact(request):
    return render(request,'contact.html')


def login(request):
    return render(request,'login.html')




def Projects(request):

    categories = Category.objects.all()

    category_data = {}  # Dictionary to hold products for each category

    for category in categories:
            products = Products.objects.filter(category=category)
            category_data[category.name] = products


    return render(request,'Projects.html', {'category_data': category_data})







def download_cv(request):
    cv_path = os.path.join(settings.BASE_DIR, 'D:\Personal_Projects\PortfolioWebAli\core\static\Muhammad Ali Irfan CV.pdf')  # Provide the correct path to your CV file
    cv_file = open(cv_path, 'rb')
    
    response = HttpResponse(cv_file.read(), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Muhammad Ali Irfan CV.pdf"'
    
    cv_file.close()
    
    return response


