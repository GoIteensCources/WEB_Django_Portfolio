from django.db import models

# Create your models here.
"""
Модель Project (назва, опис, технології, дата, зображення, GitHub посилання)
 Модель Skill (назва, рівень володіння, категорія)
 Модель Experience (посада, компанія, період, опис)
"""

class Project(models.Model):
    title = models.CharField()
    description = models.TextField()
    technologies = models.CharField(help_text="через кому: Python, JS, Postgres")
    data = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to="projects/", null=True, blank=True)
    github_url = models.URLField(null=True, blank=True)

    class Meta:
        ordering = ["-data", 'title']
        verbose_name = "Проект"
        verbose_name_plural = "Проекти"
        
    def __str__(self) -> str:
        return self.title


class Skill(models.Model):
    CATEGORY_CHOISE = [
        ("soft", "Soft"),
        ("frontend", 'Frontend'),
        ("backend", "Backend"),
        ("devops", "DevOps")
    ]

    name = models.CharField()
    level = models.PositiveSmallIntegerField(default=50, help_text="0-100")    # 0-100 
    category = models.CharField(choices=CATEGORY_CHOISE, default='backend')
    
    class Meta:
        ordering = ["-level", 'name']
        verbose_name = "Навик"
        verbose_name_plural = "Навички"
        
    def __str__(self) -> str:
        return f"[{self.name}]: {self.level}"
    

class Experience(models.Model):
    position = models.CharField()
    company = models.CharField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['-start_date', 'company']
        verbose_name = "Досвід"
        verbose_name_plural = "Досвід"
        
    def __str__(self) -> str:
        period = f"{self.start_date} - {self.end_date}" if self.end_date else f"{self.start_date} - Present"
        return f"[{self.position}] in {self.company} ({period})"
    