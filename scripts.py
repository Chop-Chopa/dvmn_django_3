from datacenter.models import Schoolkid, Mark, Chastisement, Lesson, Commendation
import random


COMPLIMENTS = [
    "Молодец!",
    "Отлично!",
    "Хорошо!",
    "Гораздо лучше, чем я ожидал!",
    "Ты меня приятно удивил!",
    "Великолепно!",
    "Прекрасно!",
    "Ты меня очень обрадовал!",
    "Именно этого я давно ждал от тебя!",
    "Сказано здорово – просто и ясно!",
    "Ты, как всегда, точен!",
    "Очень хороший ответ!",
    "Талантливо!",
    "Ты сегодня прыгнул выше головы!",
    "Я поражен!",
    "Уже существенно лучше!",
    "Потрясающе!",
    "Замечательно!",
    "Прекрасное начало!",
    "Так держать!",
    "Ты на верном пути!",
    "Здорово!",
    "Это как раз то, что нужно!",
    "Я тобой горжусь!",
    "С каждым разом у тебя получается всё лучше!",
    "Мы с тобой не зря поработали!",
    "Я вижу, как ты стараешься!",
    "Ты растешь над собой!",
    "Ты многое сделал, я это вижу!",
    "Теперь у тебя точно все получится!"
]

def get_schoolkid(name):
    try:
        return Schoolkid.objects.get(full_name__contains=name)
    except Schoolkid.DoesNotExist:
        print("Ученик не найден. Введите корректное ФИО")
    except Schoolkid.MultipleObjectsReturned:
        print("Найдено несколько учеников. Уточните ФИО")
    return None

def fix_marks(schoolkid):
    child = get_schoolkid(schoolkid)
    if not child:
        return
    student = Mark.objects.filter(schoolkid=child,points__in=['2','3']).update(points='5')


def remove_chastisements(schoolkid):
    child = get_schoolkid(schoolkid)
    if not child:
        return
    deleted_count = Chastisement.objects.filter(schoolkid=child).delete()

def create_commendation(schoolkid, item):
    child = get_schoolkid(schoolkid)
    if not child:
        return
    lessons = Lesson.objects.filter(year_of_study=child.year_of_study,group_letter=child.group_letter,subject__title=item).order_by('-date')
    if not lessons.exists():
        print('Предмет не найден')
        return
    lesson = lessons.first()
    random_compliment = random.choice(COMPLIMENTS)
    commendation = Commendation.objects.create(text=random_compliment,created=lesson.date, schoolkid = child, subject = lesson.subject, teacher = lesson.teacher)

