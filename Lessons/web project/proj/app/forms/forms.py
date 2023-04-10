from django import forms
from app.models import Post
from django.core.exceptions import ValidationError

class AddPost(forms.Form):

    title = forms.CharField(max_length=100, label="Title")
    subtitle = forms.CharField(max_length=250)
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'text'}))
    image = forms.ImageField()
    post_type = forms.ChoiceField(choices=Post.POST_TYPES)

    def clean_subtitle(self):
        title_data = self.cleaned_data['title']
        subtitle_data = self.cleaned_data['subtitle']

        if title_data == subtitle_data:
            raise ValidationError("title and subtitle should not be the same!")
        
        return subtitle_data
    

class AddPostModelForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'content', 'image', 'post_type')
