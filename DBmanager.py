import utils


class DBmanager:


    def __init__(self):
        self.conn = utils.setup_connection()
    def get_companies_and_vacancies_count(self):
        conn = self.conn
        with conn.cursor() as cur:
            cur.execute(
                'SELECT company_name, open_vacancies FROM public.employees;'
            )
            return cur.fetchall()

    def get_all_vacancies(self):
        conn = self.conn
        with conn.cursor() as cur:
            cur.execute(
                'SELECT company_name, vacancies_name, salary, vacancy_link FROM public.vacancies INNER JOIN public.employees USING (employee_id);'
            )
            return cur.fetchall()

    def get_avg_salary(self):
        conn = self.conn
        with conn.cursor() as cur:
            cur.execute(
                'SELECT AVG(salary) FROM public.vacancies;'
            )
            return cur.fetchall()

    def get_vacancies_with_higher_salary(self):
        conn = self.conn
        with conn.cursor() as cur:
            cur.execute(
                'SELECT vacancies_name, salary FROM vacancies WHERE salary > (SELECT AVG(salary) FROM vacancies);'
            )
            return cur.fetchall()



manager = DBmanager()
list_of_open_vacancies = manager.get_companies_and_vacancies_count()
for vacancy in list_of_open_vacancies:
    print(vacancy[0])