from django.http import HttpResponse
from django.views.generic import View

class IndexView(View):
    def get(self, request):
        return HttpResponse("get")
    def post(self, request):
        return HttpResponse("post")
    def put(self, request):
        return HttpResponse("put")
    def delete(self, request):
        return HttpResponse("delete")

