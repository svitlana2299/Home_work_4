# Функція-декоратор для обробки виключень від користувача
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found"
        except ValueError:
            return "Please provide a name and phone number"
        except IndexError:
            return "Please provide a name"
    return wrapper

# Функція для відображення привітання


def hello():
    return "How can I help you?"

# Функція для додавання нового контакту


@input_error
def add(*args):
    name, phone = args[0].split()
    contacts[name] = phone
    return f"{name} has been added to your contacts"

# Функція для зміни номера телефону існуючого контакту


@input_error
def change(*args):
    name, phone = args[0].split()
    contacts[name] = phone
    return f"{name}'s phone number has been updated"

# Функція для відображення номера телефону для зазначеного контакту


@input_error
def phone(*args):
    name = args[0]
    return f"{name}'s phone number is {contacts[name]}"

# Функція для відображення всіх збережених контактів


def show_all():
    if not contacts:
        return "You don't have any contacts yet"
    else:
        result = "Your contacts:\n"
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result

# Головна функція, що виконується у безкінечному циклі та чекає команди користувача


def main():
    print("Welcome to the contacts bot!")
    while True:
        command = input("Enter command: ").lower()
        if command == "hello":
            print(hello())
        elif command.startswith("add "):
            print(add(command[4:]))
        elif command.startswith("change "):
            print(change(command[7:]))
        elif command.startswith("phone "):
            print(phone(command[6:]))
        elif command == "show all":
            print(show_all())
        elif command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Invalid command. Please try again.")


# Запуск головної функції
if __name__ == "__main__":
    contacts = {}
    main()
