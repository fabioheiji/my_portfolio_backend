from django.db import models

# Create your models here.

class Message(models.Model):
    emailMessage = models.EmailField('Lead email',default='email@email.com')
    nameMessage = models.TextField('Lead name')
    messageMessage = models.TextField('Lead message')
    pub_date = models.DateTimeField(verbose_name='Date of published message',auto_now_add=True)

    def __str__(self):
        return f"Message: {self.messageMessage[:70]} ..."