from django import forms
from .models import Item
INPUT_CLASSES='mt-6 w-full py-4 px-6 rounded-xl bg-gray-200 font-semibold shadow-md hover:bg-gray-400 transition duration-300 focus:outline-none focus:ring-2 focus:ring-blue-400'
class NewItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=('category','name', 'description', 'pricing','image')
        widgets={
            'category':forms.Select(attrs={
                'class':INPUT_CLASSES
            }),
            'name':forms.TextInput(attrs={
                'class':INPUT_CLASSES,
                
            }),
            'description':forms.Textarea(attrs={
                'class':INPUT_CLASSES
            }),
            'pricing':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'image':forms.FileInput(attrs={
                'class':INPUT_CLASSES
            })
        }
class EditItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=('name', 'description', 'pricing','image','is_sold')
        widgets={
            'category':forms.Select(attrs={
                'class':INPUT_CLASSES
            }),
            'name':forms.TextInput(attrs={
                'class':INPUT_CLASSES,
                
            }),
            'description':forms.Textarea(attrs={
                'class':INPUT_CLASSES
            }),
            'pricing':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'image':forms.FileInput(attrs={
                'class':INPUT_CLASSES
            })
        }