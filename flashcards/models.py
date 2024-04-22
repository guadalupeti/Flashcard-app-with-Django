from django.db import models

BOXES_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
)

class Cards(models.Model):
    question = models.CharField(max_length = 100)
    answer = models.CharField(max_length = 100)
    
    level = models.IntegerField(
        choices=BOXES_CHOICES,
        default=BOXES_CHOICES[0]
    )
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

