from django.http import HttpResponse


def set_cookie(request):
    resp = HttpResponse('set cookies ok')
    resp.set_cookie('username', 'tedu', 600)
    return resp

def delete_cookie(request):
    resp = HttpResponse('delete cookies ok')
    resp.delete_cookie('username')
    return resp

def get_cookie(request):
    username = request.COOKIES.get('username','novalue')
    return HttpResponse('username = %s'% username)

