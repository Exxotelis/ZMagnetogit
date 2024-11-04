from django.contrib import admin
from .models import ImageUpload

@admin.register(ImageUpload)
class ImageUploadAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')  # Fields to display in the list view
    search_fields = ('title',)          # Search functionality by title

# Alternatively, you can use the following code to register the model
# admin.site.register(ImageUpload)
