from django.db import models

# Create your models here.
class question(models.Model):
    question_text=models.CharField(max_length=20,verbose_name='问题')
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
    def __str__(self):
        return self.choice_text





