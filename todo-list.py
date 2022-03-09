file_name = str(input("Podaj nazwę pliku, gdzie masz zapisane zadania (w przypadku braku podaj nazwę pliku gdzie chcesz je zapisać): "))

tasks = []

def show_tasks():
    task_index = 0
    for task in tasks:
        print(task + " [" + str(task_index) + "]")
        task_index += 1

def add_task():
    task = input("Wpisz treść zadania: ")
    tasks.append(task)
    print("Dodano zadanie!")

def delete_task():
    task_index = int(input("Podaj indeks zadania do usunięcia: "))
    if task_index < 0 or task_index > len(tasks) - 1:
        print("Zadanie o tym indeksie nie istnieje")
        return

    tasks.pop(task_index)
    print("Usunięto zadanie!")

def save_tasks_to_file(file_name):
    file = open(file_name + ".txt", "w")
    for task in tasks:
        file.write(task+"\n")
    file.close()

def load_tasks_from_file(file_name):
    try:
        file = open(file_name + ".txt")
        for line in file.readlines():
            tasks.append(line.strip())
        file.close()
    except FileNotFoundError:
        return

load_tasks_from_file(file_name)

try:
    while True:
        print()
        print("1. Pokaż zadania")
        print("2. Dodaj zadanie")
        print("3. Usuń zadanie")
        print("4. Wyjdź")

        user_choice = int(input("Wybierz liczbę: "))
        print()

        if user_choice == 1:
            show_tasks()

        if user_choice == 2:
            add_task()

        if user_choice == 3:
            delete_task()

        if user_choice == 4:
            end = ""
            while True:
                end = str(input("Chcesz zapisać swoją pracę? t - tak, n - nie:\n"))
                if end == "t":
                    save_tasks_to_file(file_name)
                    break
                if end == "n":
                    break
                else:
                    print("Musisz wybrać jedną z dwóch dostępnych opcji!")
            break
        if user_choice != 4:
            print("Musisz wybrać jedną z opcji poniżej:\n")
except ValueError:
    print("Musisz wybrać jedną z opcji poniżej:\n")