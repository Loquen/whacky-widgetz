from django.shortcuts import render, redirect
from .models import Widget
from .forms import WidgetForm

# Create your views here.
def index(request):
  form = WidgetForm()
  widget = Widget.objects.all()
  if request.method == 'POST':
    form = WidgetForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('index')
    else:
      form = WidgetForm()

  return render(request, 'index.html', {'form': form, 'widget_list': widget })

def delete(request, widget_id):
  widget = Widget.objects.get(id=widget_id)
  widget.delete()
  return redirect('index')

