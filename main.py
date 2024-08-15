from API import APIManager, EMPLOYERS_ID
from DBmanager import DBmanager
from utils import setup_connection, create_database, create_tables

# conn = setup_connection()
# create_database("vacancies", conn)
# create_tables('vacancies', conn)
# api_manager = APIManager(EMPLOYERS_ID)
# api_manager.save_employers_info()
# api_manager.save_vacancies_info()
manager = DBmanager()
while True:
        print("\nМеню:")
        print("1. получить список всех компаний и количество вакансий у каждой компании")
        print("2. получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.")
        print("3. получает среднюю зарплату по вакансиям")
        print("4. получает список всех вакансий, у которых зарплата выше средней по всем вакансиям")
        print("5. получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python.")
        print("6. выход")

        choice = input("Выберите пункт меню: ")

        if choice == '1':
            list_of_open_vacancies = manager.get_companies_and_vacancies_count()
            for company in list_of_open_vacancies:
                print(f'Название кампании {company[0]} - {company[1]}')



        elif choice == '2':
            list_of_open_vacancies = manager.get_all_vacancies()
            for company in list_of_open_vacancies:
                print(f'Название кампании {company[0]} , вакансия {company[1]}, зарплата {company[2]}, ссылка на вакансию {company[3]}')

        elif choice == '3':
            list_of_open_vacancies = manager.get_avg_salary()
            for company in list_of_open_vacancies:
                print( f'Средняя зарплата - {company[0]}')

        elif choice == '4':
            list_of_open_vacancies = manager.get_vacancies_with_higher_salary()
            for company in list_of_open_vacancies:
                print (company[0])

        elif choice == '5':
            keyword = input("Введите ключевое слово:")
            list_of_open_vacancies = manager.get_vacancies_with_keyword(keyword)
            for company in list_of_open_vacancies:
                print(company[0])

        elif choice == '6':
            print("Выход из программы.")
            break

        else:
            print("Некорректный выбор. Попробуйте еще раз.")




#
# if __name__ == "__main__":
#     ()



