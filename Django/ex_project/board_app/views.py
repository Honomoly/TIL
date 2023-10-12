from django.shortcuts import render

# Create your views here.
def board_form(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        return render(request, "board_app/board_result.html", {'input':{'title':title, 'content':content}})
    else:
        return render(request, "board_app/board_form.html")