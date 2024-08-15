import utils

class DBmanager:
    """Класс для работы с базой данных"""
    def __init__(self):
        self.conn = utils.setup_connection()

    def get_companies_and_vacancies_count(self):
        """Получает список всех компаний и количество вакансий у каждой компании"""
        conn = self.conn
        with conn.cursor() as cur:
            cur.execute(
                'SELECT company_name, open_vacancies FROM public.employees;'
            )
            return cur.fetchall()

    def get_all_vacancies(self):
        """Получает список всех вакансий с указанием названия компании, названия вакансии, зарплаты и ссылки на вакансию"""
        conn = self.conn
        with conn.cursor() as cur:
            cur.execute(
                'SELECT company_name, vacancies_name, salary, vacancy_link FROM public.vacancies INNER JOIN public.employees USING (employee_id);'
            )
            return cur.fetchall()

    def get_avg_salary(self):
        """Получает среднюю зарплату по вакансиям"""
        conn = self.conn
        with conn.cursor() as cur:
            cur.execute(
                'SELECT AVG(salary) FROM public.vacancies;'
            )
            return cur.fetchall()

    def get_vacancies_with_higher_salary(self):
        """Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям"""
        conn = self.conn
        with conn.cursor() as cur:
            cur.execute(
                'SELECT vacancies_name, salary FROM vacancies WHERE salary > (SELECT AVG(salary) FROM vacancies);'
            )
            return cur.fetchall()

    def get_vacancies_with_keyword(self,keyword):
        """Получает список всех вакансий по ключевому слову в названии вакансии"""
        conn = self.conn
        with conn.cursor() as cur:
            cur.execute(
               f"SELECT vacancies_name FROM vacancies WHERE vacancies_name LIKE '%{keyword}%';"
            )
            return cur.fetchall()


# manager = DBmanager()
# list_of_open_vacancies = manager.get_companies_and_vacancies_count()
# for vacancy in list_of_open_vacancies:
#     print(vacancy[0])