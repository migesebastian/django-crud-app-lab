from django import forms
from .models import Book, Review

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'description']
        widgets = {
            'description': forms.Textarea(
                attrs={
                    'rows': 4,
                    'placeholder': 'Enter a brief description of the book'
                }
            ),
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'comment': forms.Textarea(
                attrs={
                    'rows': 3,
                    'placeholder': 'Write your review here'
                }
            ),
            'rating': forms.NumberInput(
                attrs={
                    'min': 1,
                    'max': 5,
                    'placeholder': 'Rate from 1 to 5'
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['rating'].widget.attrs.update({'class': 'form-control'})
        self.fields['comment'].widget.attrs.update({'class': 'form-control'})

