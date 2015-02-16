from django import http
from django.shortcuts import render, redirect

import math

import shorturl.views
from shorturl.main.models import LongURL

class URLShortener(shorturl.views.BaseView):
    """
       View for shortening the url
    """
    alphabet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_'
    base = len(alphabet)

    def get(self, request):
        return self.render(request, 'shorturl.main/index.html')
    
    def post(self, request):
        url = list(request.POST.keys())[0]

        try:
            url_obj = LongURL.objects.get(long_url=url)
            return http.HttpResponse(self.encode(url_obj.id), content_type="text/plain")
        except LongURL.DoesNotExist:
            url_code = self.encode(self.new_id())
            url_obj = LongURL.objects.create(long_url=url)
            url_obj.save()
            return http.HttpResponse(url_code, content_type="text/plain")
        

    def encode(self, obj_id):
        code = ''
        num = obj_id

        if num == 0:
            return '1' # no urlobjects -> id starts at 1,

        while num > 0:
            code = self.alphabet[num % self.base] + code
            num = math.floor(num / self.base)
        return code

    def new_id(self):
        ordered_ids = LongURL.objects.all().order_by("-id")
        url_id = 0

        # Increment the id if necessary
        if len(ordered_ids) > 0:
            url_id = ordered_ids[0].id + 1
            
        return url_id
        

class Redirect(shorturl.views.BaseView):
    """
       Redirects user to the original URL (or 404 if not found)
    """
    
    alphabet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_'
    base = len(alphabet)

    def get(self, request, code):
        url_id = self.get_id(code)

        try:
            long_url = LongURL.objects.get(id=url_id)
        except LongURL.DoesNotExist:
            raise http.Http404
        
        return redirect(long_url.long_url)

    def get_id(self, code):
        num = 0
        for i in range (0, len(code)):
            num = num * self.base + self.alphabet.index(code[i])
        return num
