from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    params = {
        'title':'Hello/Index',
        'msg':'これは、サンプルで作ったページです。',
        'goto':'hello:next',
    }
    return render(request, 'hello/index.html', params)
    
def next(request):
    params = {
        'title':'Hello/Next',
        'msg':'これは、もう一つのページです。',
        'goto':'index',
    }
    return render(request, 'hello/index.html', params)
    
    
    # return render(request, 'hello/index.html')
    
    # result = f'your id:{str(id)}, name:{str(nickname)}.'
    # return HttpResponse(result)
    
    # if 'msg' in request.GET:
    #     msg = request.GET['msg']
    #     result = (f'you typed:{msg}.')
    # else:
    #     result = 'please send msg parameter!'
    # return HttpResponse(result)
    