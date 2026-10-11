from django import forms
from .models import Article, Comment

class CreateArticleForm(forms.ModelForm):
  '''A form to add an Article to the database'''
  
  class Meta:
    '''associate this form with a model from our database'''
    model = Article
    fields = ['author', 'title', 'text', 'image_url']
    
class UpdateArticleForm(forms.ModelForm):
  '''A form to handle an update to an Article'''
  
  class Meta:
    '''associate this form with a model in our database'''
    model = Article
    fields = ['title', 'text', ]  # which fields from model should we use

class CreateCommentForm(forms.ModelForm):
    '''A form to add a Comment to the database.'''
    
    class Meta:
        '''associate this form with the Comment model; select fields.'''
        model = Comment
        fields = ['author', 'text', ]  # which fields from model should we use