from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import Widget
from .forms import WidgetForm

# Create your views here.
def index(request):
  form = WidgetForm()
  widget = Widget.objects.all()
  total = Widget.objects.aggregate(total_value=Sum('quantity'))
  if request.method == 'POST':
    form = WidgetForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('index')
    else:
      form = WidgetForm()

  return render(request, 'index.html', {'form': form, 'widget_list': widget, 'total': total })

def delete(request, widget_id):
  widget = Widget.objects.get(id=widget_id)
  widget.delete()
  return redirect('index')

