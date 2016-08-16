from django.shortcuts import render
from models import PurchasesForms, Purchases


# Create your views here.

def index(request):
    """

    :param request:
    :return:
    """

    if request.method == "POST":
        name = request.POST.get('name')
        sold = request.POST.get('sold')
        price = request.POST.get('price')
	state = request.POST.get('state')
	description = request.POST.get('description')
        model_save = Purchases(name=name, sold=sold, price=price,description=description,state=state)
        model_save.save()
    if request.method == "GET":
        print "hi"

    form = PurchasesForms()
    return render(request, 'crud/index.html', {'form': form})

def retrieve_item(request):
    items = Purchases.objects.all()
    return render(request,'crud/retrieve.html',{'items':items})
