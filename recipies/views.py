from django.shortcuts import render, redirect
from recipies.models import Recipie
from recipies.models import ScrapRecipie
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from recipies.models import comments
from recipies.forms import commentforms, recipieforms
from recipies.models import profile

# Create your views here.
def recipies_index(request):
    recipies=ScrapRecipie.objects.all()
    user=request.user
    if user.is_authenticated:
        print(user.profile.likedrecipies.all())
    context={
        'recipies':recipies
    }
    return render(request,"index.html",context)

def recipie_details(request,pk):
    print("inside recipie details")
    recipie=ScrapRecipie.objects.get(pk=pk)
    if request.method=="POST":
        form=commentforms(data=request.POST)
        if form.is_valid():
            newcomment=form.save(commit=False)
            newcomment.recipie=recipie
            newcomment.save()
    else:
        form=commentforms()    
    comments_connected=comments.objects.filter(recipie__pk=pk)
    for comment in comments_connected:
        print(comment.comment_info)
    context={
        'recipie':recipie,
        'author':"",
        'form':form,
        'comments':comments_connected
    }

    return render(request,"recipie_details.html",context)

def my_recipies(request):
    user=request.user
    recipies=ScrapRecipie.objects.filter(author=user)
    print("my recipies")
    print(recipies.count())
    for recipie in recipies:
        print(recipie.author)
        print("username"+user.username)
    context={
    'recipies':recipies
    }
    return render(request,"myrecipies.html",context) 

def create_recipies(request):
    recipies=ScrapRecipie.objects.all()
    if request.method=="POST":
        form=recipieforms(request.POST,request.FILES)
        if form.is_valid():
            newrecipie=form.save(commit=False)
            newrecipie.author=request.user
            newrecipie.save()
            return render(request,"index.html",{'recipies':recipies})
    else:
        form=recipieforms()
        
    return render(request,"create_recipie.html",{'form':form,'recipies':recipies})

def edit_recipies(request):
    recipie_pk=request.GET["recipiepk"]
    recipie=ScrapRecipie.objects.get(pk=recipie_pk)
    print("Update recipies")
    print(recipie.title)
    return render(request,"update.html",{'recipie':recipie})
def update_recipies(request):
    print("inside update function")
    recipie_pk=request.POST.get("recipiepk")
    print(recipie_pk)
    recipie=ScrapRecipie.objects.filter(pk=recipie_pk)
    recipie.update(title=request.POST.get("title"))
    recipie.update(description=request.POST.get("des"))
    return redirect("recipies_index")

def delete_recipies(request):
    print("inside delete recipies")
    recipie_pk=request.GET["recipiepk"]
    print(recipie_pk)
    recipie=ScrapRecipie.objects.filter(pk=recipie_pk)
    print("delete")
    print(recipie)
    recipie.delete()
    return redirect("recipies_index")

def logout(request):
    auth.logout(request)
    return redirect("/")




def likerecipie(request):
    pk=request.GET["recipie_id"]
    print("inside like recipies")
    print(pk)
    recipie=ScrapRecipie.objects.get(pk=pk)
    user=request.user
    if user.is_authenticated:
        print("user authenticated")
        #print("request method is:"+request.method)
        #print(hasattr(user,'profile'))
        if request.method=="GET":
            if hasattr(user,'profile')==False:
                recp=None
                userprofile=profile.objects.create(user=user)
                userprofile.save()
                userprofile.likedrecipies.add(recp)
            else:
               userprofile=profile.objects.get(user=user)
               userprofile.likedrecipies.add(recipie)
               userprofile.save()
               print("has attribute profile")
               return HttpResponse("success")
               #return HttpResponseRedirect(reverse('projects_index'))
        else:
            print("Not GET method")
            return HttpResponse("failure")
            #return HttpResponseRedirect(reverse('projects_index'))
        
    else:
        print("user is not authenticated")
        return HttpResponse("failure")
        #return HttpResponseRedirect(reverse('projects_index'))
