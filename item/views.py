from django.shortcuts import render, redirect

from .models import Item
from .forms import ItemForm

def list (request):
	items = Item.objects.all()

	context = {
		"items": items,
	}
	return render(request, "list.html", context)


def create(request):

	form = ItemForm()
	if request.method == "POST":
		form = ItemForm(request.POST, request.FILES or None)
		if form.is_valid():
			item = form.save(commit = False)
			name = item.name
			item.save()
			messages.success(request, "%s is Successfully Added" %name)
			return redirect('item-list')
		print (form.errors)
	context = {
		"form": form,
	}
	return render(request, 'create.html', context)