from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def user_login(request):
    if request.user.is_authenticated:
        return redirect("index")
      
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        error = False
        msg = ""

        if username == "":
            error = True
            msg += "Kullanıcı Adı Zorunlu bir alan."

        if error:    
            return render(request, "account/login.html", {"error": True, "msg": msg,})

        user = authenticate(request, username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return render(request, "account/login.html", {"error":"Username ya da Parola yanlış"})
        
    else:
       return render(request, "account/login.html")

def user_register(request):
    if request.method == "POST":
        username = request.POST.get("username") 
        email = request.POST.get("email")
        password = request.POST.get("password")
        repassword = request.POST.get("repassword")
        
        error = False
        msg = ""



        if username == "":
            error = True
            msg += "Kullanıcı Adı Zorunlu bir alan."

        if len(password) < 5:
            error = True
            msg +=   " Şifre Minimum 5 karakter olmalıdır"

        if error:    
            return render(request, "account/register.html", {"error": True, "msg": msg,})

        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request, "account/register.html", {"error": "Kullanıcı adı kullanılıyor."})
            
            
            elif User.objects.filter(email=email).exists():
                return render(request, "account/register.html", {"error": "Email hesabı kullanılıyor."})
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect("user_login")
        else:
            return render(request, "account/register.html", {"error": "Parolalar Eşleşmiyor."})
    else:
        return render(request, "account/register.html")

    
def user_logout(request):
    logout(request)
    return redirect("index")
