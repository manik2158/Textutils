from django.http import HttpResponse,Http404
from django.shortcuts import render

def index(request):
    return render(request, 'index.html',{})

def analyze(request):
    djtext=(request.POST.get('text','default'))
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcounter = request.POST.get('charcounter','off')

    if removepunc== "on":
        punctuations= '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analysed=""
        for char in djtext:
            if char not in punctuations:
                analysed+=char
        djtext = analysed
        params={'purpose':'Remove Punctuations','analyzed_text':analysed}


    if(fullcaps == "on"):
        analysed=""
        for char in djtext:
            analysed+=char.upper();
        djtext = analysed
        params={'purpose':'Capitalisation of words', 'analyzed_text':analysed}


    if(newlineremover== "on"):
        analysed=""
        for char in djtext:
            if char !="/n" and char!="/r":
                analysed+=char
        djtext=analysed
        params={'purpose':'Remove new lines in strings', 'analyzed_text':analysed}


    if (extraspaceremover == "on"):
        analysed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index]== " " and djtext[index+1]==" "):
                analysed+=djtext[index]
        djtext = analysed
        params = {'purpose': 'Remove extra space ', 'analyzed_text': analysed}


    if (charcounter == "on"):
        count = 0
        for char in djtext:
            if not(char==" "):
                count+=1
            else:
                pass
        string = "Your number of characters in the string is "+str(count)
        params = {'purpose': 'Remove extra space ', 'analyzed_text': string}

    if (removepunc!="on" and newlineremover!= "on" and fullcaps!="on" and extraspaceremover!="on"):
        return HttpResponse("<h1> Please select one of the below options so that the sie can perform some operations</h1>")
    return render(request, 'analyze.html', params)
