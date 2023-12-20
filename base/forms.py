from django.forms import ModelForm
from .models import Company, Customer, Tyre, Order

class New_CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['name'] 

class New_CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class New_TyreForm(ModelForm):
    class Meta:
        model = Tyre
        fields = '__all__'

class Update_TyreForm(ModelForm):
    class Meta:
        model = Tyre
        fields = ['Quantity_total','Quantity_sold']

class Update_CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['mobile_number', 'Email']        

class Order_New(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
    # def save(self, commit=True):
    #     order = super().save(commit=False)

    #     # Generate and save the QR code
    #     order.qr_code = order.generate_qr_code()

    #     if commit:
    #         order.save()

    #     return order