from django import forms
from .models import UploadedPDF

class PDFUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedPDF
        fields = ['file']

class RentalAgreementForm(forms.Form):
    landlord_name = forms.CharField(label="Landlord Name")
    tenant_name = forms.CharField(label="Tenant Name")
    property_address = forms.CharField(widget=forms.Textarea)
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    rent_amount = forms.DecimalField(decimal_places=2)
    agreement_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

class DivorceAgreementForm(forms.Form):
    spouse_one = forms.CharField()
    spouse_two = forms.CharField()
    divorce_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    settlement_details = forms.CharField(widget=forms.Textarea)

class LandAgreementForm(forms.Form):
    seller_name = forms.CharField()
    buyer_name = forms.CharField()
    land_location = forms.CharField()
    sale_amount = forms.DecimalField()
    sale_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))