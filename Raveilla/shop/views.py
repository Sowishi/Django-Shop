from django.shortcuts import render, HttpResponse, get_object_or_404
from django.shortcuts import redirect
from .models import Products, WomenProducts, MensProducts, KidsProducts, Cart
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout



def home(request):
    print(request.user.username)
    print(request.user, request.user.is_authenticated)
    data = Products.objects.all()    
    if request.method == "POST":
        title = request.POST.get("title")
        price = request.POST.get("price")
        description = request.POST.get("description")
        image = request.POST.get("image")
        toAdd = Cart(title=title, price=price, description=description, image=image)
        toAdd.save()

    return render(request, "home.html", {"products": data, "username": request.user.username})
def women(request):
    data = WomenProducts.objects.all()
    if request.method == "POST":
        title = request.POST.get("title")
        price = request.POST.get("price")
        description = request.POST.get("description")
        image = request.POST.get("image")
        toAdd = Cart(title=title, price=price, description=description, image=image)
        toAdd.save()
    return render(request, "women.html", {"products": data})
def men(request):
    data = MensProducts.objects.all()
    if request.method == "POST":
        title = request.POST.get("title")
        price = request.POST.get("price")
        description = request.POST.get("description")
        image = request.POST.get("image")
        toAdd = Cart(title=title, price=price, description=description, image=image)
        toAdd.save()
    return render(request, "men.html", {"products": data})
def kids(request):
    data = KidsProducts.objects.all()
    if request.method == "POST":
        title = request.POST.get("title")
        price = request.POST.get("price")
        description = request.POST.get("description")
        image = request.POST.get("image")
        toAdd = Cart(title=title, price=price, description=description, image=image)
        toAdd.save()
    return render(request, "kids.html", {"products": data})
def cart(request):
    if request.method == "POST":
        title = request.POST.get("title")
        data = get_object_or_404(Cart, title=title)
        data.delete()
        print(data)

    data = Cart.objects.all()
    return render(request, "cart.html", {"products": data})

def login(request):
    if request.method == "POST":
        password = request.POST.get("password")
        username = request.POST.get("username")
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            return redirect("home")
        else:
            return render(request, "login.html", {"error": True})
    return render(request, "login.html")


def register(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        username = request.POST.get("username")
        user = User.objects.create_user(username, email, password)
        user.save()
        return redirect("login")
    return render(request, "register.html")

def logoutUser(request):
    logout(request)
    return redirect("home")