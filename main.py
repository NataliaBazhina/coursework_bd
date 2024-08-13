import os
import requests
from config import config





def get_vacancies_by_employer(employer_id):
    # URL для получения вакансий конкретного работодателя
    url = f'https://api.hh.ru/vacancies?employer_id={employer_id}'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()  # Возвращаем JSON-ответ
    else:
        print(f'Ошибка при получении данных: {response.status_code}')
        return None


def main():
    employers = get_employers()

    if employers:
        for employer in employers['items']:  # Это список работодателей
            print(f"Работодатель: {employer['name']}")
            employer_id = employer['id']
            vacancies = get_vacancies_by_employer(employer_id)

            if vacancies:
                for vacancy in vacancies['items']:  # Список вакансий
                    print(f"\tВакансия: {vacancy['name']}, ЗП: {vacancy['salary']}")
            print()  # Пустая строка для разделения


if __name__ == '__main__':
    main()