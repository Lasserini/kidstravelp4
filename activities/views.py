from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Experience, Review
from .filters import ExperienceFilter


# The Index Search page view
def indexView(request):
    experiences = Experience.objects.all()

    myFilter = ExperienceFilter(request.GET, queryset=experiences)
    experiences = myFilter.qs

    context = {'experiences': experiences, 'myFilter': myFilter}
    return render(request, 'index.html', context)


# The Index page view
# class HomeView(View):

#    def get(self, request):
#        return render(request, 'index.html')


    # The SearchExp view
#    def search(request):
#        qs = Experience.objects.all()
#        city_chosen = request.Get.get('city_chosen')
#        category_chosen = request.Get.get('category_chosen')
#        free_chosen = request.Get.get('free_chosen')
    

# class ExperienceView(generic.ListView):
#	model = Experience
#	queryset = Experience.objects.all().order_by('category')
#	template_name = 'results.html'
