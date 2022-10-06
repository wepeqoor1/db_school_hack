from random import choice
from datacenter.models import Lesson, Schoolkid, Mark, Chastisement

PRAISES = [
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


class SchoolChild:
    def __init__(self, child_name: str):
        self.child_name = child_name

    def fix_marks(self) -> None:
        """
        Исправляет оценки 2 и 3 на 5
        """
        child = Schoolkid.objects.get(full_name__contains=self.child_name)
        Mark.objects.filter(schoolkid=child).filter(points__in=[2, 3]).update(
            points=5)

    def delete_chastisements(self) -> None:
        """
        Удаляет плохие замечания
        """
        Chastisement.objects.filter(schoolkid=self.child_name).delete()

    def create_commendation(self, lesson: str) -> None:
        """
        Добавляет случайные хвалебные коментарии по определенному предмету
        """
        child = Schoolkid.objects.get(full_name__contains=self.child_name)
        last_lesson = Lesson.objects.filter(
            year_of_study=child.year_of_study,
            group_letter=child.group_letter,
            subject__title__contains=lesson
        ).order_by('-date').first()

        praise = choice(PRAISES)
        chastisement_child = Chastisement.objects.filter(
            schoolkid=child,
            subject__title__contains=last_lesson
        )

        chastisement_child.create(
            text=praise,
            created=last_lesson.date,
            teacher=last_lesson.teacher,
            schoolkid=child,
            subject=last_lesson.subject
        )


def main():
    child_name = 'Фролов Иван Григорьевич'
    lesson = 'Музыка'
    school_child = SchoolChild(child_name=child_name)
    school_child.fix_marks()
    school_child.create_commendation(lesson)
    school_child.delete_chastisements()


if __name__ == '__main__':
    main()
