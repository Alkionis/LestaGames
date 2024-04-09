from django.shortcuts import render
from .forms import UploadFileForm

from .handler import handle_uploaded_file


def index(request):
    if request.method == "POST":
        form = UploadFileForm(request.FILES)
        if request.FILES:
            tfidflist = handle_uploaded_file(request.FILES["file"])

            return render(request, "mainpage.html", {"form": form, 'tfidflist': tfidflist})
        else:
            print("Invalid Form")
    else:
        form = UploadFileForm()
    return render(request, "mainpage.html", {"form": form})
