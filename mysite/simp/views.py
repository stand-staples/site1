from django.shortcuts import render

# Create your views here.
def index_view(request):
  context = {'message': "Hello world"}
  template = 'simp/index.html'
  return render(request, template, context)

