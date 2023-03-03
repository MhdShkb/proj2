from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

from app.models import Book, Login, district, Area, BookCatogeory, Feedback, Payment, creditcard


class Bookform(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'description', 'type', 'image','price')


class CustomUserform(UserCreationForm):
    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2', 'name', 'phone', 'email', 'address', 'image',)


class Dealerform(UserCreationForm):
    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2', 'name', 'phone', 'email', 'address','area',)


class districtform(forms.ModelForm):
    class Meta:
        model = district
        fields = ('name',)


class areaform(forms.ModelForm):
    class Meta:
        model = Area
        fields = ('district_name', 'name',)


class Catogeoryform(forms.ModelForm):
    class Meta:
        model = BookCatogeory
        fields = ('name',)

class DateInput(forms.DateInput):
    input_type = 'date'


class feedbackform(forms.ModelForm):
    date=forms.DateField(widget=DateInput)
    class Meta:
        model = Feedback
        fields = ('title','feedback','date',)

class Paymentform(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('name','bill_date','amount',)

class cardform(forms.ModelForm):
    card_no = forms.CharField(validators=[RegexValidator(regex='^.{16}$', message='Please Enter a Valid Card Number')])
    Card_cvv = forms.CharField(widget=forms.PasswordInput,validators=[RegexValidator(regex='^.3$', message='Please Enter a Valid CVV')])
    expiry_date = forms.DateField(widget=DateInput(attrs={'id': 'example-month-input'}))

    class Meta:
        model=creditcard
        fields=('card_no','Card_cvv','expiry_date',)
