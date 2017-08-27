from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Autor, Post


class BaseUserCreationForm(UserCreationForm):
    title = None
    #email = forms.EmailField(label=_('email address'))

    class Meta:
        model = User
        exclude = (
            'last_login',
            'is_staff',
            'is_superuser',
            'date_joined',
            'groups',
            'user_permissions',
            'password',
            'is_active',
            'email'
        )
        fields = '__all__'


class FormAllFields(forms.ModelForm):

    form_title = 'None'

    class Meta:
        model = None
        fields = '__all__'


class AutorForm(BaseUserCreationForm):
    class Meta(BaseUserCreationForm.Meta):
        model = Autor


class PostForm(FormAllFields):
    autor = forms.ModelChoiceField(
        queryset=Autor.objects.all(),
        empty_label=None
    )

    class Meta(FormAllFields.Meta):
        model = Post

    def __init__(self, *args, **kwargs):
        autor = kwargs.pop('autor', None)
        super().__init__(*args, **kwargs)
        self.fields['autor'].queryset = Autor.objects.filter(id=autor.id)


