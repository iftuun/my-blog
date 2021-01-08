from django.shortcuts import render


def sum(req, a, b):
    sum1=a+b
    return render(req, 'sum.html', {'v': sum1})