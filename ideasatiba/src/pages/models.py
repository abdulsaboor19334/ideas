from django.db import models
from django.contrib.auth.models import User 

TYPE = (
    (0,'downvote'),
    (1,'upvote')
)

class Posts(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField(blank=False,null=False)
    image = models.ImageField(blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_cout = models.IntegerField(default=0)
    vote_count = models.IntegerField(default=0)
    featured = models.BooleanField(default=False)

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

# instructors

class Departments(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Courses(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Instructors(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(blank=True,null=True)
    designation = models.CharField(max_length=100)
    department = models.ManyToManyField(Departments)
    specialization = models.CharField(max_length=100)
    onboard_status = models.BooleanField()
    email = models.EmailField()
    courses_taught = models.ManyToManyField(Courses)
    rating = models.DecimalField(max_digits=3,decimal_places=2,default=0.00)
    nickname = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Reviews(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructors,on_delete=models.CASCADE)
    individual_rating = models.DecimalField(max_digits=3,decimal_places=2)
    description = models.TextField()
