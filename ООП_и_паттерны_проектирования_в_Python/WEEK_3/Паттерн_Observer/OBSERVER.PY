from abc import ABC, abstractmethod


class ObservableEngine(Engine):
    def __init__(self):
        self.__subscribers = set()

    def subscribe(self,subscriber):
        self.__subscribers.add(subscriber)

    def unsubscribe(self,subscriber):
        self.__subscribers.remove(subscriber)

    def notify(self,achievement):
        for subscriber in self.__subscribers:
            subscriber.update(achievement)


class AbstractObserver(ABC):
    @abstractmethod
    def update(self):
        pass


class ShortNotificationPrinter(AbstractObserver):

    def __init__(self):
        self.achievements = set()

    def update(self,achievement):
         self.achievements.add(achievement["title"])

class  FullNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = list()

    def update(self,achievement):
        k = 0
        for i in self.achievements:
            if achievement["title"] == i["title"]:
                k += 1
        if k==0:
            self.achievements.append(achievement)
