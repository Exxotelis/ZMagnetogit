from django.urls import path
from .views import home, upload_image, upload_design, upload_success, view_designs, subscribe, about, community, jobs, shipping, contact, search, privacy_policy, lookbook, shipping_delivery, gallery, terms_conditions, how_it_works

urlpatterns = [
    path('', home, name='home'),  # Home page
    path('upload/image/', upload_image, name='upload_image'),  # Endpoint for uploading images
    path('upload/design/', upload_design, name='upload_design'),  # Endpoint for uploading designs
    path('upload/success/', upload_success, name='upload_success'),  # Success page after upload
    path('designs/', view_designs, name='view_designs'),  # Page to view all designs
    path('subscribe/', subscribe, name='subscribe'),
    path('about/', about, name='about'),
    path('community/', community, name='community'),
    path('jobs/', jobs, name='jobs'),
    path('shipping/', shipping, name='shipping'),
    path('contact/', contact, name='contact'),
    path('search/', search, name='search'),
    path('privacy-policy/', privacy_policy, name='privacy_policy'),
    path('lookbook/', lookbook, name='lookbook'),
    path('shipping-delivery/', shipping_delivery, name='shipping_delivery'),
    path('gallery/', gallery, name='gallery'),
    path('terms-conditions/', terms_conditions, name='terms_conditions'),
    path('how_it_works/', how_it_works, name='how_it_works'),
]
