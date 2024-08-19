from datetime import date
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404, HttpResponseNotFound
from django.urls import reverse
from .models import Program, Category


data={
    "Boxing":"Boks kategorisine ait antrenman programları",
    "Kickboxing":"Kickboks kategorisine ait antrenman programları",
    "Muay-Thai":" Muay-Thai kategorisine ait antrenman programları"
}

db = {
    "programlar": [ 
        {
            "title":"Boks kursu",
            "description":"Boks, iki kişinin boks hakemi gözetiminde karşılıklı yumruklaştıkları ve birbirlerini nakavtla ya da puanla yenmeye çalıştıkları spor müsabakasıdır.",
            "imageUrl":"1.jpg",
            "slug": "boks-kursu",
            "date": date(2024,8,10),
            "isAsctive": True
        },
        {
            "title":"Kickboks kursu",
            "description":"Kick boks, yumruk, tekme, diz ve sınırlı clinch uygulamalarının bir araya getirilmesiyle oluşturulmuş eklektik bir yakın dövüş stili ve dövüş sporudur. ",
            "imageUrl":"2.jpg",
            "slug": "kickboks-kursu",
            "date": date(2024,7,10),
            "isActive": True
        },
        {
            "title":"Thai boks kursu",
            "description":"Muay-Thai ya da bir diğer adıyla Thai boks, kickboks' un diz ve dirsek eklenmiş ve daha sert biçime bürünmüş halidir.",
            "imageUrl":"3.jpg",
            "slug": "thai-boks-kursu",
            "date": date(2024,6,10),
            "isActive": True
        },

    ],
    "categories": [
        { "id":1,"name": "Boxing","slug": "Boxing",},
        { "id":2,"name":"Kickboxing","slug":"Kickboxing"},
        { "id":3,"name":"Muay-Thai","slug":"Muay-Thai"},
        
       ]


}


def index(request):
    programlar = Program.objects.filter(isActive=1)
    kategoriler = Category.objects.all()
    

    return render(request, 'programlar/index.html',{
        'categories': kategoriler,
        'programlar': programlar
    })

def details(request, slug):
    program = get_object_or_404(Program, slug=slug)

    context={
        'program': program
    }
    return render(request, 'programlar/details.html',context)


def getProgramlarByCategory(request, slug):
    programlar = Program.objects.filter(category__slug=slug, isActive=True)
    kategoriler = Category.objects.all()

    return render(request, 'programlar/index.html', {
        'categories': kategoriler,
        'programlar': programlar,
        'seciliKategori': slug
    })

     

