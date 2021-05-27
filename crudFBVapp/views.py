from django.shortcuts import render,redirect
from crudFBVapp.models import Employee
from crudFBVapp.forms import EmployeeForm
# Create your views here.
def retrieve_view(request):
    employees=Employee.objects.all()
    return render(request,'tempapp/index.html',{'emppass':employees})




def create_view(request):
    form= EmployeeForm()

    #after filling form next 5 lines will execute
    if request.method=='POST':
        form= EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'tempapp/create.html',{'form':form})
