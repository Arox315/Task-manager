"""
Moduł odpowiedzialny za zarządzaine zadaniami.
"""

from task import Task,RegularTask,PriorityTask,DEFAULT_DATE
import datetime
import json
import time


class TaskManager:
    """
    Klasa zarządzająca zadaniami
    """
    def __init__(self) -> None:
        self.tasks = []
    
    def calculate_time(func):
        """
        Dekorator do obliczania czasu wykonania sie funkcji
        """
    
        def func_wrapper(*args, **kwargs):

            begin = time.time()
        
            func(*args, **kwargs)

            end = time.time()
            print("Total time taken in : ", func.__name__, end - begin)

        return func_wrapper

    @calculate_time
    def add_task(self,title:str,desc:str,type = "Default",*args:int)->None:
        """
    Dodaje nowe zadanie do listy zadań.

    :param title: Tytuł zadania.
    :param desc: Opis zadania.
    :param type: Typ zadania 'Default'|'Priority'|'Regular', domyślnie 'Default'.
    :param args: Dodatkowe wartości. W zależności od typu zadania oznaczają priorytet albo regularność zadania.
    """ 
        if type == "Priority":
            if args[0] < 0: priority = 0
            elif args[0] > 10: priority = 10
            else: priority = args[0]
            task = PriorityTask(title=title,desc=desc,priority = priority)
        elif type == "Regular":
            if args[0] < 1: regularity = 1
            else: regularity = args[0]
            task = RegularTask(title=title,desc=desc,regularity = regularity)
        else:
            task = Task(title=title,desc=desc)

        self.tasks.append(task)
    

    def delete_task(self,task:Task|PriorityTask|RegularTask)->None:
        """
        Usuwa zadanie z listy zadań.

        :param task: Zadanie w postaci obiektu klasy: 'Task'|'PriorityTask'|'RegularTask'.
        """
        self.tasks.remove(task)
    

    def edit_task_title(self,task:Task|PriorityTask|RegularTask,title:str)->None:
        """
        Edytuje tytuł zadania.

        :param task: Zadanie w postaci obiektu klasy: 'Task'|'PriorityTask'|'RegularTask'.
        :param title: Nowy tytuł zadania.
        """
        task.title = title


    def edit_task_desc(self,task:Task|PriorityTask|RegularTask,desc:str)->None:
        """
        Edytuje opis zadania.

        :param task: Zadanie w postaci obiektu klasy: 'Task'|'PriorityTask'|'RegularTask'.
        :param desc: Nowy opis zadania.
        """
        task.desc = desc


    def edit_task_regulrity(self,task:Task|PriorityTask|RegularTask,regularity:int|str)->None:
        """
        Edytuje regularność zadania.

        :param task: Zadanie w postaci obiektu klasy: 'Task'|'PriorityTask'|'RegularTask'.
        :param regularity: Regularność zadania. Minimalna wartość = 1.
        """

        if not regularity.isnumeric():
            regularity = 1
        else:
            regularity = int(regularity)
        if regularity < 1:
            regularity = 1
        else:
            pass
        task.regularity = regularity


    def edit_task_priority(self,task:Task|PriorityTask|RegularTask,priority:int|str)->None:
        """
        Edytuje priorytet zadania.

        :param task: Zadanie w postaci obiektu klasy: 'Task'|'PriorityTask'|'RegularTask'.
        :param priority: Priorytet zadania. Przedział wartości: od 1 do 10.
        """

        if not priority.isnumeric():
            priority = 1
        else:
            priority = int(priority)

        if priority < 1:
            priority = 1
        elif priority > 10:
            priority = 10
        else:
            pass
        task.priority = priority
    

    def edit_task_status(self,task:Task|PriorityTask|RegularTask)->None:
        """
        Edytuje status ukończenia zadania.

        :param task: Zadanie w postaci obiektu klasy: 'Task'|'PriorityTask'|'RegularTask'.
        """

        if task.completed:
            task.completed = False
            task.completion_date = DEFAULT_DATE
            if task.type == "Regular":
                task.completion_due = DEFAULT_DATE
        else:
            self.complete_task(task)


    def edit_task_date(self,task:Task|PriorityTask|RegularTask,date:str)->None:
        """
        Edytuje datę ukończenia zadania.

        :param task: Zadanie w postaci obiektu klasy: 'Task'|'PriorityTask'|'RegularTask'.
        :param date: Nowa data zakończenia zadania. Wymagany format: [dd-mm-yyyy].
        """

        try:
            x = datetime.datetime.strptime(date,"%d-%m-%Y")
        except:
            print("Wprowadzono błędną datę. Poprawny format daty: [dd-mm-yyyy].")
            input("Naciśnij [enter] aby kontynuować")
        else:
            if x > datetime.datetime.now():
                print("Wprowadzono błędną datę.")
                input("Naciśnij [enter] aby kontynuować")
            else:
                task.completion_date = date
                task.completed = True


    def complete_task(self,task:Task|PriorityTask|RegularTask)->None:
        """
        Odznacza status zadania na zakończone oraz ustawia aktualną datę jako datę ukończenia zadania.

        :param task: Zadanie w postaci obiektu klasy: 'Task'|'PriorityTask'|'RegularTask'.
        """

        task.completed = True
        task.completion_date = str(datetime.datetime.now().strftime("%d-%m-%Y"))

        if task.type == "Regular":
            date = datetime.datetime.now() + datetime.timedelta(days=task.regularity)
            task.completion_due = str(date.strftime("%d-%m-%Y"))


    def list_tasks(self,flag=0)->None:
        """
        Wyświetla zadania z listy.

        :param flag: Domyślnie wartość 0. Inne wartości spowodują wyświetlwnie tylko nieukończonych zadań.
        """

        if flag != 0:
            for index,task in enumerate(self.tasks):
                if not task.completed:
                    print(f"{index+1}. [{task.type[0]}] {task.title}.")
        else:
            for index,task in enumerate(self.tasks):
                print(f"{index+1}. [{task.type[0]}] {task.title}.")


    def __contains__(self,*args:int|str)->None:
        """
        Sprawdza czy zadanie znajduje się w liście zadań.

        :param args: Kryteria wyszukiwania zadania. Dla wartości INT zadanie wyszukiwane jest po id.
            Dla pojedyńczej wartości STR zadanie wyszukiwane jest po tytule.
            Dla dwóch wartości STR zadanie wyszukiwane jest po tytule i opisie.
        """

        if len(args)==1:
            if type(args[0]) == int:
                idx = args[0]
                for index,task in enumerate(self.tasks):
                    print(task.id)
                    if task.id == idx:
                        print(f"Task found. Position in the list: {index}")
                        print(task)
                        break
                else:
                    print("Task not found. id")
            elif type(args[0])==str:
                title = args[0]
                task_found = False
                for index,task in enumerate(self.tasks):
                    if task.title == title:
                        print(f"Task {title} found. Position in the list: {index}")
                        task_found = True
                if not task_found:
                    print("Task not found.")
            else:
                print("Unknown search criteria.")
        else:
            if type(args[0]) == type(args[1]) == str:
                title = args[0]
                desc = args[1]
                for index,task in enumerate(self.tasks):
                    if task.title == title and task.desc == desc:
                        print(f"Task {title} found. Position in the list: {index}")
            else:
                print("Unknown search criteria.")


    def sort_tasks_asc(self)->None:
        """
        Sortuje listę zadań rosnąco po dacie ukończenia.
        """

        self.tasks = sorted(self.tasks,key= lambda x: datetime.datetime.strptime(x.completion_date,"%d-%m-%Y"))


    def sort_tasks_desc(self)->None:
        """
        Sortuje listę zadań malejąco po dacie ukończenia.
        """
        self.tasks = sorted(self.tasks,key= lambda x: datetime.datetime.strptime(x.completion_date,"%d-%m-%Y"),reverse=True)
    

    def update_regular_tasks(self)->None:
        """
        Uaktualnia status oraz datę zakończenia wszystkim regularnym zadaniom z listy w zależności od regularności danego zadania.
        """

        tasks:list[RegularTask] = self.get_tasks("Regular")
        for task in tasks:
            if task.completed and task.completion_due <= str(datetime.datetime.now().strftime("%d-%m-%Y")):
                task.completion_date = DEFAULT_DATE
                task.completion_due = DEFAULT_DATE
                task.completed = False
    

    def get_tasks(self,type="Default")->list:
        """
        Zwraca listę zadań wybranego typu.

        :param type: Typ zadania 'Default'|'Priority'|'Regular', domyślnie 'Default'.
        """

        res = [task for task in self.tasks if task.type == type]
        return res


    def get_tasks_completed(self,reversed=False)->list:
        """
        Zwraca listę ukończonych zadań.

        :param reversed: Jeśli ustawione na 'True' zwróci listę nieukończonych zadań.
        """

        if reversed:
            res = [task for task in self.tasks if not task.completed]
        else:
            res = [task for task in self.tasks if task.completed]
        return res
    

    def load_tasks_from_file(self,file_name="tasks")->None:
        """
        Wczytuje listę zadań z pliku.

        :param file_name: Nazwa pliku, z którego wczytana ma być lista zadań. 
        """

        self.tasks.clear()
        with open(file_name+'.json', 'r') as file:
            data = json.load(file)
            for task in data:
                if task['type'] == "Regular":
                    loaded_task = RegularTask(
                        id = task['id'],
                        type = task['type'],
                        title = task['title'],
                        desc = task['desc'],
                        completion_date = task['completion_date'],
                        completed = task['completed'],
                        creation_date = task['creation_date'],
                        regularity = task['regularity'],
                        completion_due = task['completion_due']
                    )
                elif task['type'] == "Priority":
                    loaded_task = PriorityTask(
                        id = task['id'],
                        type = task['type'],
                        title = task['title'],
                        desc = task['desc'],
                        completion_date = task['completion_date'],
                        completed = task['completed'],
                        creation_date = task['creation_date'],
                        priority = task['priority']
                    )
                else:
                    loaded_task = Task(
                        id = task['id'],
                        type = task['type'],
                        title = task['title'],
                        desc = task['desc'],
                        completion_date = task['completion_date'],
                        completed = task['completed'],
                        creation_date = task['creation_date']
                    )
                
                # if task with the same id exists, it gets overwritten
                if self.__has_id(loaded_task.id):
                    self.delete_task(self.__get_task_by_id(loaded_task.id))
                self.tasks.append(loaded_task)

    @calculate_time
    def save_tasks_to_file(self)->None:
        """
        Zapisuje listę zadań do pliku 'tasks.json'
        """

        tasks_data = []

        for task in self.tasks:
            task_data = {
                "id":task.id,
                "type":task.type,
                "title":task.title,
                "desc":task.desc,
                "completion_date":task.completion_date,
                "completed":task.completed,
                "creation_date":task.creation_date,
            }

            if task.type == "Priority":
                task_data["priority"] = task.priority
            
            if task.type == "Regular":
                task_data["completion_due"] = task.completion_due
                task_data["regularity"] = task.regularity
            
            tasks_data.append(task_data)
        
        with open("tasks.json", "w") as file:
            json.dump(tasks_data, file)


    def __has_id(self, idx:int) -> bool:
        """
        Sprawdza czy zadanie o konkretnym id występuje w liście.

        :param idx: id zadania.
        """
        for task in self.tasks:
            if task.id == idx:
                return True
        return False
    

    def __get_task_by_id(self,idx:int) -> Task|RegularTask|PriorityTask|None:
        """
        Zwraca zadanie o podanym id. Jeśli zadanie o podanym id nie istnieje zwraca 'None'

        :param idx: id zadania
        """

        for task in self.tasks:
            if task.id == idx:
                return task
        else:
            return None

