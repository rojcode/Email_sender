from django.core.mail import send_mail
from django.shortcuts import render,get_object_or_404

# Create your views here.
from email_sender.forms import ShareForm
from email_sender.models import Post


def home(request):
    posts = Post.objects.all()
    return render(request,'home.html',{'posts': posts})


def post_detail(request,slug):
    post = get_object_or_404(Post,slug=slug)
    sent = False

    if request.method == 'POST':
        # Form was submitted
        form = ShareForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '✍️ {}--({})'.format(cd['subject'],post.title)
            message = '{}, Read this article on the website:\n{}.\n {}'.format(cd['body'],post.des,post_url)
            my_email = 'webmobin80@gmail.com'
            send_mail(subject,message,my_email,[cd['email']],fail_silently=False)
            sent = True
            if sent:
                return render(request,'status/Successful.html',{'cd': cd,'sent': sent})
    else:
        form = ShareForm()

    return render(request,'detail/detail.html',{'post': post,'form': form,'sent': sent})
