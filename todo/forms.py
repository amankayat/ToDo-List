from django import forms
from todo.models import todo_list
class addingtodo(forms.ModelForm):
    class Meta:
        model = todo_list
        fields = ('name','date')
        widgets = {
            "date":forms.DateInput(attrs={'type':'date'}),
        }
        