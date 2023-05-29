phone_book: list[dict[str, str]] = []
path = 'phones.txt'
original_book = []


def open_pb():
    global phone_book
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for contact in data:
        contact = contact.strip().split(':')
        new = {'id': contact[0], 'name': contact[1], 'phone': contact[2], 'comment': contact[3]}
        phone_book.append(new)
        original_book.append(new)


def save_pb():
    global phone_book
    data = []
    for contact in phone_book:
        data.append(':'.join([contact['id'], contact['name'], contact['phone'], contact['comment']]))
    data = '\n'.join(data)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)


def get_pb():
    global phone_book
    return phone_book


def add_contact(new: dict[str, str]) -> str:
    global phone_book
    new_id = int(phone_book[-1].get('id')) + 1
    new['id'] = str(new_id)
    phone_book.append(new)
    return new.get('name')


def search_contact(word: str) -> list[dict[str, str]]:
    global phone_book
    result: list[dict[str, str]] = []
    for contact in phone_book:
        for field in contact.values():
            if word.lower() in field.lower():
                result.append(contact)
                break
    return result


def change_contact(new: dict, index: int) -> str:
    global phone_book
    for contact in phone_book:
        if index == contact.get('id'):
            contact['name'] = new.get('name', contact.get('name'))
            contact['phone'] = new.get('phone', contact.get('phone'))
            contact['comment'] = new.get('comment', contact.get('comment'))
            return contact.get('name')


def delete_contact(index: int) -> str:
    deleted_element = phone_book.pop(index - 1)
    return deleted_element.get('name')


def confirm(message: str):
    answer = input(message + ' (Да / Нет) -> ')
    if answer.lower() == 'Да':
        return True
    return False