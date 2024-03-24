from django.shortcuts import render,redirect
from django.http import HttpResponse
from users.models import Profile
from users.forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from coordinator.decorators import coordinator_required


def homepage(request):
    
    return render(request, 'home.html')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = UserLoginForm()
    return render(request, 'user_login.html', {'form': form})



def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print("Form is valid. Proceeding with registration.")
            try:
                user = User.objects.create_user(username=username, email=email, password=password)
                print("User created successfully:", user.username)  
                messages.success(request, 'Registration successful. Please log in.')
                return redirect('user_login')
            except Exception as e:
                print("Error creating user:", e)
                messages.error(request, 'An error occurred during registration. Please try again later.')
        else:
            print("Form is invalid. Errors:", form.errors)
    else:
        form = UserRegistrationForm()
    return render(request, 'user_register.html', {'form': form})


 

def about_page(request):
    # Placeholder logic for the About page view
    context = {
        'about_content': 'Learn more about our mission and goals here.'
    }
    return render(request, 'about.html', context)

def contact_page(request):
    # Placeholder logic for the Contact page view
    context = {
        'contact_info': {
            'email': 'info@example.com',
            'phone_number': '123-456-7890',
            'address': '123 Main Street, City, Country'
        }
    }
    return render(request, 'contact.html', context)

@login_required
def contact_submit_view(request):
    # Placeholder logic for handling form submission
    if request.method == 'POST':
        # Process the form data
        return HttpResponse('Form submitted successfully!')
    else:
        # Handle GET request (if needed)
        return HttpResponse('Invalid request method')


def faq_page(request):
    # Placeholder logic for the FAQ page view
    faq_items = [
        {'question': 'How can I adopt a pet?', 'answer': 'You can browse available pets on our website and contact us for adoption details.'},
        {'question': 'What are the adoption fees?', 'answer': 'Adoption fees vary depending on the type of pet and other factors. Please contact us for more information.'},
        {'question': 'Can I volunteer at your shelter?', 'answer': 'Yes, we welcome volunteers! Please visit our volunteer page for more information.'},
    ]
    context = {
        'faq_items': faq_items
    }
    return render(request, 'faq.html', context)

def adoption_event(request):
    #
    context = {
        'events': 'events of the  pet adoption platform!'
    }
    return render(request, 'adoption_events.html', context)



@login_required
def profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    adoption_status = profile.adoption_status
    return render(request, 'profile.html', {'adoption_status': adoption_status})

@coordinator_required
def coordinator_dashboard(request):
    # Logic to render the coordinator dashboard template
    return render(request, 'coordinator_home.html')