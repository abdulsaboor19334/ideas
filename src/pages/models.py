from django.db import models
from users.models import User 
 

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



class Comments(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Posts,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    vote_count = models.IntegerField()

    def get_vote_difference(self):
        upvote = self.vote_set.filter(vote_type=1).count()
        downvote = self.vote_set.filter(vote_type=0).count()
        votecount = upvote-downvote

        self.vote_count = votecount
        self.save()
        return votecount

class Vote(models.Model):
    voter = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Posts,on_delete=models.CASCADE, null=True,blank=True)
    comment = models.ForeignKey(Comments,on_delete=models.CASCADE,null=True,blank=True)
    vote_type = models.SmallIntegerField(choices=TYPE)

    def __str__(self):
        if self.post:
            return self.voter.username +' post' 
        else:
            return self.voter.username +' comment'
class Sub_Comments(models.Model):
    comment = models.ForeignKey(Comments,on_delete=models.CASCADE,null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    body = models.TextField()