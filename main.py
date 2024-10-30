"""
Moduł główny uruchamiający aplikację.
"""

from taskmanager import TaskManager
import os


def cls():
    """
    Czyści konsolę.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':

    task_manager = TaskManager()

    while True:
        task_manager.update_regular_tasks()
        print("""
    1. Dodaj nowe zadanie.
    2. Edytuj zadanie.
    3. Oznacz zadanie jako zakończone.
    4. Usuń zadanie.
    5. Wyświetl zadania.
    6. Wyszukaj zadanie.
    7. Zapisz zadania do pliku.
    8. Wczytaj zadania z pliku.
    9. Wyjdź.
    """)
        user_input = input("Wybierz funkcję: ")

        if user_input == '1':
            cls()
            while True:
                user_type_input = input("Wybierz rodzaj zadania:\n1. Domyślne\n2. Regularne\n3. Priorytetowne\n-> ")
                cls()
                if user_type_input == "1":
                    new_task_title = input("Wprowadź tytuł zadania: ")
                    new_task_desc = input("Wprowadź opis zadania: ")
                    task_manager.add_task(new_task_title,new_task_desc)
                    cls()
                    print(f"Wprowadzono nowe zadanie: {new_task_title}.")
                    input("Naciśnij [enter] aby kontynuować.")
                    cls()
                    break
                elif user_type_input == "2":
                    new_task_title = input("Wprowadź tytuł zadania: ")
                    new_task_desc = input("Wprowadź opis zadania: ")
                    new_task_regularity = input("Wprowadź regularność zadania: ")
                    if not new_task_regularity.isnumeric():
                        print("Błąd podczas tworzenia zadania. Regularność musi być liczbą!")
                        input("Naciśnij [enter] aby kontynuować.")
                        cls()
                        break
                    task_manager.add_task(new_task_title,new_task_desc,"Regular",int(new_task_regularity))
                    cls()
                    print(f"Wprowadzono nowe zadanie: {new_task_title}.")
                    input("Naciśnij [enter] aby kontynuować.")
                    cls()
                    break
                elif user_type_input == "3":
                    new_task_title = input("Wprowadź tytuł zadania: ")
                    new_task_desc = input("Wprowadź opis zadania: ")
                    new_task_priority = input("Wprowadź priorytet zadania: ")
                    if not new_task_priority.isnumeric():
                        print("Błąd podczas tworzenia zadania. Priorytet musi być liczbą!")
                        input("Naciśnij [enter] aby kontynuować.")
                        cls()
                        break
                    task_manager.add_task(new_task_title,new_task_desc,"Priority",int(new_task_priority))
                    cls()
                    print(f"Wprowadzono nowe zadanie: {new_task_title}.")
                    input("Naciśnij [enter] aby kontynuować.")
                    cls()
                    break
                else:
                    cls()
        
        if user_input == '2':
            cls()
            if len(task_manager.tasks) == 0:
                print("Lista zadań jest pusta.")
                input("Naciśnij [enter] aby kontynuować.")
                cls()
            else:
                while True:
                    task_manager.list_tasks()
                    task_num = input("Wybierz zadanie do edycji: ")
                    if not task_num.isnumeric():
                        cls()
                    elif 0 < int(task_num) <= len(task_manager.tasks):
                        cls()
                        break
                    else:
                        cls()
                while True:
                    task = task_manager.tasks[int(task_num)-1]
                    print(task)
                    if task.type == "Default":
                        print("1. Edytuj tytuł.\n2. Edytuj opis.\n3. Edytuj status.\n4. Edytuj date zakończenia.\n5. Opuść edycję zadania.\n")
                        edit_input = input("Wybierz opcję: ")

                        if edit_input == "1":
                            cls()
                            edit_task_title = input("Wprowadź nowy tytuł: ")
                            task_manager.edit_task_title(task,edit_task_title)
                            cls()
                        elif edit_input == "2":
                            cls()
                            edit_task_desc = input("Wprowadź nowy opis: ")
                            task_manager.edit_task_desc(task,edit_task_desc)
                            cls()
                        elif edit_input == "3":
                            cls()
                            task_manager.edit_task_status(task)
                        elif edit_input == "4":
                            cls()
                            edit_task_date = input("Wprowadź nową datę: ")
                            task_manager.edit_task_date(task,edit_task_date)
                            cls()
                        elif edit_input == "5":
                            cls()
                            break
                        else:
                            cls()
                    elif task.type == "Regular":
                        print("1. Edytuj tytuł.\n2. Edytuj opis.\n3. Edytuj regularność.\n4. Edytuj status.\n5. Edytuj date zakończenia.\n6. Opuść edycję zadania.\n")
                        edit_input = input("Wybierz opcję: ")

                        if edit_input == "1":
                            cls()
                            edit_task_title = input("Wprowadź nowy tytuł: ")
                            task_manager.edit_task_title(task,edit_task_title)
                            cls()
                        elif edit_input == "2":
                            cls()
                            edit_task_desc = input("Wprowadź nowy opis: ")
                            task_manager.edit_task_desc(task,edit_task_desc)
                            cls()
                        elif edit_input == "3":
                            cls()
                            edit_task_regularity = input("Wprowadź nową regularność: ")
                            task_manager.edit_task_regulrity(task,edit_task_regularity)
                            cls()
                        elif edit_input == "4":
                            cls()
                            task_manager.edit_task_status(task)
                        elif edit_input == "5":
                            cls()
                            edit_task_date = input("Wprowadź nową datę: ")
                            task_manager.edit_task_date(task,edit_task_date)
                            cls()
                        elif edit_input == "6":
                            cls()
                            break
                        else:
                            cls()
                    elif task.type == "Priority":
                        print("1. Edytuj tytuł.\n2. Edytuj opis.\n3. Edytuj priorytet.\n4. Edytuj status.\n5. Edytuj date zakończenia.\n6. Opuść edycję zadania.\n")
                        edit_input = input("Wybierz opcję: ")

                        if edit_input == "1":
                            cls()
                            edit_task_title = input("Wprowadź nowy tytuł: ")
                            task_manager.edit_task_title(task,edit_task_title)
                            cls()
                        elif edit_input == "2":
                            cls()
                            edit_task_desc = input("Wprowadź nowy opis: ")
                            task_manager.edit_task_desc(task,edit_task_desc)
                            cls()
                        elif edit_input == "3":
                            cls()
                            edit_task_priority = input("Wprowadź nowy priorytet: ")
                            task_manager.edit_task_priority(task,edit_task_priority)
                            cls()
                        elif edit_input == "4":
                            cls()
                            task_manager.edit_task_status(task)
                        elif edit_input == "5":
                            cls()
                            edit_task_date = input("Wprowadź nową datę: ")
                            task_manager.edit_task_date(task,edit_task_date)
                            cls()
                        elif edit_input == "6":
                            cls()
                            break
                        else:
                            cls()
                    else:
                        cls()
                        print("Wystapił błąd: Nieobsługiwany typ zadania.")
                        input("Naciśnij [enter] aby kontynuować.")
                        cls()
    
        if user_input == '3':
            cls()
            if len(task_manager.tasks) == 0:
                print("Lista zadań jest pusta.")
                input("Naciśnij [enter] aby kontynuować.")
                cls()
            elif len(task_manager.get_tasks_completed(True)) == 0:
                print("Brak zadań do zakończenia.")
                input("Naciśnij [enter] aby kontynuować.")
                cls()
            else:
                while True:
                    task_manager.list_tasks(1)
                    task_num = input("Wybierz zadanie do zakończenia: ")
                    if not task_num.isnumeric():
                        cls()
                    elif 0 < int(task_num) <= len(task_manager.tasks):
                        cls()
                        break
                    else:
                        cls()
                while True:
                    task = task_manager.tasks[int(task_num)-1]
                    print(task)
                    print("1. Oznacz zadanie jako zakończone.\n2. Opuść oznaczanie zadania.\n")
                    edit_input = input("Wybierz opcję: ")

                    if edit_input == "1":
                        cls()
                        task_manager.complete_task(task)
                        print(task)
                        print("Zadanie zostało ukończone.")
                        input("Naciśnij [enter] aby kontynuować.")
                        cls()
                        break
                    elif edit_input == "2":
                        cls()
                        break
                    else:
                        cls()

        if user_input == '4':
            cls()
            if len(task_manager.tasks) == 0:
                print("Lista zadań jest pusta.")
                input("Naciśnij [enter] aby kontynuować.")
                cls()
            else:
                while True:
                    task_manager.list_tasks()
                    print("-----------------------------------\n\'asc\' - sortuj zadania rosnąco po dacie ukończenia\n\'desc\' - sortuj zadania malejąco po dacie ukończenia\n")
                    task_num = input("Wybierz zadanie do usunięcia: ")
                    if task_num != "asc" and task_num != "desc" and not task_num.isnumeric():
                        cls()
                    elif task_num == "asc":
                        task_manager.sort_tasks_asc()
                        cls()
                    elif task_num == "desc":
                        task_manager.sort_tasks_desc()
                        cls()
                    elif 0 < int(task_num) <= len(task_manager.tasks):
                        cls()
                        break
                    else:
                        cls()
                while True:
                    task = task_manager.tasks[int(task_num)-1]
                    print(task)
                    print("1. Usuń zadanie.\n2. Opuść usuwanie zadania.\n")
                    edit_input = input("Wybierz opcję: ")

                    if edit_input == "1":
                        cls()
                        task_manager.delete_task(task)
                        print("Zadanie zostało usunięte.")
                        input("Naciśnij [enter] aby kontynuować.")
                        cls()
                        break
                    elif edit_input == "2":
                        cls()
                        break
                    else:
                        cls()

        if user_input == '5':
            cls()
            if len(task_manager.tasks) == 0:
                print("Lista zadań jest pusta.")
                input("Naciśnij [enter] aby kontynuować.")
                cls()
            else:
                while True:
                    task_manager.list_tasks()
                    print("-----------------------------------\n\'asc\' - sortuj zadania rosnąco po dacie ukończenia\n\'desc\' - sortuj zadania malejąco po dacie ukończenia\n")
                    task_num = input("Wybierz zadanie do wyświetlenia: ")
                    if task_num != "asc" and task_num != "desc" and not task_num.isnumeric():
                        cls()
                    elif task_num == "asc":
                        task_manager.sort_tasks_asc()
                        cls()
                    elif task_num == "desc":
                        task_manager.sort_tasks_desc()
                        cls()
                    elif 0 < int(task_num) <= len(task_manager.tasks):
                        cls()
                        break
                    else:
                        cls()
                while True:
                    task = task_manager.tasks[int(task_num)-1]
                    print(task)
                    print("1. Opuść podgląd zadania.\n")
                    edit_input = input("Wybierz opcję: ")

                    if edit_input == "1":
                        cls()
                        break
                    cls()
                        
        if user_input == '6':
            cls()
            while True:
                print("1. Wyszukaj zadanie po tytule.\n2. Wyszukaj zadanie po id.\n")
                find_task = input("Wybierz opcję: ")

                if find_task == '1':
                    cls()
                    title = input("Wprowadź tytuł: ")
                    task_manager.__contains__(title)
                    break
                elif find_task == "2":
                    while True:
                        cls()
                        id = input("Wprowadź id: ")
                        if id.isnumeric():
                            task_manager.__contains__(int(id))
                            break
                    break
                else:
                    cls()
            
            input("Naciśnij [enter] aby kontynuować.")
            cls()

        if user_input == '7':
            task_manager.save_tasks_to_file()
            print("Zapisano zadania do pliku.")
            input("Naciśnij [enter] aby kontynuować.")
            cls()
        
        if user_input == '8':
            cls()
            user_load_input = input("UWAGA! Wczytanie zadań z pliku wyczyści aktualną listę zadań.\nCzy chcesz kontynuować [y/n]?\n-> ")
            if user_load_input == "y" or user_load_input == "Y":
                task_manager.load_tasks_from_file()
                print("Wczytano zadania z pliku.")
                input("Naciśnij [enter] aby kontynuować.")
            else:
                print("Niewczytano zadań z pliku.")
                input("Naciśnij [enter] aby kontynuować.")
            cls()
        
        if user_input == '9':
            print("Zamykanie programu...")
            break