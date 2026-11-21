from django.db import models

statuses = [
    ('pending', 'To do'),
    ('in_progress', 'In Progress'),
    ('complated', 'Done')
]


priority = [
    ('low', 'Low'),
    ('mid', 'Mid'),
    ('high', 'High'),
    ('none', 'None')
]

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True ,null=True)

    status = models.CharField(max_length=100, choices=statuses, default='pending')
    prior = models.CharField(max_length=100, choices=priority, default='none')
    deadline = models.DateTimeField(blank=True, null=True)
    workers = models.ManyToManyField('auth.User', related_name='my_tasks', blank=True)

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(blank=True, null=True)

    attachment = models.FileField(upload_to='attach', null=True, blank=True)

    def __str__(self):
        return self.title


class Coment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField(max_length=5000)
    attachment = models.FileField(upload_to='comment_attachment/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author