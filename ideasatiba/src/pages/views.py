from django.shortcuts import render, redirect
from .models import Posts,Vote,Comments, Instructors



def front_page(request):
    posts = Posts.objects.all().order_by('-vote_count')
    featured = Posts.objects.filter(featured=True)[0:4]
    top_instructors = Instructors.objects.all().order_by('-rating')[0:5]
    context = {
        'posts' : posts,
        'featured' : featured,
        'instructor' : top_instructors
    }
    return render(request, 'index.html', context)


def post_page(request):
    return render(request, 'post_page.html', {})


def search_results(request):
    return render(request, 'search.html', {})


def vote(request):
    if request.method == 'POST':
        upvotes = request.POST.get('upvote_id')
        downvotes = request.POST.get('downvote_id')
        if upvotes:
            post = Posts.objects.get(pk=upvotes)            
            check_downvote = Vote.objects.filter(
                voter=request.user,
                post=post,
                vote_type=0
            )
            if check_downvote:
                # change to upvote
                the_downvote = Vote.objects.get(
                voter=request.user,
                post=post,
                vote_type=0
                )
                the_downvote.vote_type = 1
                the_downvote.save()
                return redirect('front')
            create_or_get_upvote = Vote.objects.get_or_create(
            voter=request.user,
            post=post,
            vote_type=1
            )
            if not create_or_get_upvote[1]:
                vote = Vote.objects.get(id=create_or_get_upvote[0].id)
                vote.delete()
        elif downvotes:
            post = Posts.objects.get(pk=downvotes)            
            check_upvote = Vote.objects.filter(
                voter=request.user,
                post=post,
                vote_type=1
            )
            if check_upvote:
                # change to downvote
                the_upvote = Vote.objects.get(
                voter=request.user,
                post=post,
                vote_type=1
                )
                the_upvote.vote_type = 0
                the_upvote.save()
                return redirect('front')
            create_or_get_downvote = Vote.objects.get_or_create(
            voter=request.user,
            post=post,
            vote_type=0
            )
            if not create_or_get_downvote[1]:
                vote = Vote.objects.get(id=create_or_get_downvote[0].id)
                vote.delete()
    return redirect('front')

# instructors

def all_instructors(request):
    instructors = Instructors.objects.all()
    context = {
        'instructors' : instructors
    }
    return render(request,'instructors.html',context)


def single_instructor(request,id):
    instructor = Instructors.objects.get(pk=id)
    check_review = Reviews.objects.filter(
        user = request.user,
        instructor = instructor,
    )
    if check_review:
        reviewed = True
    else:
        reviewed = False
    
    context = {
        'instructor' : instructor,
        'reviewed' : reviewed
    }
    return render(request,'single_instructor.html',context)


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