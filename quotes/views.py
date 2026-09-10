from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

import random

quotes = [
  "Sometimes you need to get knocked down before you can really figure out what your fight is, and how you need to fight it.",
  "Everything that you fought for was not for yourself. It was for those that come after.",
  "As is often the case, those that follow most often enjoy the results of the progress you gained.",
  "Sometimes your grades don’t give a great indication of what your greatness might be.",
]
images = [
  "https://miro.medium.com/v2/resize:fit:1400/format:webp/1*_dkjnqzFYtlzxg0CkZgj4g.jpeg",
  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQVlaNcr3OYeHHIjE2H6PnORyO6fkoC4rvYbzQHtbz5RA&s=10",
  "https://people.com/thmb/WU8DVHNWG-3osyzvQLoiSU6zLzI=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc():focal(899x326:901x328)/books-11-2000-a90067111e91441fb1e2e91dcb7c4184.jpg",
  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ1cUYFGqYNkjbl2ZBosB2ctslAoeMTc9tykjgagWtm_A&s=10",
]

quote_person = "Chadwick Boseman"

# Create your views here.
def quotes_about_page(request):
  ''' Display about page '''
  template_name = 'quotes/about.html'  
  return render(request, template_name)
  
def quotes_quote_page(request):
  ''' Display daily quote page '''
  template_name = 'quotes/quote.html'
  
  random_quote = quotes[random.randint(0,len(quotes) - 1)]
  random_image = images[random.randint(0,len(images) - 1)]
  
  context = {
    "current_quote": random_quote,
    "current_image": random_image,
    "quote_person": quote_person,
  }
  
  return render(request, template_name, context)
  
def quotes_show_all_page(request):
  ''' Display all quotes and images page '''
  template_name = 'quotes/show_all.html'
  
  context = {
    "all_quotes": quotes,
    "all_images": images,
    "quote_person": quote_person,
  }
  
  return render(request, template_name, context)