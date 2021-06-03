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
    name = models.CharField("Ім'я", max_length=90)
    surname = models.CharField("Прізвище", max_length=90, blank=True)
    group = models.ForeignKey("Group", models.CASCADE, related_name='students')
    email = models.EmailField("Пошта", max_length=80)
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


class Material(models.Model):
    """Material Model."""

    class Meta:
        """Material Model Meta."""

        db_table = "tb_materials"
        verbose_name_plural = "Матеріали"
        verbose_name = "Матеріал"
    title = models.CharField("Заголовок", max_length=90)
    description = models.TextField("Описание поста", max_length=90)
    group = models.ForeignKey("Group", models.CASCADE, related_name='materials')
    """Setup name and email fields types and lengths."""

    def __str__(self):
        """Print Author name."""
        return self.title

