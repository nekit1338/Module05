import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

class Video:
    def __init__(self, title: str, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return

        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.log_in(nickname, password)

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(
                    password):
                self.current_user = user
                return
        print("Пользователь не найден")

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            flag = False
            for v in self.videos:
                if v.title == video.title:
                    flag = True
                    break
            if not flag:
                self.videos.append(video)

    def get_videos(self, word):
        result_of_search = []
        word = word.lower()
        for video in self.videos:
            if word in video.title.lower():
                result_of_search.append(video.title)
        return result_of_search

    def watch_video(self, title: str):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        for video in self.videos:
            if video.title.lower() == title.lower():
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return

                print(f"Просмотр видео {title} начат")
                while video.time_now < video.duration:
                    print(f"Просмотрено {video.time_now} секунд")
                    video.time_now += 1
                    time.sleep(1)
                video.time_now = 0
                print("Конец видео")
                return
        print(f"Видео {title} не найдено")


if __name__ == '__main__':
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
