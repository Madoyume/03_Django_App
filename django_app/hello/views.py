from django.shortcuts import render
from django.http import HtttpResponse
from .forms import HelloForm
from django.http import TemplateView

class HelloView(TemplateView):
    
    def __init__(self):
        self.params = {
            'title':'Hello',
            'message':'your data',
            'form':HelloForm()
        }
    
    def get(self, request):
        return render(request, 'hello/index.html', self.params)

    def post(self, request):
        msg = f'あなたは、<b>{request.POST['name']}({request.POST['age']})さんです。' + \
            f'<br>メールアドレスは<b>{request.POST['mail']}ですね。'
        self.params['message'] = msg
        self.params['form'] = HelloForm(request.POST)
        return render(request, 'hello/index.html', self.params)