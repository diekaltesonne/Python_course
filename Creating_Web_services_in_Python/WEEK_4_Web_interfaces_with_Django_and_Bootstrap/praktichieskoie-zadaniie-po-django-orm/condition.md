## Практическое задание по Django ORM
В этом задании вы научитесь работать с ORM
Для выполнения задания необходимо использовать шаблон проекта https://github.com/alexopryshko/coursera_assignment_tmp
Файл, который необходимо отредактировать db/query.py. В файле представлены шаблоны функций, которые нужно дополнить. Решение должно быть файлом query.py.

Предметная область – блоги и топики:
```Python
class User(models.Model):
   first_name = models.CharField(max_length=255)
   last_name = models.CharField(max_length=255)

class Blog(models.Model):
   title = models.CharField(max_length=255)
   author = models.ForeignKey(User)
   created = models.DateTimeField(default=timezone.now())

   subscribers = models.ManyToManyField(User, related_name='subscriptions')

class Topic(models.Model):
   title = models.CharField(max_length=255)
   blog = models.ForeignKey(Blog)
   author = models.ForeignKey(User)
   created = models.DateTimeField(default=timezone.now())

   likes = models.ManyToManyField(User, related_name='likes')
```
Необходимо написать запросы:
1. Создание (функция create):
* Создать пользователя first_name = u1, last_name = u1.
* Создать пользователя first_name = u2, last_name = u2.
* Создать пользователя first_name = u3, last_name = u3.
* Создать блог title = blog1, author = u1.
* Создать блог title = blog2, author = u1.
* Подписать пользователей u1 u2 на blog1, u2 на blog2.
* Создать топик title = topic1, blog = blog1, author = u1.
* Создать топик title = topic2_content, blog = blog1, author = u3, created = 2017-01-01.
* Лайкнуть topic1 пользователями u1, u2, u3.
2. Редактирование:
* Поменять first_name на uu1 у всех пользователей (функция edit_all).
* Поменять first_name на uu1 у пользователей, у которых first_name u1 или u2 (функция edit_u1_u2).
3. Удаление:
* удалить пользователя с first_name u1 (функция delete_u1).
* отписать пользователя с first_name u2 от блогов (функция unsubscribe_u2_from_blogs).
4. Найти топики у которых дата создания больше 2018-01-01 (функция get_topic_created_grated).
5. Найти топик у которого title заканчивается на content (функция get_topic_title_ended).
6. Получить 2х первых пользователей (сортировка в обратном порядке по id) (функция get_user_with_limit).
7. Получить количество топиков в каждом блоге, назвать поле topic_count, отсортировать по topic_count по возрастанию (функция get_topic_count).
8. Получить среднее количество топиков в блоге (функция get_avg_topic_count).
9. Найти блоги, в которых топиков больше одного (функция get_blog_that_have_more_than_one_topic).
10. Получить все топики автора с first_name u1 (функция get_topic_by_u1).
11. Найти пользователей, у которых нет блогов, отсортировать по возрастанию id (функция get_user_that_dont_have_blog).
12. Найти топик, который лайкнули все пользователи (функция get_topic_that_like_all_users).
13. Найти топики, у которы нет лайков (функция get_topic_that_dont_have_like).
