from django.shortcuts import render


def render_start_page(request):
    return render(request, 'index.html')


def render_reg_page(request):
    return render(request, 'registration.html')


def render_auth_page(request):
    return render(request, 'auth.html')


def render_lk_page(request):
    return render(request, 'lk.html')


def render_order_page(request):
    return render(request, 'order.html')

