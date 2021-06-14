from django.views.generic import ListView, CreateView
from django.urls import reverse

from .models import Thread, Comment
from .forms import ThreadCreateForm, ThreadCommentCreateForm

class IndexView(ListView):
    template_name = 'index.html'
    queryset = Thread.objects.all().order_by('-updated')
    context_object_name = 'threads'
    paginate_by = 5

index = IndexView.as_view()


class ThreadCommentList(ListView):
    template_name = 'thread/comment/list.html'
    queryset = None
    context_object_name = 'comments'
    paginate_by = 10

    def get_queryset(self):
        self.thread_id = self.kwargs['pk']
        comments = Comment.objects.filter(thread_id=self.thread_id).order_by('-created')
        return comments

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        thread = Thread.objects.get(id=self.thread_id)
        context['thread'] = thread
        return context

thread_comment_list = ThreadCommentList.as_view()


class ThreadCreateView(CreateView):
    template_name = 'thread/create.html'
    form_class = ThreadCreateForm
    success_url = None

    def form_valid(self, form):
        thread = form.save() # 作成されたthreadにアクセスする
        self.success_url = reverse('board:thread_comment_list', kwargs={'pk': thread.id})
        return super().form_valid(form)

thread_create = ThreadCreateView.as_view()


class ThreadCommentCreateView(CreateView):
    template_name = 'thread/comment/create.html'
    model = Comment
    form_class = ThreadCommentCreateForm
    success_url = None

    def form_valid(self, form):
        comment = form.save(commit=False)
        self.thread_id = self.kwargs['pk']
        comment.thread_id = self.thread_id
        comment.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        success_url = reverse('board:thread_comment_list', kwargs={'pk':self.thread_id})
        return success_url

thread_comment_create = ThreadCommentCreateView.as_view()