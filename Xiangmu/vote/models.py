from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class question(models.Model):
    question_text=models.CharField(max_length=20,verbose_name='问题')
    class Meta():
        verbose_name='问题'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.question_text

# class chiceManage(models.Manager):
#     def incresevotes(self,id):
#         c=self.get(pk=id)
#         c.votes+=1
#         c.save()

class choice(models.Model):
    choice_text=models.CharField(max_length=20,verbose_name='选项描述')
    votes = models.IntegerField(default=0,verbose_name='得票数')
    question = models.ForeignKey("Question", on_delete=models.CASCADE)
    class Meta():
        verbose_name='选项'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.choice_text

class MyUser(User):
    url=models.URLField(blank=True,null=True,default='http://baidu.com')
    class Meta():
        verbose_name='用户'
        verbose_name_plural=verbose_name






