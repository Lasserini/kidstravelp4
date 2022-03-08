from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Experience, Review
from .filters import ExperienceFilter
from .forms import ReviewForm


# The Index Search page view
def indexView(request):

    return render(request, 'index.html')


def resultsView(request):
    experiences = Experience.objects.all()

    myFilter = ExperienceFilter(request.GET, queryset=experiences)
    experiences = myFilter.qs

    context = {'experiences': experiences, 'myFilter': myFilter}
    return render(request, 'results.html', context)


class ExperienceDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Experience.objects.all()
        experience = get_object_or_404(queryset, slug=slug)
        reviews = experience.reviews.all().order_by('-created_on')

        return render(
            request,
            "experience_detail.html",
            {
                "experience": experience,
                "reviews": reviews,
                "review_form": ReviewForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Experience.objects.all()
        experience = get_object_or_404(queryset, slug=slug)
        reviews = experience.reviews.all().order_by('-created_on')

        review_form = ReviewForm(data=request.POST)

        if review_form.is_valid():
            review_form.instance.username = request.user.username
            review = review_form.save(commit=False)
            review.experience = experience
            review.save()
        else:
            review_form = ReviewForm()

        return render(
            request,
            "experience_detail.html",
            {
                "experience": experience,
                "reviews": reviews,
                "review_form": ReviewForm()
            },
        )