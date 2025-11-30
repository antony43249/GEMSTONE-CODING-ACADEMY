from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages


def marketing_detail(request, pk):
    return render(request, 'marketing/detail.html', {'pk': pk})


def marketing_create(request):
    class CampaignForm(forms.Form):
        title = forms.CharField(max_length=200)
        date = forms.DateField(required=False)

    if request.method == 'POST':
        form = CampaignForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Campaign saved (placeholder).')
            return redirect('marketing-home')
    else:
        form = CampaignForm()
    return render(request, 'marketing/create.html', {'form': form})

def marketing_home(request):
    return render(request, 'marketing/marketing.html')
