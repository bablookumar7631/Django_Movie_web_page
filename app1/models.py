from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Screenshot(models.Model):
    scr_id = models.AutoField(primary_key=True)
    scr_title = models.CharField(max_length=100)
    scr_image = models.ImageField(default="")
    movie_id = models.ForeignKey('Allmovie', on_delete=models.CASCADE, default=True, null=False)


    def __str__(self):
        return f"{self.scr_id},{self.scr_title}"
    

class Allmovie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    movie_name = models.CharField(max_length=200, null=False, blank=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default=True, null=False)
    movie_image = models.ImageField(default="")
    # Movie Info:
    Full_name = models.CharField(max_length=100, default="")
    language = models.CharField(max_length=100, null=False, blank=False,default="")
    # release_year = models.CharField(max_length=100,default="")
    release_year = models.IntegerField(default=0)
    quality = models.CharField(max_length=100,default="")
    pixel = models.CharField(max_length=100,default="")
    size = models.CharField(max_length=100,default="")
    stars_name = models.CharField(max_length=255,default="")
    director = models.CharField(max_length=255,default="")
    # Storyline:
    storyline = models.TextField(default="")
    
    # Links_name and Links_for download
    links_name_1 = models.CharField(max_length=200, default="")
    links_down_1 = models.URLField(max_length = 200, default="")
    links_name_2 = models.CharField(max_length=200, default="")
    links_down_2 = models.URLField(max_length = 200, default="")


    def __str__(self):
        return f"{self.movie_name},{self.category}"
    
class MovieComment(models.Model):
    allmovies = models.ForeignKey(Allmovie, related_name="comments", on_delete=models.CASCADE)
    commentor = models.ForeignKey(User, on_delete=models.CASCADE)
    com_msg = models.TextField()
    rating = models.PositiveIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.commentor},{self.rating}"
    

class Mywebsite_feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    feedbackor_name = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback_msg = models.TextField()
    feedback_rating = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.feedbackor_name} -> Rating is : {self.feedback_rating} -> {self.feedback_msg}"


