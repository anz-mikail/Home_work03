# 1 Создать двух пользователей (с помощью метода User.objects.create_user('username')).
user_1 = User.objects.create_user(username='Пользователь_1')
user_2 = User.objects.create_user(username='Пользователь_2')

# 2 Создать два объекта модели Author, связанные с пользователями.
Author.objects.create(authorUser=user_1)
Author.objects.create(authorUser=user_2)

# 3 Добавить 4 категории в модель Category.
Category.objects.create(name='категория_1')
Category.objects.create(name='категория_2')
Category.objects.create(name='категория_3')
Category.objects.create(name='категория_4')

# 4 Добавить 2 статьи и 1 новость.
Post.objects.create(author=Author.objects.get(pk=1), categoryType='NW', title='новость', text='новости недели')
Post.objects.create(author=Author.objects.get(pk=2), categoryType='AR', title='статья №1', text='недельная статья №1')
Post.objects.create(author=Author.objects.get(pk=2), categoryType='AR', title='статья №2', text='недельная статья №2')

# 5 Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
Post.objects.get(pk=1).postCategory.add(Category.objects.get(pk=1))
Post.objects.get(pk=1).postCategory.add(Category.objects.get(pk=2))
Post.objects.get(pk=2).postCategory.add(Category.objects.get(pk=3))
Post.objects.get(pk=2).postCategory.add(Category.objects.get(pk=4))
Post.objects.get(pk=3).postCategory.add(Category.objects.get(pk=4))

# 6 Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).
Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=1).authorUser, text='коментарий №1')
Comment.objects.create(commentPost=Post.objects.get(id=2), commentUser=Author.objects.get(id=1).authorUser, text='коментарий №2')
Comment.objects.create(commentPost=Post.objects.get(id=2), commentUser=Author.objects.get(id=2).authorUser, text='коментарий №3')
Comment.objects.create(commentPost=Post.objects.get(id=3), commentUser=Author.objects.get(id=2).authorUser, text='коментарий №4')

# 7 Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
Comment.objects.get(pk=1).like()
Comment.objects.get(pk=1).like()
Comment.objects.get(pk=1).dislike()
Comment.objects.get(pk=2).like()
Comment.objects.get(pk=2).like()
Comment.objects.get(pk=3).like()
Comment.objects.get(pk=4).dislike()
Post.objects.get(pk=1).like()
Post.objects.get(pk=2).dislike()
Post.objects.get(pk=3).like()
Post.objects.get(pk=3).like()

# 8 Обновить рейтинги пользователей.
Author.objects.get(pk=1).update_rating()
Author.objects.get(pk=2).update_rating()

# 9 Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
for i in Author.objects.order_by('-ratingAuthor')[:1]:
    i.authorUser
    i.ratingAuthor

# 10 Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
for i in Post.objects.order_by('-rating')[:1]:
     i.dateCreation.strftime('%d.%m.%Y %H:%M')
     i.author.authorUser.username
     i.rating
     i.title
     i.preview()

# 11 Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
for i in Comment.objects.order_by('-rating')[:1]:
     i.dateCreation.strftime('%d.%m.%Y %H:%M')
     i.commentUser.username
     i.rating
     i.text

