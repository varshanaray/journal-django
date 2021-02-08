from django.shortcuts import render

# Create your views here.
from .models import Page, Login, Notebk
from django.views import generic
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_notebooks = Notebk.objects.all().count()
    num_pages = Page.objects.all().count()


    context = {
        'num_notebooks': num_notebooks, 'num_pages': num_pages
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

  

class NotebkListView(generic.ListView):
    model = Notebk
    context_object_name = 'notebk_list'   # your own name for the list as a template variable
    template_name = '/notebk_list.html'  # Specify your own template name/location

class NotebkDetailView(generic.DetailView):
    model = Notebk

class PageListView(generic.ListView):
    model = Page
    context_object_name = 'page_list'   # your own name for the list as a template variable
    template_name = '/page_list.html'  # Specify your own template name/location

class PageDetailView(generic.DetailView):
    model = Page
