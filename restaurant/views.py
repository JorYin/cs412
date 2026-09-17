from django.shortcuts import render

# Create your views here.
def main_restaurant (request):
  template_name = 'restaurant/main.html'
  
  return render(request, template_name)

def order_restaurant (request):
  template_name = 'restaurant/order.html'
  
  return render(request, template_name)
  
def confirmation_restaurant (request):
  template_name = 'restaurant/confirmation.html'
  template_redirect = 'restaurant/order.html'
  
  if request.POST:
    
    context = {
      
    }
    
    return render(request, template_name, context)

  return render(request, template_redirect)