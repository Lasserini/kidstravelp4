from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views import View
from .models import Experience, Review
from .filters import ExperienceFilter
from .forms import ReviewForm, ExperienceForm


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
        reviews = experience.reviews.filter().order_by('-created_on')

        review_form = ReviewForm(data=request.POST)

        if review_form.is_valid():
            review_form.instance.name = request.user.username
            review = review_form.save(commit=False)
            review.experience = experience
            review.username = request.user
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


def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)

    if request.user.is_superuser or request.user == review.username:
        if request.method == "POST":
            form = ReviewForm(request.POST, instance=review)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/results")
        else:
            form = ReviewForm(instance=review)

    context = {'form': form}

    return render(request, 'edit_review.html', context)


def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.user.is_superuser or request.user == review.username:
        review.delete()
    return HttpResponseRedirect("/results")


def edit_experience(request, experience_id):
    experience = get_object_or_404(Experience, id=experience_id)

    if request.method == "POST":
        form = ExperienceForm(request.POST, instance=experience)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/results")
    else:
        form = ExperienceForm(instance=experience)

    context = {'form': form}

    return render(request, 'edit_experience.html', context)


def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, id=experience_id)
    if request.user.is_superuser:
        experience.delete()
    return HttpResponseRedirect("/results")


def add_experience(request):
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect("/results")
    form = ExperienceForm()
    context = {
        'form': form
    }
    return render(request, 'add_experience.html', context)
