from django.shortcuts import render
from .models import Instructors,Reviews, Departments, Courses

from .forms import ReviewForm

import django_filters

class InstructorFilter(django_filters.FilterSet):
    # name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Instructors
        fields = ['department', 'courses_taught', ]

# instructors

def all_instructors(request):
    departments = Departments.objects.all()
    courses = Courses.objects.all
    instructors = Instructors.objects.all()
    filter = InstructorFilter(request.GET, queryset=instructors)
    context = {
        'instructors' : instructors,
        'filter' : filter,
        'departments': departments,
        'courses': courses,
    }
    return render(request,'instructor/all.html',context)


def single_instructor(request, id):
    instructor = Instructors.objects.get(pk=id)
    check_review = Reviews.objects.filter(user=request.user, instructor=instructor).first()
    # check_review = Reviews.objects.get(
    #     user = request.user,
    #     instructor = instructor,
    # )
    reviews = Reviews.objects.filter(instructor = instructor)
    if check_review:
        reviewed = True
        form = ReviewForm(request.POST or None, instance=check_review)
        if form.is_valid():
            form.save()
    else:
        reviewed = False
        form = ReviewForm(request.POST or None)
        if form.is_valid():
            form.save()
    print(request.POST)
    context = {
        'instructor' : instructor,
        'reviewed' : reviewed,
        'reviews' : reviews,
        'form': form,
    }
    return render(request, 'instructor/single.html', context)




def review(request,id):
    if request.method == 'POST':
        instructor = Instructors.objects.get(pk=id)
        description = request.POST.get('description')
        user = request.user
        rating = request.POST.get('rating')
        save_review = Reviews.objects.create(
        user = user,
        instructor = instructor,
        individual_rating=rating,
        description=description
        )
        all_ratings = Reviews.objects.filter(instructor=instructor)
        total = 0
        ave_rating = 0
        for rat in all_ratings:
            total += rat.individual_rating
            ave_rating = total/len(all_ratings)
        instructor.rating = ave_rating
        instructor.save()
        save_review.save()
    
    return redirect('instructors:single_instructor',instructor.id)