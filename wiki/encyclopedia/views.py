from django.shortcuts import render

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

