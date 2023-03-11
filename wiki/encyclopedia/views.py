from django.shortcuts import render
import markdown2
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki(request, name):
    content = markdown2.markdown(util.get_entry(name))

    return render(request, "encyclopedia/content.html", {
        "content" : content, "name" : name
    })