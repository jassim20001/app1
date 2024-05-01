from django.shortcuts import render

from app.models import Blog,Comment, Conect

# Create your views here.
def home(request):
    if request.method=='POST':
          
      x=request.POST.get('name')
      y=request.POST.get('email')
      z=request.POST.get('subject')
      s=Conect(name=x,email=y,subject=z)
      s.save()
      
      return render(request, 'index.html')
    
    blog=Blog.objects.all()
    coment=Comment.objects.all()
   
    context={
        'blog':blog,
        'comment':coment,
    }
   
    return render(request, 'index.html',context=context)

def comment(request):
    if request.method=='POST':
          
      x=request.POST.get('name')
      y=request.POST.get('date')
      e=request.POST.get('email')
      z=request.POST.get('comment')
      s=Comment(name=x,comment=z,date=y,email=e)
      s.save()
      
      return render(request, 'comment.html')

    return render(request, 'comment.html')
