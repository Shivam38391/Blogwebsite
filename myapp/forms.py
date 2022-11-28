from  django import forms
from .models import Comments

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = [
            'name', 'content', 'website','email',
        ]
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs["placeholder"] = 'Type your comment'
        self.fields['name'].widget.attrs["placeholder"] = 'Type your name'
        self.fields['email'].widget.attrs["placeholder"] = 'Type your email'
        self.fields['website'].widget.attrs["placeholder"] = 'enter your website'
        
    