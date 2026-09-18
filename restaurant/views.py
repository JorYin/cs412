from django.shortcuts import render
import random
import time

# Create your views here.
def main_restaurant (request):
  template_name = 'restaurant/main.html'
  
  return render(request, template_name)

def order_restaurant (request):
  template_name = 'restaurant/order.html'
  
  # All the daily specials
  All_Daily_Special = ["Chocolate Chips Chicken Waffle", "Oreo Waffle", "Pumpkin Waffle"]
  
  # Get a random daily special
  Current_Daily_Special = All_Daily_Special[random.randint(0, len(All_Daily_Special)-1)]
  
  context={
    "Daily_Special": Current_Daily_Special,
  }
  
  return render(request, template_name, context)
  
def confirmation_restaurant (request):
  template_name = 'restaurant/confirmation.html'
  template_redirect = 'restaurant/order.html'
  
  # If a POST then go into the logic. Otherwise "redirect" to order form
  if request.POST:
    
    # Need some interval of 30 - 60 min difference from local time
    Random_Interval = random.randint(30,60)
    Seconds_Passed = Random_Interval * 60
    
    # Get the current seconds of local time
    Current_Time_Seconds = time.time()
    
    # Compute the random time where asctime() converts localtime() to a string
    Random_Order_Time = time.asctime(time.localtime(Current_Time_Seconds + Seconds_Passed))
    
    # Since all checkbox for form have menu grab all instances.
    Customer_Orders = request.POST.getlist("menu")
    Customer_Total = 0
    Special_Instructions = request.POST.get("Special_Instructions")
    Customer_Name = request.POST.get("Customer_Name")
    Customer_Phone = request.POST.get("Customer_Phone")
    Customer_Email = request.POST.get("Customer_Email")
    
    # If they didn't want the daily special then no need to append
    Daily_Special = request.POST.get("Daily_Special")
    if Daily_Special != "":
      Customer_Orders.append(Daily_Special)
    
    # Go through our list, the values have price at the end of them where "_" separates the numbers and words
    for i in range(len(Customer_Orders)):
      Current_Order = Customer_Orders[i].split("_")
      Customer_Total += int(Current_Order[-1])
      
      Sliced_Order = Current_Order[0:len(Current_Order)-1]
      
      # Update so when we go through and pass as context its not split with "_" and has the number at the end
      Customer_Orders[i] = " ".join(Sliced_Order)
    
    context = {
      "Random_Order_Time": Random_Order_Time,
      "Customer_Orders": Customer_Orders,
      "Special_Instructions": Special_Instructions,
      "Customer_Total": Customer_Total,
      "Customer_Name": Customer_Name,
      "Customer_Phone": Customer_Phone,
      "Customer_Email": Customer_Email,
    }
    
    return render(request, template_name, context)

  return render(request, template_redirect)