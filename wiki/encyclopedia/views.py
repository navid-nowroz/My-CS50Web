from django.shortcuts import render, redirect

from . import util

import markdown2


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