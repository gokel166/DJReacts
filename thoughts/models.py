from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

CONDITIONS = (
    (1, 'Happy'),
    (2, 'Satisfactory'),
    (3, 'Okay'),
    (4, 'Mad'),
    (5, 'Confused')
)

# Create your models here.
class Thought(models.Model):
    user = models.ForeignKey(User, related_name='thoughts')
    record_at = models.DateTimeField(default=timezone.now, editable=False)
    condition = models.IntegerField(choices=CONDITIONS)
    notes = models.TextField(blank=True, default='')

def __str__(self):
    return '{}: {}'.format(self.recorded_at.strftime('%Y-%m-%d %H:%M:%S'), self.get_condition_display())