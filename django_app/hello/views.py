from django.shortcuts import render
from .forms import HelloForm
from django.views.generic import TemplateView
from django.http import HttpResponse

class HelloView(TemplateView):
    
    def __init__(self):
        self.params = {
            'title':'Hello',
            'form':HelloForm(),
            'result':None
        }
    
    def get(self, request):
        return render(request, 'hello/index.html', self.params)

    def post(self, request):
        if ('check' in request.POST):
            self.params['result'] = 'Checked!!'
        else:
            self.params['result'] = 'Not Checked...'
        self.params['form'] = HelloForm(request.POST)
        return render(request, 'hello/index.html', self.params)