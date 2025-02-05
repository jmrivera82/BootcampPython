from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comentarios
from .forms import ComentariosForm
# Create your views here.


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()  # Obtener los comentarios del post
    form = ComentariosForm()

    if request.method == "POST":
        form = ComentariosForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.usuario = request.usuario  # Asigna el usuario autenticado
            comment.post = post  # Asigna el post relacionado
            comment.save()
            return redirect('post_detail', post_id=post.id)

    return render(request, 'post.html', {'post': post, 'comments': comments, 'form': form})