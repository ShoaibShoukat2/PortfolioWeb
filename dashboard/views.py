from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from .models import Email,Category,Products
from django.shortcuts import redirect, get_object_or_404
# Create your views here.



def index(request):

    products = Products.objects.all()
    return render(request,'dashboard/index.html', {'products': products})


def DeleteProduct(request,product_id):
    product = Products.objects.get(pk=product_id)

    product.delete()

    return redirect('index-page')

def login(request):
    if request.method == 'POST':
        U_Name = request.POST.get('user_name')
        password = request.POST.get('password')

        user = authenticate(request, username=U_Name, password=password)

        if user is not None:
            auth_login(request, user)
            print('user login')

            request.session['user_email'] = user.email

            return redirect('/dashboard/')
        else:
            print('user not login')
            error_message = "Invalid email or password"
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'dashboard/admin.html')


    

def logout(request):

    request.session.flush()

    context = {'message': 'Successfully logged out'}

    return render(request,'index.html',context)
    



def contact(request):
    if request.method == 'POST':
        # Get form data using request.POST.get
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        text = request.POST.get('text')

        if email and subject and text:
            # Check if email already exists
            if Email.objects.filter(email=email).exists():
                context = {
                    'caugtion': 'You have already submitted the form. Please wait for a reply.'
                }
                return render(request, 'contact.html', context)

            # Check if text has at least 90 words
            if len(text.split()) < 90:
                context = {
                    'error_message': 'The message must be at least 90 words.'
                }
                return render(request, 'contact.html', context)

            email_obj = Email(email=email, subject=subject, text=text)
            email_obj.save()

            context = {
                'message': 'Form submitted successfully'
            }
            return render(request, 'contact.html', context)
        else:
            print('error called')
            context = {
                'error_message': 'Please fill all fields'
            }
            return render(request, 'contact.html', context)
    else:
        return render(request, 'contact.html')



def users(request):
    # Query all Email objects from the database
    emails = Email.objects.all()

    return render(request,'dashboard/users.html',{'emails': emails})



def delete_user(request,email_id):

    email = Email.objects.get(id=email_id)

    if email:
        email.delete()
        emails = Email.objects.all()
        return render(request,'dashboard/users.html',{'emails': emails})

        

    emails = Email.objects.all()

    return render(request,'dashboard/users.html',{'emails': emails})





def AddProducts(request):
    if request.method == 'POST':
        # Retrieve form data from POST request
        title = request.POST.get('ProjectName')
        description = request.POST.get('description')
        category_id = request.POST.get('category')
        image = request.FILES.get('image')

        # Create new Product object and save it to the database
        new_product = Products(title=title, description=description, category_id=category_id, image=image)
        new_product.save()

        messages = 'Product added successfully'

        # Redirect to a page showing all projects (adjust the URL as needed)

        return render(request,'dashboard/AddProducts.html',{'message':messages})

    # If request method is GET, render the form with category data
    categories = Category.objects.all()
    return render(request, 'dashboard/AddProducts.html', {'category_data': categories})





def AddCategory(request):
    if request.method == 'POST':
        category_name = request.POST.get('category')  # Get the category name from the POST data
        if category_name:  # Check if the category name is not empty
            category = Category(name=category_name)  # Create a new Category object
            category.save()  # Save the category directly
            return redirect('Add-Category')  # Redirect to the same page to show updated list of categories

    categories = Category.objects.all()

    return render(request, 'dashboard/AddCategory.html', {'categories': categories})



def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    return redirect('Add-Category')  





