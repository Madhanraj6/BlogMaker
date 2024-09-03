from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from .models import Post
from django.contrib import messages
from .forms import PersonForm

def base(request):
    return render(request,'base.html')

def post_list(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(title__icontains=query)
    else:
        posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request,pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Post.objects.create(title=title, content=content)
        messages.add_message(request,messages.SUCCESS,'Blog added successfully')
        return redirect('post_list')
    return render(request, 'blog/post_form.html')

def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
        messages.add_message(request,messages.SUCCESS,'Blog updated successfully')
        return redirect('post_detail', pk=post.id) 
    return render(request, 'blog/post_edit.html', {'post': post})


def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        messages.add_message(request,messages.SUCCESS,'Blog deleted successfully')
        return redirect('post_list')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})

def person(request):
    person_obj = PersonForm()
    if request.method == 'POST':
        person_obj = PersonForm(request.POST)
        if person_obj.is_valid():
            name = person_obj.cleaned_data['name']
            age = person_obj.cleaned_data['age']
            st = ''.join([name, str(age)])
            return HttpResponse(st)
        return HttpResponse('Form is invalid')
    
    return render(request, 'forms.html', {'form': person_obj})