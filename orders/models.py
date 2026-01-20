from django.db import models

# Create your models here.
class Order(models.Model):
    STATUS_CHOICES = [
        ('new', 'Нове замовлення'),
        ('in_progress', 'В обробці'),
        ('done', 'Завершено'),
        ('rejected', 'Відхилено'),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField()
    project_description = models.TextField(verbose_name='Опис проекту')
    budget = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Бюджет (USD)')
    deadline = models.CharField(max_length=100, verbose_name='Терміни реалізації')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'

    def __str__(self):
        return f"{self.pk}: Замовлення від {self.name} ({self.status})"
