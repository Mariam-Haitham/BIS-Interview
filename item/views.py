from django.shortcuts import render, redirect

from .models import Item

def list (request):
	items = Item.objects.all()

	context = {
		"items": items,
	}
	return render(request, "list.html", context)