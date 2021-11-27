from django.http.response import HttpResponseRedirect
from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import user
# Create your views here.

#this function will add new items and show all items
def add_show(request):
    if request.method == 'POST':
       fm = StudentRegistration(request.POST)
       if fm.is_valid(): #check karega valid hai ya nai
          nm=fm.cleaned_data['name']  #ek field ko hata sakte conti-
          em=fm.cleaned_data['email'] # nue  fir uska data store nai hoga
          pw=fm.cleaned_data['password']
          reg= user(name =nm, email=em, password=pw)
          reg.save() #ispe data save hojaega
          fm = StudentRegistration() #isse page firse khhali hojaega 
          
    else:
       fm = StudentRegistration(request.POST)
    stud = user.objects.all() # isse sara data changes user ko dikhega or fir stud pas karo
                                
    return render(request,'addandshow.html', {'form':fm, 'stu':stud})  

# this function will update/edit
def update(request, id):
   if request.method == 'POST':
     pi= user.objects.get(pk=id)
     fm= StudentRegistration(request.POST, instance=pi)
     if fm.is_valid():
        fm.save()
   else:
      pi= user.objects.get(pk=id)
      fm= StudentRegistration(request.POST, instance=pi)
   return render(request, 'updatestudent.html', {'form':fm}) 



# this function is for delete
def delete(request,id):
    if request.method == 'POST':
       pi=user.objects.get(pk=id) # idhar object all karte to galat hota, humei sirf id vala delete karna hai
       pi.delete()
       return HttpResponseRedirect('/')


