from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Publisher,Author,Book
# Create your views here.
def home(request):
    return HttpResponse("This is home page")

def add_some_items(request):
    p1=Publisher(name="Harsh-RG",addr="Chiikalasandra",city="Bengaluru")
    p1.save()

    p2=Publisher(name="AlanGeorge",addr="Kodipalya",city="Bengaluru")
    p2.save()

    p3=Publisher(name="EshwarK",addr="KalenaAgrahara",city="Bengaluru")
    p3.save()
    publisher_list=Publisher.objects.all()
    print(publisher_list)

    a1=Author(first_name="Harsh",last_name="RG")
    a1.save()
    a2=Author(first_name="Alan",last_name="George")
    a2.save()
    a3=Author(first_name="Eshwar",last_name="K")
    a3.save()

    b1=Book(title="War and Piece",author="Harsh")
    b1.save()
    b2=Book(title="Annie Karenina",author="AlanGeorge")
    b2.save()
    b3=Book(title="Naana Prethiya Kathe",author="Eshwark")
    b3.save()
    publisher_list=Publisher.objects.all()
    author_list=Author.objects.all()
    book_list=Book.objects.all()
    context={"publisher":publisher_list,"author":author_list,"books":book_list}
    return render(request,"ListsAdded.html",context)
