from django.shortcuts import render, redirect
from .models import Posts,Vote,Comments, Topic

from instructors.models import Instructors

from .forms import PostsForm

from django.db.models import Q


def front_page(request):
    form = PostsForm(request.POST or None)
    if request.method == 'POST':
        form = PostsForm(request.POST,request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post', post.id)

    posts = Posts.objects.all().order_by('-vote_count')
    featured = Posts.objects.filter(featured=True)[0:4]
    top_instructors = Instructors.objects.all().order_by('-rating')[0:5]
    topics = Topic.objects.all()[0:5]
    context = {
        'form': form,
        'posts' : posts,
        'featured' : featured,
        'instructor' : top_instructors,
        'topics': topics,
    }
    return render(request, 'index.html', context)


def post_page(request, id):
    post = Posts.objects.get(id=id)
    context = {
        'post': post,
    }
    return render(request, 'post_page.html', context)


# def search_results(request):
#     return render(request, 'search.html', {})


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
    return redirect('post', post.id)


def topic_page(request, id):
    topic = Topic.objects.get(id=id)
    posts = Posts.objects.filter(topic=topic)
    context = {
        'posts': posts,
        'topic': topic, 
    }
    return render(request, 'topic.html', context)



def search_results(request):
    qs_inst = Instructors.objects.all()
    qs_post = Posts.objects.all()
    query = request.GET.get('query')
    print(query)
    print(qs_inst)
    print(qs_post)
    if query != '' and query is not None:
        qs_inst = qs_inst.filter(Q(name__icontains=query) | Q(nickname__icontains=query ) | Q(email__icontains=query)).distinct()
        qs_post = qs_post.filter(Q(topic__name__icontains=query) | Q(title__icontains=query) | Q(body__icontains=query))
        print(qs_inst)
        print(qs_post)
    context = {
        'instructors': qs_inst,
        'posts' : qs_post,
        'query': query,
    }
    return render(request, 'search.html', context)