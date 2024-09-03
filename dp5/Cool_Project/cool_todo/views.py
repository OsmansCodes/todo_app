from django.shortcuts import render

def todos(request):
    data_from_urls= request.GET
    print(data_from_urls)
    context = {
        "type": data_from_urls.get("type"),
    }
    return render(request, "cool_todo/todos.html", context= context )