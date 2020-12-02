from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.contrib.auth.models import User
# Create your models here.


class Movie(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=100)

    def no_of_ratings(self):
        ratings=Rating.objects.filter(movie=self)
        return(len(ratings))

    def avg_ratings(self):
        ratings = Rating.objects.filter(movie=self)
        sum=0
        for rating in ratings:
            sum=sum+rating.stars
        if(len(ratings)>0):
            return(sum/len(ratings))
        else:
            return 0

    def __str__(self):
        return '{}{}'.format(self.title, self.description)



class Rating(models.Model):
    movie=models.ForeignKey(Movie, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    stars=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    class Meta:
        unique_together=(('user','movie'),)
        index_together=(('user','movie'),)

    def __str__(self):
        return '{}{}{}'.format(self.movie, self.user,self.stars)

