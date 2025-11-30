from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages


class ProjectForm(forms.Form):
    title = forms.CharField(max_length=200)
    summary = forms.CharField(widget=forms.Textarea, required=False)


def project_detail(request, pk):
    # Minimal detail view; real project model not defined in this repo
    return render(request, 'projects/detail.html', {"pk": pk})


def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Project submitted (placeholder).')
            return redirect('projects-home')
    else:
        form = ProjectForm()
    return render(request, 'projects/create.html', {'form': form})

def projects_home(request):
    return render(request, 'projects/projects.html')
