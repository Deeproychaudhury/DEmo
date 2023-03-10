from django.shortcuts import render
from django .http import HttpResponse
from shop.models import product
# Create your views here.

def index(request):
    productobject=product.objects.all()
    print(productobject)
    
    return render(request,'shop/index.html')

def track(request):
    return HttpResponse("Track")
def search(request):
     return HttpResponse("Search")
def product(request):
      return HttpResponse("Product")
def checkout(request):
     return HttpResponse("Checkout")                    
           
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
