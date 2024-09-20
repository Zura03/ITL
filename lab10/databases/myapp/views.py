from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import CategoryModel, PageModel, EmpModel
from .forms import CategoryForm, PageForm, EmpForm

def index(request):
    categories = CategoryModel.objects.all()
    pages = PageModel.objects.all()
    return render(request, 'myapp/index.html', {'cat_form':CategoryForm, 'page_form': PageForm, 'categories': categories, 'pages':pages});

def create(request):
    if request.method == "POST":
        cat_form = CategoryForm(request.POST)
        page_form = PageForm(request.POST)
        if cat_form.is_valid() and page_form.is_valid():
            cat = cat_form.save(commit=False)
            page = page_form.save(commit=False)
            if CategoryModel.objects.last():
                cat.index = CategoryModel.objects.last().index + 1
                page.index = PageModel.objects.last().index + 1
            else:
                cat.index = 1
                page.index = 1
            cat.save()
            page.save()
    return HttpResponseRedirect('/')


def home(request):
    emps = EmpModel.objects.all()
    return render(request, 'myapp/emp.html', {'emp_form': EmpForm, 'emps':emps})

def add(request):
    if request.method == 'POST':
        form = EmpForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            
    return HttpResponseRedirect('/home/')
        