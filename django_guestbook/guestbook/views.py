from django.shortcuts import render

from .models import Message


def main(request):
    if request.POST:
        if 'name' in request.POST and 'text' in request.POST:
            Message.objects.create(name=request.POST['name'], text=request.POST['text'])

    messages = Message.objects.all().order_by('-created_at')[:5]
    context = {
        'messages': messages,
    }
    return render(request, 'guestbook.html', context)
