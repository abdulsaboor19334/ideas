from django.db import models

from django.contrib.auth.models import User 

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


    def instructor_rating(self):
        instructor = Instructors.objects.get(pk=self.id)
        reviews = Reviews.objects.filter(instructor=instructor)
        rating = 0
        if reviews:
            for review in reviews:
                rating += review.individual_rating
            rating = rating/len(reviews)
        else:
            rating = 0
        return rating

class Reviews(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructors,on_delete=models.CASCADE)
    individual_rating = models.DecimalField(max_digits=3,decimal_places=2)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)


