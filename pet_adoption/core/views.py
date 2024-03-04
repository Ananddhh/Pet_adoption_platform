from django.shortcuts import render
from django.http import HttpResponse
from  users.models import Profile
from django.contrib.auth.decorators import login_required

def homepage(request):
    #
    context = {
        'welcome_message': 'Welcome to our pet adoption platform!'
    }
    return render(request, 'home.html', context)

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