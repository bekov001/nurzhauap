from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, Textarea, FileInput, \
    PasswordInput, CharField, Select
from .models import Task, Comments


class TaskForm(ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'task', "img", "theme"]

        widgets = {"title": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите название',

        }), "task": Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Введите описание',

        }), "theme": Select(attrs={
            "class": "form-select",
            # "max-width": "200"
        })
        }


class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields["password2"].help_text = ""

    class Meta:
        model = User
        fields = ['username', "password1", "password2"]
        widgets = {
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите логин'
            }),
            "password1": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите пароль'
            }),
            "password2": TextInput(attrs={
                'class': 'form-сontrol',
                'placeholder': 'Повторите пароль'
            })
        }


class CommentForm(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for f in self.fields:
    #         self.fields[f].widget.attrs["class"] = "form-input"
    #     self.fields["text"].widget.attrs["class"] = Textarea(attrs={
    #         "class": "form-input",
    #         'cols': 20,
    #         'rows': 10
    #     })

    class Meta:
        model = Comments
        fields = ("text", "img")
        widgets = {
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание',
                "rows": 4,
            })
        }
