"""
Moduł definiujący zadania.
"""

import itertools
import datetime

DEFAULT_DATE = "01-01-0001"


class Task:
    """
    Klasa definiująca zadanie
    """
    id_iter = itertools.count()

    def __init__(self,**kwargs) -> None:
        self.id=next(self.id_iter)
        self.type = "Default"
        self.title=f"Title {self.id}"
        self.desc=f"Description {self.id}"
        self.completion_date=DEFAULT_DATE
        self.completed=False
        self.creation_date = str(datetime.datetime.now().strftime("%d-%m-%Y"))

        for key,value in kwargs.items():
            setattr(self,key,value)


    def __str__(self) -> str:
        return f"Title: {self.title}\nDescription: {self.desc}\nStatus: {'Completed' if self.completed else 'In progress'}\nDate of completion: {self.completion_date if self.completed else '--:--:--'}\n"


class PriorityTask(Task):
    """
    Klasa definiująca zadanie priorytetowe
    """
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.priority = 0
        self.type = "Priority"

        for key,value in kwargs.items():
            setattr(self,key,value)
    

    def __str__(self):
        return super().__str__() + f"Priority: {self.priority}\n"


class RegularTask(Task):
    """
    Klasa definiująca zadanie regularne
    """
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.regularity = 0
        self.type = "Regular"
        self.completion_due = DEFAULT_DATE

        for key,value in kwargs.items():
            setattr(self,key,value)
    

    def __str__(self):
        return super().__str__() + f"Regularity: {self.regularity}\n"