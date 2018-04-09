from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField('Texto da questão', max_length=200)
    pub_date = models.DateTimeField('Data de publicação')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField('Texto da escolha', max_length=200)
    votes = models.IntegerField('Votos', default=0)

    def __str__(self):
        return "{} - {}".format(self.question, self.choice_text)
