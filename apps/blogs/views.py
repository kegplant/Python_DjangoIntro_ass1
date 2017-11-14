from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
    context={
        'email': 'blog@gmail.com',
        'name': 'mike'
    }
    response='Hello WorldDDDD!!!!'
    return render(request,'blogs/index.html',context)
def create(request):
    response="f-off!"
    return HttpResponse(response)
def new(request):
    response='placeholder to display a new form to create a new blog'
    return HttpResponse(response)
def create(request):
    response='placeholder to display a new form to create a new blog'
    return redirect('/')
def show(request,number):
    response='placeholder to display a new form to create a new blog'
    return HttpResponse('show method '+number)
def edit(response,number):
    return HttpResponse('placeholder to edit blog '+number)
def destroy(response,number):
    return redirect('/')