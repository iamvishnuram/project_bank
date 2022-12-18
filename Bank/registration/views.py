from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth
from . forms import PersonCreationForm
from . models import Person, District, City

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('user')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method == 'POST': 
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "User already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already Exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password,email=email)
                user.save()
                return redirect('login')
                
        else:
                messages.info(request, 'Password Mismatch')
                return redirect('register')
        return redirect('/')
    
    return render(request, 'register.html')

def user(request):
    return render(request, 'account.html')

def success(request):
    return render(request, 'success.html')



def join(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
        else:
            messages.info(request, 'Error Occured')
    return render(request, 'join.html', {'form': form})

# AJAX
def load_cities(request):
    district_id = request.GET.get('district_id')
    branch = City.objects.filter(district_id=district_id).all()
    return render(request, 'city_dropdown_list_options.html', {'branch': branch})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)



