from django.shortcuts import render, redirect

from b_d_p.main_app.forms import InputForm
from b_d_p.main_app.models import Data


def index(request):
    form = InputForm(request.POST or None)
    objects = Data.objects.all()
    if form.is_valid():
        form.save()
        return redirect('success')
    context = {
        'objects': objects,
        'form': form,
    }
    return render(request, 'index.html', context=context)


def success(request):
    return render(request, 'success.html')
