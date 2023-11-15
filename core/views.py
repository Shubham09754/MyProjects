from django.shortcuts import render
from .models import User
from .forms import Form

# Create your views here.
def home(request):
    return render(request,'core/home.html')

def contact(request):
    return render(request,'core/contact.html')


#def contact(request, id):
#    if request.method == 'POST':
#        pi = User.objects.get(pk=id)
#        fm = Form(request.POST, instance=pi)
#        if fm.is_valid():
#            fm.save()
#    else:
#        pi = User.objects.get(pk=id)
#        fm = Form(instance=pi)
#
#    return render(request, 'core/contact.html', {'form':fm})
#