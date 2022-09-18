from random import choice
from datacenter.models import Lesson, Schoolkid, Mark, Chastisement


def fix_marks() -> None:
    """Исправляет оценки 2 и 3 на 5"""
    child = Schoolkid.objects.get(full_name__contains=' Фролов Иван Григорьевич')
    Mark.objects.filter(schoolkid=child).filter(points__in=[2, 3]).update(points=5)
    Chastisement.objects.filter(schoolkid=child).delete()

    
def create_commendation(praises: list, child_name: str, lesson: str) -> None:
    """Добавляет случайные хвалебные коментарии по определенному предмету"""
    child = Schoolkid.objects.get(full_name__contains=child_name)
    last_lesson = Lesson.objects.filter(
        year_of_study=child.year_of_study,
        group_letter=child.group_letter,
        subject__title__contains=lesson
    ).order_by('-date').first()

    praise = choice(praises)
    chastisement_child = Chastisement.objects.filter(schoolkid=child, subject__title__contains=last_lesson)

    chastisement_child.create(
        text=praise,
        created=last_lesson.date,
        teacher=last_lesson.teacher,
        schoolkid=child,
        subject=last_lesson.subject
    )


praises = [
    'Молодец!',
    'Отлично!',
    'Хорошо!',
    'Гораздо лучше, чем я ожидал!',
    'Ты меня приятно удивил!',
    'Великолепно!',
    'Прекрасно!',
    'Ты меня очень обрадовал!',
    'Именно этого я давно ждал от тебя!',
    'Сказано здорово – просто и ясно!',
    'Ты, как всегда, точен!',
    'Очень хороший ответ!',
    'Талантливо!',
    'Ты сегодня прыгнул выше головы!',
    'Я поражен!',
    'Уже существенно лучше!',
    'Потрясающе!',
    'Замечательно!',
    'Прекрасное начало!',
    'Так держать!',
    'Ты на верном пути!',
    'Здорово!',
    'Это как раз то, что нужно!',
    'Я тобой горжусь!',
    'С каждым разом у тебя получается всё лучше!',
    'Мы с тобой не зря поработали!',
    'Я вижу, как ты стараешься!',
    'Ты растешь над собой!',
    'Ты многое сделал, я это вижу!',
    'Теперь у тебя точно все получится!'
]
