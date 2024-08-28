# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Country,Customer, Review, ShoeCleaningService, Contact, Question, Answer, TravelReview, Blog, MediaReview, MediaContent, laundryReview, StudyReview, Contact, TeamMember, Education, ContentBO
from django.shortcuts import render, get_object_or_404

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact = Contact(name=name, email=email, message=message)
        contact.save()

        messages.success(request, 'Thank you for getting in touch!')
        return redirect('home')
    team_members = TeamMember.objects.all()
    return render(request, 'home.html', {'team_members': team_members})

def work_page(request):
    latest_reviews = TravelReview.objects.all().order_by('-id')[:3]
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact = Contact(name=name, email=email, message=message)
        contact.save()

        messages.success(request, 'Thank you for getting in touch!')
        return redirect('work_page')

    return render(request, 'work.html', {'reviews': latest_reviews})

def study_page(request):
    latest_reviews = StudyReview.objects.all().order_by('-id')[:3]
    content_boxes = ContentBO.objects.all()  # Ensure the model name is correct
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact = Contact(name=name, email=email, message=message)
        contact.save()
        
        messages.success(request, 'Thank you for getting in touch!')
        return redirect('study_page')
    abroad_educations = Education.objects.filter(education_type='abroad')
    distance_educations = Education.objects.filter(education_type='distance')
    domestic_educations = Education.objects.filter(education_type='domestic')

    context = {
        'reviews': latest_reviews,
        'abroad_educations': abroad_educations,
        'distance_educations': distance_educations,
        'domestic_educations': domestic_educations,
        "content_boxes": content_boxes
    }
    return render(request, 'study.html', context)

def travel_page(request):
    countries = Country.objects.all()
    reviews = Review.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact = Contact(name=name, email=email, message=message)
        contact.save()

        messages.success(request, 'Thank you for getting in touch!')
        return redirect('travel_page')

    return render(request, 'travel.html', {'countries': countries, 'reviews': reviews})

# def health_page(request):
#     latest_reviews = TravelReview.objects.all().order_by('-id')[:3]
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')

#         contact = Contact(name=name, email=email, message=message)
#         contact.save()

#         messages.success(request, 'Thank you for getting in touch!')
#         return redirect('health_page')

#     return render(request, 'health.html', {'reviews': latest_reviews})

def health_page(request):
    latest_reviews = TravelReview.objects.all().order_by('-id')[:3]
    questions = Question.objects.all()

    if request.method == 'POST':
        # Handle contact form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact = Contact(name=name, email=email, message=message)
        contact.save()

        messages.success(request, 'Thank you for getting in touch!')
        return redirect('health_page')

    return render(request, 'health.html', {'reviews': latest_reviews, 'questions': questions})

def save_answers(request):
    questions = Question.objects.all()
    
    if request.method == 'POST':
        # Handle question-answer form submission
        for question in questions:
            answer_text = request.POST.get(f'answer_{question.id}')
            if answer_text:
                Answer.objects.create(question=question, answer_text=answer_text)

        messages.success(request, 'Your answers have been submitted successfully!')
        return redirect('health_page')

    return redirect('health_page')


def media_page(request):
    # Assuming MediaReview model exists, otherwise remove this line
    latest_reviews = MediaReview.objects.all().order_by('-id')[:3]
    blogs = Blog.objects.all()
    media_contents = MediaContent.objects.all()
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact = Contact(name=name, email=email, message=message)
        contact.save()

        messages.success(request, 'Thank you for getting in touch!')
        return redirect('media_page')

    return render(request, 'media.html', {'reviews': latest_reviews, 'blogs': blogs, 'media_contents': media_contents})


def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    media_contents = blog.media_contents.all()
    return render(request, 'blog_detail.html', {'blog': blog, 'media_contents': media_contents})



def shoes_laundry_page(request):
    latest_reviews = laundryReview.objects.all().order_by('-id')[:3]
    services = ShoeCleaningService.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact = Contact(name=name, email=email, message=message)
        contact.save()

        messages.success(request, 'Thank you for getting in touch!')
        return redirect('shoes_laundry_page')

    return render(request, 'shoes_laundry.html', {'reviews': latest_reviews, 'services': services})




def register_customer(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')

        # Create a new customer record
        customer = Customer(
            full_name=full_name,
            email=email,
            phone_number=phone_number,
        )
        customer.save()

        # Display a success message
        messages.success(request, 'Registration successful!')

        # Redirect to WhatsApp chat with a pre-filled message
        whatsapp_url = 'https://wa.me/917025646518?text=Hello, Sir'
        return redirect(whatsapp_url)

    return render(request, 'register.html')
