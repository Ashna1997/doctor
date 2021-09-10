from django.shortcuts import render,redirect
from app.models import doctor1,patient1,sp1
from django.core.files.storage import FileSystemStorage
# Create your views here.


def index(request):
    return render(request,"index.html")
def doctor(request):
    st = sp1.objects.all()
    return render(request,"doctor.html", {'stud':st})
def insert1(request):
    s=doctor1()
    s.name=request.POST.get("name")
    s.special = request.POST.get("sw")
    s.hospital = request.POST.get("hospital")
    s.salary = request.POST.get("salary")
    photo=request.FILES['photo']
    fs=FileSystemStorage()
    filename=fs.save(photo.name,photo)
    uploaded_file_url=fs.url(filename)
    s.photo=uploaded_file_url
    s.save()
    return render(request, 'doctor.html')
def patient(request):
    return render(request,"patient.html")
def insert2(request):
    s=patient1()
    s.name=request.POST.get("name")
    s.doctor=request.POST.get("doctor")
    s.bill = request.POST.get("bill")
    s.hospital = request.POST.get("hospital")

    photo = request.FILES['photo']
    fs = FileSystemStorage()
    filename = fs.save(photo.name, photo)
    uploaded_file_url = fs.url(filename)
    s.photo = uploaded_file_url
    s.save()
    return redirect("/patient")
def specialization(request):
    return render(request,"specialization.html")
def insert3(request):
    s=sp1()
    s.category_id=request.POST.get("categoryid")
    s.special=request.POST.get("special")
    s.save()
    return redirect("/specialization")

def viewdoctor(request):

    s = doctor1.objects.all()
    return render(request, 'viewdoctor.html', {'stud': s})
def viewpatient(request):

    s = patient1.objects.all()
    return render(request, 'viewpatient.html', {'stud': s})
def gsalary(request):
    s =doctor1.objects.filter(salary__gte=10000)
    return render(request,'gsalary.html',{'stud':s})
def search(request):
    st = sp1.objects.all()
    return render(request, 'search.html', {'stud': st})


def view_special(request):
    s = request.POST.get("s1")
    st = doctor1.objects.filter(special=s)
    return render(request, 'viewspecial.html', {'stud1': st})
