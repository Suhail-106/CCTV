from django.shortcuts import render


def check(request):
    return render(request,'forcheck.html')

def checking(request):
    return render(request,'checkimg.html')