from django import forms

from .models import Topic

class TopicForm(forms.ModelForm):
    # The `Meta` class tells Django which model to base the form on and which fields to
    # include in the form.
    class Meta:
        model = Topic
        fields = ['text']
        # Do not generate a lbale for the `text` field.
        labels = {'text': ''}