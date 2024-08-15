import requests
import utils


EMPLOYERS_ID = [49357,1942330,3529,80,4181,1740,3022853,41862,23427,84585]

class APIManager:
    """Класс для работы с API"""
    URL_EMPLOYERS = "https://api.hh.ru/employers/"
    URL_VACANCIES = "https://api.hh.ru/vacancies/"

    def __init__(self, empls_list):
        self.empls_list = empls_list
        self.conn = utils.setup_connection()

    def send_request(self, id: int):
        """Посылает запрос для получения информации о вакансиях, работодателе"""
        response = requests.get(self.URL_EMPLOYERS + str(id))
        if response.status_code == 200:
            return response.json()
        else:
            print(f'Ошибка при получении данных: {response.status_code}')
            return None
        return r.json()

    def save_employers_info(self):
        """Получает информацию о работодателе"""
        conn = self.conn
        with conn.cursor() as cur:
            for i in self.empls_list:
                response = self.send_request(i)
                cur.execute(
                    'INSERT INTO employees (employee_id, company_name, open_vacancies)'
                    'VALUES (%s, %s, %s)',
                    [int(i), response["name"], int(response["open_vacancies"])]
                )

    def send_request_vacancies(self, employer_id: int):
        """Посылает запрос для получения информации о вакансиях работодателя"""
        response = requests.get(f"{self.URL_VACANCIES}?employer_id={employer_id}")
        if response.status_code == 200:
            return response.json()
        else:
            print(f'Ошибка при получении данных о вакансиях: {response.status_code}')
            return None

    def save_vacancies_info(self):
        """Получает информацию о вакансиях"""
        conn = self.conn
        with conn.cursor() as cur:
            for employer_id in self.empls_list:
                vacancies_response = self.send_request_vacancies(employer_id)
                if vacancies_response and 'items' in vacancies_response:
                    for res in vacancies_response['items']:
                        salary = utils.inspect_salary_from(res)
                        cur.execute(
                            'INSERT INTO vacancies (vacancy_id, vacancies_name, salary, vacancy_link, key_skills, employee_id) '
                            'VALUES (%s, %s, %s, %s, %s, %s)',
                            [
                                int(res["id"]),
                                res["name"],
                                salary,
                                res["alternate_url"],
                                res['snippet']['responsibility'],
                                employer_id
                            ]
                        )
            conn.commit()



# employer_id = EMPLOYERS_ID[0]
# vacancies_info = api_manager.send_request_vacancies(employer_id)
# if vacancies_info:
#     print(vacancies_info)

# if __name__ == "__main__":
#     api_manager = APIManager(EMPLOYERS_ID)
#     api_manager.save_vacancies_info()