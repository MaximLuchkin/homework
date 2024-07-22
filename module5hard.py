from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:

    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)
            else:
                return print('Видео с таким названием уже существует')

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and user.password == hash(password):
                self.current_user = nickname
            else:
                return print('Не верное имя пользователя или пароль')

    def register(self, nickname, password, age):
        if any(user.nickname == nickname for user in self.users):
            print(f"Пользователь {nickname} уже существует.")
        else:
            nickname = User(nickname, password, age)
            self.users.append(nickname)
            self.current_user = nickname

    def log_out(self):
        self.current_user = None

    def get_videos(self, search_title):
        return [video.title for video in self.videos if search_title.lower() in video.title.lower()]

    def watch_video(self, search_video):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
        else:
            search_video = next((video for video in self.videos if video.title == search_video), None)
            if search_video:
                if search_video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return

                while search_video.time_now < search_video.duration:
                    print(search_video.time_now)
                    search_video.time_now += 1
                    sleep(1)
                print('Конец Видео')
            else:
                print('Видео с таким названием не существует')




ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

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
