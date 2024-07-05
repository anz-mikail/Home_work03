from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.conf import settings
from .models import Post, Subscription, User
import datetime


#html_message = strip_tags(render_to_string('mail_template.html', {'context': 'values'}))

@shared_task
def send_mail(pk):
    post = Post.objects.get(id=pk)
    categories = post.category.all()

    emails = set(User.objects.filter(subscriptions__category__in=categories).values_list("email", flat=True))

    subject = f"Новый пост в категории: {', '.join([f'{cat}' for cat in categories])}"

    html_content = (f'<p><b>письмо с таски:</b> {post.title}</p>'
                    f'<p><b>Содержание:</b> {post.text[0:123]}</p>'
                    f'<p><b>Автор:</b> {post.user}</p>'
                    f'<a href="http://127.0.0.1:8000{post.get_absolute_url()}">'
                    f'Ссылка на пост tasks</a>'
                    )
    for email in emails:
        print('email ', email)
        msg = EmailMultiAlternatives(subject, html_content, None, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()


@shared_task()
def send_mail_weekly():
    one_week_later = datetime.datetime.now() - datetime.timedelta(weeks=1)
    posts = Post.objects.filter(dateCreation__gt=one_week_later)
    category = set(posts.values_list('postCategory', flat=True))
    subscribers = set(Subscription.objects.filter(category__in=category).values_list('user__email', flat=True))

    html_content = render_to_string(
        'daily_post.html',
        {
            'link': f'http://127.0.0.1:8000',
            'posts': posts
        }
    )

    msg = EmailMultiAlternatives(
        subject=f"Новости недели",
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()
