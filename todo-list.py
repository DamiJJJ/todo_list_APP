user_choice = -1

tasks = []
tasks.append("Wynieść śmieci")
tasks.append("Pozmywać")

def show_tasks():
    task_index = 0
    for task in tasks:
        print(task + " [" + str(task_index) + "]")
        task_index += 1

while user_choice != 5:
    if user_choice == 1:
        show_tasks()

    if user_choice == 2:
        task = input("Wpisz treść zadania: ")
        tasks.append(task)

    # if user_choice == 3:

    print()
    print("1. Pokaż zadania")
    print("2. Dodaj zadanie")
    print("3. Usuń zadanie")
    print("4. Zapisz zmiany do pliku")
    print("5. Wyjdź")

    user_choice = int(input("Wybierz liczbę: "))
    print()