from django.shortcuts import render, redirect
from . import util
import markdown2
from django import forms
from django.urls import reverse
import random


class NewEntryForm(forms.Form):
    title = forms.CharField(label="Title",
                            widget=forms.TextInput(attrs={
                                "placeholder" : "Write the title..."
                                }))
    content= forms.CharField(widget=forms.Textarea(attrs={
        'placeholder' : 'Write the content here....'
    })
                             , label="Content")
    

class EditEntryForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea)


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def title(request, title):
    content = util.get_entry(title)

    if content == None:
        return render(request, "encyclopedia/error_load.html", {
            "title" : title
        })    
    
    else:
        return render(request, "encyclopedia/entry.html", {
            "content": markdown2.markdown(content), "title" : title
        })


def search(request,):
    query = request.GET.get("q")
    entries = util.list_entries()
    results = [entry for entry in entries if query.lower() in entry.lower()]

    if query.lower() in list(map(str.lower, entries)):
        return redirect("show-entry", title=query)
    
    elif not len(results) > 0:
        return render(request, "encyclopedia/error_load.html", {
            "title" : query,
        })
    
    else:
        return render(request, "encyclopedia/search_results.html", {
            "results" : results, "query": query
        })
    

def new(request):
    return render(request, "encyclopedia/new.html", {
        "form" : NewEntryForm()
    })


def created(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
        entries = util.list_entries()

        if title.lower() not in list(map(str.lower, entries)):
            util.save_entry(title, content)
            return redirect(reverse("show-entry", kwargs={"title" : title}))
        
        else:
            return render(request, "encyclopedia/created_apology.html", {
                "form" : NewEntryForm()
            })
    else:
        return redirect("new")


def edit(request, title):
    content = util.get_entry(title)

    form = EditEntryForm(initial={"content" : content})
    return render(request, "encyclopedia/edit.html", {
        "title" : title,
        "form" : form,
    })


def updated(request):
    if request.method == "POST":
        form = EditEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
        entries = util.list_entries()

        util.save_entry(title, content)
        return redirect(reverse("show-entry", kwargs={"title" : title}))
    
    else:
        return redirect(reverse("show-entry", kwargs={"title" : title}))
    

def randomise(request):
    random_entry = random.choice(util.list_entries())
    content = util.get_entry(random_entry)
    
    return render(request, "encyclopedia/entry.html", {
        "content" : markdown2.markdown(content),
        "title" : random_entry,
    })