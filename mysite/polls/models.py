from django.db import models

# Create your models here.


class Question(models.Model):
    # 问题
    l_question_text = models.CharField(max_length=100)
    # 提问日期
    l_date_publish = models.DateField('date published')


class Choice(models.Model):
    # 问题
    l_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # 选举
    l_choice_text = models.CharField(max_length=200)
    # 投票
    l_vote = models.IntegerField(default=0)
