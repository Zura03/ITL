from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import AuthorModel, BookModel, PublisherModel, ProductModel, HumanModel
from .forms import AuthorForm, BookForm, PublisherForm, ProductForm, HumanForm

def index(request):
    authors = AuthorModel.objects.all(),
    books = BookModel.objects.all()
    publishers = PublisherModel.objects.all()
    
    return render(request, 'myapp/book.html', {'books':books, 'authors':authors, 'publishers':publishers,
                                               'author_form':AuthorForm, 'book_form':BookForm, 'pub_form': PublisherForm})

def create(request):
    if request.method == 'POST':
        author_form = AuthorForm(request.POST)
        publisher_form = PublisherForm(request.POST)
        
        if author_form.is_valid() and publisher_form.is_valid():
            author_form.save(commit=False)
            publisher_form.save(commit=False)
            author_form.save()
            publisher_form.save()
         
        else:
            print('ERROR')
            print("Authors valid: ", author_form.is_valid())
            print("Publisher valid: ", publisher_form.is_valid())
            
        if not author_form.is_valid():
            return render(request, 'myapp/err.html', {'form':author_form})
        elif not publisher_form.is_valid():
            return render(request, 'myapp/err.html', {'form':publisher_form})
        
        return HttpResponseRedirect('/')

def createbook(request):
    if request.method == 'POST':
        book_form = BookForm(request.POST)
        
        if book_form.is_valid():
            book_form.save(commit=False)
            book_form.save()
            
        else:
            print('ERROR')
            print('books valid', book_form.is_valid())
            
        if not book_form.is_valid():
            return render(request, 'myapp/err.html', {'form':book_form})
        
        return HttpResponseRedirect('/')
            
#q2
    
def indexprod(req):
    prods = ProductModel.objects.all()
    return render(req, 'myapp/prod.html', {'prods': prods})

def addprod(req):
    return render(req, 'myapp/add.html', {'prod_form': ProductForm()})

def createprod(req):
    if req.method == 'POST':
        prod_form = ProductForm(req.POST)
        if prod_form.is_valid():
            prod = prod_form.save(commit=False)
            prod.save()
        else:
            print("ERROR")
    return HttpResponseRedirect('/index')

def addhuman(request):    
    return render(request, 'myapp/addhuman.html', {'hum_form': HumanForm})

def createhuman(request):
    if request.method == 'POST':
        human_form = HumanForm(request.POST)
        
        if human_form.is_valid():
            human_form.save(commit=False)
            human_form.save()
            
        else:
            print('ERROR')
    
    return HttpResponseRedirect('/update')

def update(request):
    hums = HumanModel.objects.all()
    
    return render(request, 'myapp/update.html', {'humans':hums})
            