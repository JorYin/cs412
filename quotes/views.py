from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def about_page(request):
  ''' Display about page '''
  template_name = 'quotes/about.html'
  return render(request, template_name)
  
def quote_page(request):
  ''' Display daily quote page '''
  template_name = 'quotes/quote.html'
  return render(request, template_name)
  
def show_all_page(request):
  ''' Display all quotes and images page '''
  template_name = 'quotes/show_all.html'
  return render(request, template_name)