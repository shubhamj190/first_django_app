#this site is created by me

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # params={'name':'shubham','place':'ulhasnagar'}
    return render(request,'index.html')
    # return HttpResponse('<h1>Hello world</h1><br> <a href="/removepunc">remove punction</a> <br><a href="/capatalizetheword">capatial The first word</a>   <br><a href="/removeline">Remove the line</a> <br><a href="/charcount">char count</a>')

def analyze(request):
    djtext=request.POST.get('text','default')

    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    spaceremover=request.POST.get('spaceremover','off')
    charcount=request.POST.get('charcount','off')

    if removepunc=="on":
        analyzed=""
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Remove Punctuation','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyzed.html',params)

    if fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyzed.html', params)

    if newlineremover=="on":
        analyzed=""
        for char in djtext:
            if char!="\n"and char!="\r":
                analyzed=analyzed+char
            params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
            djtext=analyzed
        # return render(request, 'analyzed.html', params)

    if spaceremover=="on":
        analyzed=""
        for index, char in enumerate(djtext):
            if not( djtext[index] == " "and djtext[index+1]==" "):
                analyzed=analyzed+char
                params = {'purpose': 'Space removed', 'analyzed_text': analyzed}
        print(analyzed)
        djtext=analyzed
        # return render(request, 'analyzed.html', params)

    if charcount=="on":
        analyzed=len(djtext)
        params={'purpose': 'charcount','analyzed_text': analyzed}
        djtext=analyzed
        # return render(request,'analyzed.html',params)
        return render(request,'analyzed.html',params)
        
    else:
        return HttpResponse('Error')