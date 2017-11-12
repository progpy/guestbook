from django.shortcuts import render
from django import forms

from .models import Message


class MessageForm(forms.Form):
    name = forms.CharField(label='Ваше имя', max_length=255)
    text = forms.CharField(label='Cообщение', widget=forms.Textarea)


def main(request):
    if request.POST:
        form = MessageForm(request.POST)
        if form.is_valid():
            Message.objects.create(name=form.cleaned_data['name'], text=form.cleaned_data['text'])
            form = MessageForm()
    else:
        form = MessageForm()

    messages = Message.objects.all().order_by('-created_at')[:5]
    context = {
        'messages': messages,
        'form': form,
    }
    return render(request, 'guestbook.html', context)
