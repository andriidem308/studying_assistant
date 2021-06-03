from main.models import Group


def group_all():
    objects_all = Group.objects.all()
    return objects_all


def group_find(group_id: int) -> Group:
    return Group.objects.get(id=group_id)
