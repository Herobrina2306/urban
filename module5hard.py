from time import sleep

class User:
    list_Us = []

    def __new__(cls, *args):
        cls.list_Us.append(args)
    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = hash(password)
        self.age = int(age)


class Video:

    list_Vi = []
    def __new__(cls, *args, **kwargs):
        cls.list_Vi.append(list(args))
        if kwargs:
            for v in kwargs.values():
                cls.list_Vi[-1].append(v)
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = str(title)
        self.duration = int(duration)
        self.time_now = int(time_now)
        self.adult_mode = bool(adult_mode)


class UrTube:
    def __init__(self):
        self.users = User.list_Us
        self.videos = Video.list_Vi
        self.current_user = None

    def log_in(self, nickname, password):
        if nickname in self.users:
            if hash(password) == self.users[nickname]:
                self.current_user = nickname
            else:
                print('Пароли не совпадают')
        else:
            print('Такого пользователя не существует')


    def register(self, nickname, pssword, age):
        if len(self.users) == 0:
            User(nickname, pssword, age)
            self.current_user = nickname
        else:
            for i in self.users:
                if nickname in i:
                    print(f'Пользователь {nickname} уже существует')
                else:
                    User(nickname, pssword, age)
                    self.current_user = nickname
                    break


    def log_out(self):
        self.current_user = None

    def add(self, *other):
        for i in other:
            if isinstance(i, Video):
                i = list(i)
                if i[0] not in self.videos:
                    self.videos.append(i)


    def get_videos(self, request):
        str_ = str(request).lower()
        lis = []
        fin = []
        for i in range(len(self.videos)):
            m = str(self.videos[i][0]).lower()
            lis.append(m)
        for j in range(len(lis)):
            if str_ in lis[j]:
                fin.append(self.videos[j][0])
        if len(fin) > 0:
            return fin
        else: pass

    def watch_video(self, name_video):
        video = None
        for i in self.videos:
            if name_video == i[0]:
                video = i
        if video == None:
            exit()
        else:
            if self.current_user == None:
                print('Войдите в аккаунт, чтобы смотреть видео')
            else:
                if True in video:
                    for i in self.users:
                        if self.current_user in i:
                            if i[2] < 18:
                                print('Вам нет 18 лет, пожалуйста покиньте страницу')
                            else:
                                i = 0
                                while i < video[1]:
                                    print(f'{i} ', end = '')
                                    sleep(1)
                                    i += 1
                                print('Конец видео')




ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)


# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
#
 # Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')















