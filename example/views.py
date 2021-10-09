from django.shortcuts import render


def page_not_found_view(request, exception):
    return render(request, 'ERROR/index.html', status=404)


def server_error(request, *exception):
    return render(request, 'ERROR/index.html', status=500)
