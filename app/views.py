from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect

from app.forms import Bookform, CustomUserform, districtform, areaform, Catogeoryform, Dealerform, feedbackform, \
    Paymentform, cardform
from app.models import Book, Login, district, Area, BookCatogeory, Feedback, creditcard, Payment


# # Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        print(username)
        password = request.POST.get('pass')
        print(password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin_dashboard')
            elif user.is_dealer:
                return redirect('dealer_home')
            elif user.is_customer:
                return redirect('Customer_Home')
    else:
        messages.info(request, 'INVALID CREDENTIALS')
    return render(request, 'login.html')


#
def admin_dashboard(request):
    return render(request, 'Admin_Temp/index.html')


def add_Customer(request):
    form = CustomUserform()
    if request.method == 'POST':
        form = CustomUserform(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_customer = True
            user.save()
            return redirect('Home')
    return render(request, 'add_Customer.html', {'form': form})


def view_Customer(request):
    data = Login.objects.filter(is_customer=True)
    return render(request, 'Admin_Temp/view_Customer.html', {'data': data})


def edit_customer(request, id):
    data = Login.objects.get(id=id)
    form = CustomUserform(instance=data)
    if request.method == 'POST':
        form = CustomUserform(request.POST or None, request.FILES or None, instance=data)
        if form.is_valid():
            form.save()
            return redirect('view_Customer')
    return render(request, 'edit_customer.html', {'form': form})


def delete_customer(request, id):
    data = Login.objects.get(id=id)
    data.delete()
    return redirect('view_Customer')


def add_district(request):
    form = districtform()
    if request.method == 'POST':
        form = districtform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_district')
    return render(request, 'Admin_Temp/add_district.html', {'form': form})


def view_district(request):
    data = district.objects.all()
    return render(request, 'Admin_Temp/view_district.html', {'data': data})


def delete_district(request, id):
    data = district.objects.get(id=id)
    data.delete()
    return redirect('view_district')


def add_Area(request):
    form = areaform()
    if request.method == 'POST':
        form = areaform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_Area')
    return render(request, 'Admin_Temp/add_Area.html', {'form': form})


def view_Area(request):
    data = Area.objects.all()
    return render(request, 'Admin_Temp/view_Area.html', {'data': data})


def delete_Area(request, id):
    data = Area.objects.get(id=id)
    data.delete()
    return redirect('view_Area')


def adminview_Book(request):
    data = Book.objects.all()
    return render(request, 'Admin_Temp/adminview_Book.html', {'data': data})


def view_BookCatogeory(request):
    data = BookCatogeory.objects.all()
    return render(request, 'Admin_Temp/view_BookCatogery.html', {'data': data})


def add_BookCatogeory(request):
    form = Catogeoryform()
    if request.method == 'POST':
        form = Catogeoryform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_BookCatogeory')
    return render(request, 'Admin_Temp/add_BookCatogeory.html', {'form': form})


def admin_view_BookCatogeory(request):
    data = BookCatogeory.objects.all()
    return render(request, 'Dealer_Temp/admin_view_BookCatogeory.html', {'data': data})


def delete_BookCatogery(request, id):
    data = BookCatogeory.objects.get(id=id)
    data.delete()
    return redirect('view_BookCatogeory')


def view_district(request):
    data = district.objects.all()
    return render(request, 'Admin_Temp/view_district.html', {'data': data})


def add_Dealer(request):
    form = Dealerform()
    if request.method == 'POST':
        form = Dealerform(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_dealer = True
            user.save()
            return redirect('view_Dealer')
    return render(request, 'Admin_Temp/add_Dealer.html', {'form': form})


def view_Dealer(request):
    data = Login.objects.filter(is_dealer=True)
    return render(request, 'Admin_Temp/view_Dealer.html', {'data': data})


def edit_Dealer(request, id):
    data = Login.objects.get(id=id)
    form = Dealerform(instance=data)
    if request.method == 'POST':
        form = Dealerform(request.POST or None, instance=data)
        if form.is_valid():
            form.save()
            return redirect('view_Dealer')
    return render(request, 'Admin_Temp/edit_Dealer.html', {'form': form})


def delete_Dealer(request, id):
    data = Login.objects.get(id=id)
    data.delete()
    return redirect('view_Dealer')


def logout_view(request):
    logout(request)
    return redirect('Home')


#############################DEALER PAGE###############################

def dealer_home(request):
    return render(request, 'Dealer_Temp/index.html')


def create_Book(request):
    form = Bookform()
    if request.method == 'POST':
        form = Bookform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_Book')
    return render(request, 'Dealer_Temp/create_Book.html', {'form': form})


def view_Book(request):
    data = Book.objects.all()
    return render(request, 'Dealer_Temp/view_Book.html', {'data': data})


def edit_Book(request, id):
    data = Book.objects.get(id=id)
    form = Bookform(instance=data)
    if request.method == 'POST':
        form = Bookform(request.POST or None, request.FILES or None, instance=data)
        if form.is_valid():
            form.save()
            return redirect('view_Book')
    return render(request, 'Dealer_Temp/edit_Book.html', {'form': form})


def delete(request, id):
    data = Book.objects.get(id=id)
    data.delete()
    return redirect('view_Book')


def Customer_Home(request):
    return render(request, 'Customer_Temp/index.html')


def customer_view_Book(request):
    data = Book.objects.all()
    return render(request, 'Customer_Temp/customer_view_Book.html', {'data': data})


def Home(request):
    return render(request, 'index.html')


def Customer_feedback(request):
    form = feedbackform()
    if request.method == 'POST':
        form = feedbackform(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.customer = request.user
            form.save()
            return redirect('view_customer_feedback')
    return render(request, 'Customer_Temp/Customer_feedback.html', {'form': form})


def view_customer_feedback(request):
    data = Feedback.objects.filter(customer=request.user)
    return render(request, 'Customer_Temp/view_customer_feedback.html', {'data': data})


def edit_customer_feedback(request, id):
    data = Feedback.objects.get(id=id)
    form = feedbackform(instance=data)
    if request.method == 'POST':
        form = feedbackform(request.POST or None, instance=data)
        if form.is_valid():
            form.save()
            return redirect('view_customer_feedback')
    return render(request, 'Customer_Temp/edit_customer_feedback.html', {'form': form})


def delete_customer_feedback(request, id):
    data = Feedback.objects.get(id=id)
    data.delete()
    return redirect('view_customer_feedback.html')


def admin_view_customer_feedback(request):
    data = Feedback.objects.all()
    return render(request, 'Admin_Temp/admin_view_customer_feedback.html', {'data': data})


def admin_reply(request, id):
    data = Feedback.objects.get(id=id)
    if request.method == 'POST':
        Data = request.POST.get('reply')
        data.reply = Data
        data.save()
        return redirect('admin_view_customer_feedback')
    return render(request, 'Admin_Temp/admin_reply.html', {'data': data})


def bill_payment(request, name_id):
    pay = Payment.objects.filter(id=name_id).first()
    if request.method == 'POST':
        card = request.POST.get('card')
        print(card)
        cvv = request.POST.get('cvv')
        print(cvv)
        exp = request.POST.get('exp')
        print(exp)
        creditcard(card_no=card, Card_cvv=cvv, expiry_date=exp).save
        pay.status = 1
        pay.save()
        print(pay)
        messages.info(request, 'Bill Paid Successfully')
        return redirect('customer_view_Book')
    return render(request, 'Customer_Temp/bill_payment.html')


def buy_now(request, id):
    data = Book.objects.filter(id=id)
    return render(request, 'Customer_Temp/buy_now.html', {'data': data})


def bill_history(request):
    data = Payment.objects.all()
    return render(request, 'Admin_Temp/bill_history.html', {'data': data})

def customer_view_Dealer(request):
    data = Login.objects.filter(is_dealer=True)
    return render(request, 'Customer_Temp/customer_view_Dealer.html', {'data': data})

def view_Customer_profile(request):
    data = Login.objects.filter(username=request.user)
    return render(request, 'Customer_Temp/view_Customer_profile.html', {'data': data})