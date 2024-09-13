from django.shortcuts import render
from .forms import SessionForm
from django.views.generic import TemplateView

class HelloView(TemplateView):
    
    def __init__(self):
        self.params = {
            'title':'Hello',
            'form':SessionForm(),
            'result':None
        }
    
    def get(self, request):
        self.params = request.session.get('last_msg', 'No message.')
        return render(request, 'hello/index.html', self.params)

    def post(self, request):
        ses = request.POST['session']
        self.params['result'] = f'send:"{ses}".'
        request.session['last_msg'] = ses
        self.params['form'] = SessionForm(request.POST)
        return render(request, 'hello/index.html', self.params)