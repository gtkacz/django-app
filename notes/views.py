from django.shortcuts import render, redirect
from .models import Note

def index(request):
    if request.method=='POST':
        title=request.POST.get('titulo')
        content=request.POST.get('detalhes')
        id=request.POST.get('id')
        edit=request.POST.get('edit_note_id')
        if not title:
            note = Note.objects.get(id=id)
            note.delete()
        
        elif id != None and id != "None" and id != '':
            note = Note.objects.get(id=edit)
            note.title = title
            note.content = content
            note.save()
        
        else:
            note = Note(title=title, content=content)
            note.save()
                    
        return redirect('index')
    else:
        all_notes=Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})
