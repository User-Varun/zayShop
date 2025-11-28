from django.shortcuts import render, redirect
from .models import Customer , ImageUploader , Product
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request , 'index.html')

def about(request):
    return render(request , 'about.html')

def contact(request):
    return render(request , 'contact.html')


def shopSingle(request):
    return render(request , 'shop-single.html')


def product_detail(request, product_id):
    """Show product detail  """
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return redirect('shop')

    return render(request, 'shop-single.html', {'product': product})

def shop(request):
  name = request.session.get('name')
  products = Product.objects.all()
  if name is not None:
        return render(request , 'shop.html' , {'products' : products})
  else:
        return render(request , 'login.html')

    

def login(request):
    request.session.flush()
    if request.method == 'POST':
        unm1= request.POST.get('unm')
        pw1 = request.POST.get('pw')

        try:
            data = Customer.objects.get(pw = pw1)
            request.session['name'] = unm1
            request.session['data'] = data.id
            return redirect('/shop')
        except Exception:
            return render(request , 'login.html')
    else:  
     return render(request , 'login.html')


def regis(request):

    if request.method == 'POST':
        cname = request.POST.get('cname')
        cadd = request.POST.get('cadd')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        unm = request.POST.get('unm')
        pw = request.POST.get('pw')

        cust = Customer(cname = cname, cadd = cadd , email = email , phone = phone , unm=unm , pw = pw)

        cust.save()
        return render(request , 'login.html')

    else :
        return render(request , 'regis.html')
    

def upload_image(request):
    if request.method == 'POST' and len(request.FILES) !=0:
        image_uploader_obj = ImageUploader()
        image_uploader_obj.photo = request.FILES['image']
        image_uploader_obj.save()
    
    all_images = ImageUploader.objects.all()

    return render(request = request , template_name='imageUpload.html' , context={'img' : all_images })


def delete_image(request , image_id):
    if request.method == 'POST':
        obj = ImageUploader.objects.get(pk=image_id)
        obj.delete()
        # In HttpResponseRedirect take the "route" of the urls
        return HttpResponseRedirect(redirect_to="/images")


def add_to_cart(request, product_id=None):
    """Simple cart increment: stores cart count and product ids in session.

    - If `product_id` is provided, append it to `request.session['cart']` list.
    - Always increment `request.session['cart_count']` by 1.
    - Redirect back to the referring page (or `/shop` if none).
    """
    # initialize
    cart_count = request.session.get('cart_count', 0)
    cart_count += 1
    request.session['cart_count'] = cart_count

    if product_id is not None:
        cart = request.session.get('cart', [])
        # store ids as ints for clarity
        try:
            pid = int(product_id)
        except Exception:
            pid = None
        if pid:
            cart.append(pid)
            request.session['cart'] = cart

    # Redirect back to where the request came from
    referer = request.META.get('HTTP_REFERER')
    if referer:
        return HttpResponseRedirect(referer)
    return redirect('shop')