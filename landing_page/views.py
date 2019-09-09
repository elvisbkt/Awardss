from django.shortcuts import render, redirect, get_object_or_404
from .models import Website, Category
from users.models import CustomUser
from django.views.generic import DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
# from django.conf import settings

# import redis

# r = redis.StrictRedis(host=settings.REDIS_HOST,
#                       port=settings.REDIS_PORT,
#                       db=settings.REDIS_DB)

def  landing_index(request):
    print(request.user.username)
    websites = Website.objects.all().order_by('-posted_on')
    context = {
        "websites": websites,
    }
    return render(request, 'landing_index.html', context)


class WebPostView(LoginRequiredMixin, CreateView):
    model = Website
    context_object_name = 'web'
    template_name = 'website_form.html'
    fields = ['title','description', 'image', 'url']
    success_url = reverse_lazy('landing_index')

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)

def search_results(request):
    if 'website' in request.GET and request.GET["website"]:
        search_term = request.GET.get("website")
        searched_websites = Website.search_by_title(search_term)
        message = f"{search_term}"
        return render(request, 'search.html',{"message":message,"websites": searched_websites})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

class WebsiteDetailView(DetailView):
    model = Website
    context_object_name = 'website'
    template_name = 'website_detail.html'


@login_required
@require_POST
def website_like(request):
    website_id = request.POST.get('id')
    action = request.POST.get('action')
    if website_id and action:
        try:
            website = Website.objects.get(id=website_id)
            if action == 'like':
                website.users_like.add(request.user)
                create_action(request.user, 'likes', website)
            else:
                website.users_like.remove(request.user)
            return JsonResponse({'status':'ok'})
        except:
            pass
    return JsonResponse({'status':'ko'})
