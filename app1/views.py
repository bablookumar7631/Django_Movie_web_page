from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.http import HttpResponse,HttpResponseForbidden,JsonResponse
from .models import*
from django import template
register = template.Library()
from django.views import View



# Create your views here
def  indexPage(request):
    return render(request, 'index.html')

def  SignupPage(request):
    if request.method == "POST":
        uname=request.POST.get('Username')
        email=request.POST.get('Email')
        pass1=request.POST.get('Password')
        pass2=request.POST.get('CNFpass')
        try:
            validate_email(email)
        except ValidationError as e:
            return HttpResponse(e)
        else:
            if pass1 != pass2:
                return HttpResponse("Your password and confirm password are not Same")
            else:
                my_user=User.objects.create_user(uname,email,pass1)
                my_user.save()
                return redirect('login')
            
    return render(request, 'signup.html')


def  LoginPage(request):
    if request.method=="POST":
        username=request.POST.get('Username')
        pass1=request.POST.get('Password')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('/moviesList')
        else:
            return HttpResponse("Username or password is incorrect")
    return render(request, 'login.html')



@login_required(login_url='index')
def  MoviesList(request):
    obj1=Allmovie.objects.all()
    obj2 = Category.objects.all()
    if request.method=="GET":
        mn=request.GET.get('moviename')
        if mn != None:
            obj1 = Allmovie.objects.filter(movie_name__icontains=mn)
    
    obj3={}
    for categ in obj2:
        movie_count = Allmovie.objects.filter(category_id = categ.cat_id ).count()
        if movie_count > 0:
            obj3[categ.cat_id] = categ.name
    return render(request, 'moviesList.html',{'Movies':obj1,'Categories':obj3})
   


@login_required(login_url='index')
def MovieDetailPage(request,id):
    data=Allmovie.objects.get(movie_id=id)
    print(data)
    screenshots = Screenshot.objects.filter(movie_id=id)
    print(screenshots)
    movie_comments = MovieComment.objects.filter(allmovies_id=id)

    return render(request,'moviedetail.html',{'data':data, 'screenshots' : screenshots, 'movie_comments': movie_comments})


def postComment(request, allmovie_id):
    if request.method == 'POST':
        com_msg = request.POST.get('com_msg')  # Use request.POST.get() to access form data
        rating = int(request.POST.get('rating'))

        allmovie = Allmovie.objects.get(pk=allmovie_id)

        movie_comment = MovieComment(
            allmovies=allmovie,
            commentor=request.user,
            com_msg=com_msg,
            rating=rating,
        )
        movie_comment.save()

        return redirect('moviedetail', id=allmovie_id)
    return render(request, 'moviedetail.html')



@login_required(login_url='index')
def  ReviewPage(request):
    return render(request, 'reviews.html')



def LogoutPage(request):
    logout(request)
    return redirect('index')

# delete data ........................
def delete_data(request, allmovie_id):
    if request.method == 'POST':
        # Use get_object_or_404 to retrieve the MovieComment object
        movie_comment = get_object_or_404(MovieComment, pk=allmovie_id)
        
        # Check if the user attempting to delete the comment is the original commenter
        if movie_comment.commentor == request.user:
            # Get the associated movie ID
            movie_id = movie_comment.allmovies.movie_id
            
            # Delete the comment
            movie_comment.delete()
            
            # Redirect back to the movie detail page
            return redirect('moviedetail', id=movie_id)
        else:
            return HttpResponse("You don't have permission to delete this comment.")
    
    return redirect('moviedetail', id=allmovie_id)


# update comment data ...............

def editComment(request):
    # Fetch the MovieComment object using get_object_or_404

    if request.method == 'POST':
        
        movie_comment = get_object_or_404(MovieComment, pk=request.POST.get('comment_id'))
        # Update the comment and rating based on form data
        movie_comment.com_msg = request.POST.get('com_msg')
        movie_comment.rating = request.POST.get('rating')
        movie_comment.save()
        
        # Redirect to the movie detail page for the updated comment
        return JsonResponse({'updatedComment': request.POST.get('com_msg'),
                             'updatedRating' : request.POST.get('rating')})  # Assuming 'moviedetail' is a valid URL pattern
    return JsonResponse({'error': 'Comment not updated'})


# Feedback our website ...................
def save_feedback(request):
    if request.method=="POST":
        feedback_msg=request.POST.get('feedback_msg')
        feedback_rating=request.POST.get('feedback_rating')

        
        svf = Mywebsite_feedback(
            feedbackor_name=request.user,
            feedback_msg=feedback_msg,
            feedback_rating=feedback_rating
        )
            
        svf.save()
    return render(request, 'reviews.html')