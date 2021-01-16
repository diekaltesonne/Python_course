# =============================================================================
# начало секции ВАШ КОД
# =============================================================================
# Поместите в этой секции реализацию классов AbstractEffect, AbstractPositive,
# AbstractNegative, Berserk, Blessing, Curse, EvilEye, Weakness из вашего
# решения
from abc import ABC, abstractmethod
class AbstractEffect(ABC,Hero):

    def __init__(self, base):
        self.base = base

    @abstractmethod
    def get_positive_effects(self):
        pass

    @abstractmethod
    def get_negative_effects(self):
        pass

    @abstractmethod
    def get_stats(self):
        pass

class AbstractNegative(AbstractEffect):

    @abstractmethod
    def get_stats(self):
        pass
    @abstractmethod
    def get_negative_effects(self):
        pass

    def get_positive_effects(self):
        return self.base.get_positive_effects().copy()

class AbstractPositive(AbstractEffect):

    @abstractmethod
    def get_positive_effects(self):
        pass
    @abstractmethod
    def get_stats(self):
        pass
    def get_negative_effects(self):
        return self.base.get_negative_effects().copy()

#увеличивает все основные характеристики на 2.
class Blessing(AbstractPositive):
    def get_positive_effects(self):
        r= self.base.get_positive_effects()
        r.append("Blessing")
        return r.copy()


    def get_stats(self):
        r = self.base.get_stats()
        r["Strength"] = r["Strength"]+2
        r["Agility"] = r["Agility"]+2
        r["Luck"] = r["Luck"]+2
        r["Endurance"] = r["Endurance"]+2
        r["Perception"] = r["Perception"]+2
        r["Charisma"] = r["Charisma"]+2
        r["Intelligence"] = r["Intelligence"]+2
        return r.copy()

# Берсерк (Berserk) -
# Увеличивает характеристики: Сила, Выносливость, Ловкость, Удача на 7;
# уменьшает характеристики: Восприятие, Харизма, Интеллект на 3;
# количество единиц здоровья увеличивается на 50.

class Berserk(AbstractPositive):

    def get_positive_effects(self):
        r= self.base.get_positive_effects()
        r.append("Berserk")
        return r

    def get_stats(self):

        r = self.base.get_stats()

        r["HP"] = r["HP"]+50
        r["Strength"] = r["Strength"]+7
        r["Agility"] = r["Agility"]+7
        r["Luck"] = r["Luck"]+7
        r["Endurance"] = r["Endurance"]+7
        r["Perception"] = r["Perception"]-3
        r["Charisma"] = r["Charisma"]-3
        r["Intelligence"] = r["Intelligence"]-3


        return r.copy()

#Слабость (Weakness)
#уменьшает характеристики: Сила, Выносливость, Ловкость на 4.
class Weakness(AbstractNegative):

    def get_negative_effects(self):
        r = self.base.get_negative_effects()
        r.append("Weakness")
        return r.copy()

    def get_stats(self):
        r = self.base.get_stats()
        r["Strength"] = r["Strength"]-4
        r["Agility"] = r["Agility"]-4
        r["Endurance"] = r["Endurance"]-4
        return r.copy()


# Проклятье (Curse) -
# уменьшает все основные характеристики на 2.
class Curse(AbstractNegative):

    def get_negative_effects(self):

        r = self.base.get_negative_effects()
        r.append("Curse")
        return r.copy()

    def get_stats(self):
        r = self.base.get_stats()
        r["Strength"] = r["Strength"]-2
        r["Agility"] = r["Agility"]-2
        r["Luck"] = r["Luck"]-2
        r["Endurance"] = r["Endurance"]-2
        r["Perception"] = r["Perception"]-2
        r["Charisma"] = r["Charisma"]-2
        r["Intelligence"] = r["Intelligence"]-2
        return r.copy()

# Сглаз (EvilEye) -
# уменьшает  характеристику Удача на 10.
class EvilEye(AbstractNegative):

    def get_negative_effects(self):
        r = self.base.get_negative_effects()
        r.append("EvilEye")
        return r.copy()

    def get_stats(self):
        r = self.base.get_stats()
        r["Luck"] = r["Luck"]-10
        return r.copy()

# =============================================================================
# конец секции ВАШ КОД
# =============================================================================
