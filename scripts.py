from random import choice
from datacenter.models import Lesson, Schoolkid, Mark, Chastisement


def fix_marks() -> None:
    """Исправляет оценки 2 и 3 на 5"""
    child = Schoolkid.objects.get(full_name__contains=' Фролов Иван Григорьевич')
    Mark.objects.filter(schoolkid=child).filter(points__in=[2, 3]).update(points=5)
    Chastisement.objects.filter(schoolkid=child).delete()
