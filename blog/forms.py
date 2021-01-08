from django import forms
from django.contrib.auth.models import User

class ShareWithEmailForm(forms.Form):
    name = forms.CharField(max_length=50, initial = User.objects.filter(is_active=True).values_list('username', flat=True).get())
    email = forms.EmailField(initial = User.objects.filter(is_active=True).values_list('email', flat=True).get())
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)