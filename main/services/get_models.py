from main.models import Group, Task, Student, Lecture, Solution


def group_all():
    objects_all = Group.objects.all()
    return objects_all


def group_find(group_id: int) -> Group:
    return Group.objects.get(id=group_id)


def students_all():
    objects_all = Student.objects.all()
    return objects_all


def students_by_group(group_id):
    group = group_find(group_id)
    objects_all = students_all().filter(group_id=group)
    return objects_all


def student_find(student_id: int) -> Student:
    return Student.objects.get(id=student_id)


def lectures_all():
    objects_all = Lecture.objects.all()
    return objects_all


def lectures_by_group(group_id):
    group = group_find(group_id)
    objects_all = lectures_all().filter(group_id=group)
    return objects_all


def lecture_find(lecture_id: int) -> Lecture:
    return Lecture.objects.get(id=lecture_id)


def tasks_all():
    objects_all = Task.objects.all()
    return objects_all


def tasks_by_group(group_id):
    group = group_find(group_id)
    objects_all = tasks_all().filter(group_id=group)
    return objects_all


def task_find(task_id: int) -> Task:
    return Task.objects.get(id=task_id)




