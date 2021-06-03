from django.db import models

# Create your models here.


class Group(models.Model):
    """Group Model."""

    class Meta:
        """Group Model Meta."""

        db_table = "tb_groups"
        verbose_name_plural = "Групи"
        verbose_name = "Група"
    name = models.CharField("Назва групи", max_length=90)
    """Setup name and email fields types and lengths."""

    def __str__(self):
        """Print Author name."""
        return self.name


class Student(models.Model):
    """Student Model."""

    class Meta:
        """Student Model Meta."""

        db_table = "tb_students"
        verbose_name_plural = "Студенти"
        verbose_name = "Студент"
    name = models.CharField("Ім'я", max_length=30)
    surname = models.CharField("Прізвище", max_length=30, blank=True)
    grades_sum = models.IntegerField('Сума балів', default=0)
    email = models.EmailField("Пошта", max_length=80)
    group_id = models.ForeignKey("Group", on_delete=models.CASCADE, related_name='students')
    """Setup name and email fields types and lengths."""

    def __str__(self):
        """Print Student name."""
        return self.name

    def get_full_name(self):
        """Get Student Full Name."""
        return f'{self.name} {self.surname}'

    @property
    def full_name(self):
        """Print Student Full Name."""
        return f'{self.name} {self.surname}'


class Lecture(models.Model):
    """Material Model."""

    class Meta:
        """Material Model Meta."""

        db_table = "tb_lectures"
        verbose_name_plural = "Лекції"
        verbose_name = "Лекція"
    title = models.CharField("Тема лекції", max_length=90)
    description = models.TextField("Опис лекції", max_length=90)
    attachments = models.FileField('Матеріали', upload_to='../files/lectures/', blank=True)
    group_id = models.ForeignKey("Group", on_delete=models.CASCADE, related_name='lectures')
    """Setup name and email fields types and lengths."""

    def __str__(self):
        """Print Author name."""
        return self.title


class Task(models.Model):
    """Material Model."""

    class Meta:
        """Material Model Meta."""

        db_table = "tb_tasks"
        verbose_name_plural = "Задачі"
        verbose_name = "Задача"
    title = models.CharField("Назва задачі", max_length=90)
    description = models.TextField("Умова Задачі")
    testfile = models.FileField('Матеріали', upload_to='../files/tasks/', blank=True)

    group_id = models.ForeignKey("Group", on_delete=models.CASCADE, related_name='tasks')
    """Setup name and email fields types and lengths."""

    def __str__(self):
        """Print Author name."""
        return self.title


class Solution(models.Model):
    class Meta:
        """Material Model Meta."""

        db_table = "tb_solutions"
        verbose_name_plural = "Розв'язки"
        verbose_name = "Розв'язок"

    solution = models.FileField('Матеріали', upload_to='../files/tasks/', blank=True)

    task_id = models.ForeignKey("Task", on_delete=models.CASCADE, related_name='solutions')
    student_id = models.ForeignKey("Student", on_delete=models.CASCADE, related_name='solutions')
