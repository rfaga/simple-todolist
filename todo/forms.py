from models import Task

### Forms
from django.forms.models import ModelForm

class TaskForm(ModelForm):

    class Meta:
        model = Task
        fields = ('title', 'description', 
                  'date', 'place', 'priority', )
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(TaskForm, self).__init__(*args, **kwargs)
        
    def save(self, commit=True):
        instance = super(TaskForm, self).save(commit=False)
        if self.user:
            instance.user = self.user
        if commit:
            instance.save()
        return instance
