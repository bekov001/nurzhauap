from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from django.views.generic.edit import FormMixin
from .forms import TaskForm, RegisterForm, CommentForm
from .models import Task


# Create your views here.
def test(request):
    return render(request, "404/index.html")


def index(request):
    tasks = Task.objects.order_by('-id')
    data = {
        "title": "Главная страница",
        "tasks": tasks
    }
    return render(request, 'main/index.html', data)


class Detail(FormMixin, DetailView):
    model = Task
    template_name = 'main/detail.html'
    context_object_name = "task"
    form_class = CommentForm
    # success_msg = 'Комментарий успешно создан'
    success_url = ""

    def get_success_url(self, **kwargs):
        return reverse_lazy("post", kwargs={"pk": self.get_object().id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.article = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class PostUpdate(UpdateView):
    model = Task
    template_name = "main/create.html"
    form_class = TaskForm
    # fields = ["title", "task"]


class DeletePost(DeleteView):
    model = Task
    template_name = "main/delete.html"
    success_url = "/"
    form_class = TaskForm


def about(request):
    return render(request, 'main/about.html')


class CreateQuestion(CreateView):
    form_class = TaskForm
    template_name = "main/create.html"
    success_url = reverse_lazy("home")
    context_object_name = "form"


class RegisterUser(CreateView):
    form_class = RegisterForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # c_def = self.get_user_context(title="Регистрация")
    #     return dict(list(context.items))
# def detail(request, id):
#     task = Task.objects.all() .l
#     post = e
#         'id': id,
#         'task': task
#     }
#     return render(request, 'main/detail.html', post)