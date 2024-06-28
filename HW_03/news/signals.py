from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.contrib.auth.models import User

from .models import Post, PostCategory

@receiver(m2m_changed, sender=PostCategory)
def post_created(instance, **kwargs):
    if not kwargs['action'] == 'post_add':
        return

    emails = User.objects.filter(
        subscriptions__category__in=instance.postCategory.all()
    ).values_list('email', flat=True)

    subject = f'Новость в категории {instance.postCategory.all()}'

    text_content = (
        f'новость: {instance.title}\n'
        f'Ссылка на новость: http://127.0.0.1:8000{instance.get_absolute_url()}'
    )
    html_content = (
        f'Пост: {instance.title}<br>'
        f'<a href="http://127.0.0.1{instance.get_absolute_url()}">'
        f'Ссылка на новость</a>'
    )
    for email in emails:
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

