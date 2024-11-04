from django import forms
from .models import ImageUpload, StickerDesign
from django.core.exceptions import ValidationError

def validate_image(image):
    if image.size > 2 * 1024 * 1024:  # Limit file size to 2MB
        raise ValidationError('Image file too large (maximum 2MB)')

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUpload
        fields = ['title', 'description', 'image']
    
    def clean_image(self):
        image = self.cleaned_data.get('image')
        validate_image(image)
        return image


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUpload
        fields = ['title', 'description', 'image']

class StickerDesignForm(forms.ModelForm):
    class Meta:
        model = StickerDesign
        fields = ['title', 'description', 'image']