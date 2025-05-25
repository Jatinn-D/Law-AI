from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # <-- this is now the homepage
    path('upload/', views.upload_pdf, name='upload_pdf'),
    path('chat/<int:pdf_id>/', views.chat_about_pdf, name='chat_pdf'),
    path('download/<int:pdf_id>/', views.download_summary, name='download_summary'),
    path('generate-documents/', views.document_selector, name='document_selector'),
    path('generate-rental/', views.generate_rental_agreement, name='generate_rental'),
    path('generate-divorce/', views.generate_divorce_agreement, name='generate_divorce'),
    path('generate-land/', views.generate_land_agreement, name='generate_land'),
    path('preview-rental/', views.preview_rental_doc, name='preview_rental'),
    path('preview-divorce/', views.preview_divorce_doc, name='preview_divorce'),
    path("preview-land/", views.preview_land_doc, name="preview_land"),
]