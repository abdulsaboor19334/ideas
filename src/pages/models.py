from django.db import models
from django.contrib.auth.models import User 

TYPE = (
    (0,'downvote'),
    (1,'upvote')
)

class Topic(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class Posts(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.SET_NULL, null=True, blank=True, default=1)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=150, null=True, blank=True)
    body = models.TextField(blank=False,null=False)
    image = models.ImageField(blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_cout = models.IntegerField(default=0)
    vote_count = models.IntegerField(default=0)
    featured = models.BooleanField(default=False)
    anonymous = models.BooleanField(default=False)
    

    def __str__(self):
        return self.user.username

    def get_vote_difference(self):
        upvote = self.vote_set.filter(vote_type=1).count()
        downvote = self.vote_set.filter(vote_type=0).count()
        votecount = upvote-downvote

        self.vote_count = votecount
        self.save()
        return votecount

class Vote(models.Model):
    voter = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Posts,on_delete=models.CASCADE)
    vote_type = models.SmallIntegerField(choices=TYPE)

    def __str__(self):
        return self.voter.username +' '+ str(self.vote_type)

class Comments(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Posts,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
