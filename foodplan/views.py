from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from .forms import SubsForm



def render_start_page(request):
    return render(request, 'index.html')


def render_reg_page(request):
    return render(request, 'registration.html')


def render_auth_page(request):
    return render(request, 'auth.html')


@login_required(login_url='/')
def render_lk_page(request):
    return render(request, 'lk.html')


@login_required(login_url='/')
def render_order_page(request):
    if request.method == "POST":
        # name = request.POST.get("test")
        print('==================')
        print('POST is Here!')

        return redirect('/')
    
    else:
        subsform = SubsForm()

        context = {
            'form': subsform
        }

        return render(request, 'order.html', context)

