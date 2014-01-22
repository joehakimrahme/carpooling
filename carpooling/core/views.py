from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404

from carpooling.core.models import Ad

def home(request):
    """Should show 2 buttons:
    + Look for a carpool ad
    + Submit a carpool ad
    """
    return HttpResponse("Hello, world. You're at the core home page.")

def index(request):
    """This page should output up to the 5 latest Ads in the db.
    """
    latest_ad_list = Ad.objects.all().order_by('-publication_date')[:5]
    template = loader.get_template("Ad/index.html")
    context = RequestContext(request, {
        'latest_ad_list': latest_ad_list,
    })

    return HttpResponse(template.render(context))

def show(request, ad_id):
    """This page exposes the details of an Ad.
    """
    ad = get_object_or_404(Ad, pk=ad_id)
    return render(request, 'Ad/show.html', {'ad': ad})
