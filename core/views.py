from django.shortcuts import render, redirect
from .models import Post, Tags

def blog(request):
    posts = {
        'dados': Post.objects.all().order_by('-created_at'),
    }
    
    return render(request, 'base.html', posts)

def postar(request):
    if request.method =="POST":
        titulo = request.POST.get('titulo_modal')
        conteudo = request.POST.get('conteudo_modal')
        txt_tag = request.POST.get('tag')
        #print(titulo, conteudo, txt_tag)

        id = Tags.objects.filter(name__iexact=txt_tag)
        if not id:
            tag = Tags(name=txt_tag)
            tag.save()
            

        postagem = Post(
            title = titulo,
            content = conteudo,
            
        )

        
        postagem.save()

        id = Tags.objects.filter(name__iexact=txt_tag)
        for i in id:
            postagem.tags.add(i)
            postagem.save()
        

        return redirect("/blog")
    
   