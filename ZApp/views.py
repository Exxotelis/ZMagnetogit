from django.shortcuts import render, redirect
from .forms import ImageUploadForm, StickerDesignForm
from .models import StickerDesign, ImageUpload
from django.contrib import messages

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # Here, you can save the email to your database, send a confirmation email, etc.
        
        # Add a message to confirm subscription
        messages.success(request, "Thank you for subscribing!")
        return redirect('home')  # Redirect to home or any other page
    
    return render(request, 'ZApp/subscribe.html')

def home(request):
    return render(request, "ZApp/home.html")  # Render the home template

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_upload = form.save()  # Save the form and get the image instance
            return render(request, 'ZApp/upload_success.html', {'image': image_upload.image})  # Pass the image to the success page
    else:
        form = ImageUploadForm()
    return render(request, 'ZApp/upload_image.html', {'form': form})

def upload_design(request):
    if request.method == 'POST':
        form = StickerDesignForm(request.POST, request.FILES)
        if form.is_valid():
            sticker = form.save(commit=False)
            sticker.user = request.user  # Ensure user is authenticated before assigning
            sticker.save()
            return redirect('upload_success')
    else:
        form = StickerDesignForm()
    return render(request, 'ZApp/upload_design.html', {'form': form})

def upload_success(request):
    return render(request, 'ZApp/upload_success.html')  # Ensure this template path is correct

def view_designs(request):
    designs = StickerDesign.objects.all()
    return render(request, 'ZApp/view_designs.html', {'designs': designs})

def about(request):
    return render(request, 'ZApp/about.html')

def community(request):
    return render(request, 'ZApp/community.html')

def jobs(request):
    return render(request, 'ZApp/jobs.html')

def shipping(request):
    return render(request, 'ZApp/shipping.html')

def contact(request):
    return render(request, 'ZApp/contact.html')

def search(request):
    return render(request, 'ZApp/search.html')

def privacy_policy(request):
    return render(request, 'ZApp/privacy_policy.html')

def lookbook(request):
    return render(request, 'ZApp/lookbook.html')

def shipping_delivery(request):
    return render(request, 'ZApp/shipping_delivery.html')

def gallery(request):
    sticker_designs = StickerDesign.objects.all()  # Fetch all sticker designs
    image_uploads = ImageUpload.objects.all()       # Fetch all uploaded images


    return render(request, 'ZApp/gallery.html', {
        'sticker_designs': sticker_designs,
        'image_uploads': image_uploads,
    })

def terms_conditions(request):
    return render(request, 'ZApp/terms_conditions.html')

def how_it_works(request):
    return render(request, 'ZApp/how_it_works.html')