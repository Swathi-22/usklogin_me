from .forms import NoteForm
from .models import Note
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render


@login_required
def note_list(request):
    form = NoteForm(request.POST or None)
    if form.is_valid():
        note = form.save(commit=False)
        note.created_by = request.user
        note.save()
    notes = Note.objects.filter(created_by=request.user)
    context = {"notes": notes, "form": form}
    return render(request, "accounts/note_list.html", context)


@login_required
def note_delete(request, pk):
    print(pk)
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    response_data = {"status": "true"}
    return JsonResponse(response_data)
