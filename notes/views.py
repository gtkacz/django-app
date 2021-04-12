from django.shortcuts import render, redirect
from .models import Note

def index(request):
    if request.method=='POST':
        title=request.POST.get('titulo')
        content=request.POST.get('detalhes')
        id=request.POST.get('id')
        edit=request.POST.get('edit_note_id')
        if id==None or id=="None" or id=='':
            note=Note(title=title, content=content)
            note.save()
        else:
            if not title:
                Note.objects.filter(id=id).delete()
            else:
                edit=Note.objects.get(id=edit)
                edit.title=title
                edit.content=content
                edit.save()
                
        return redirect('index')
    else:
        all_notes=Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})
