import requests
import utils


EMPLOYERS_ID = [49357,1942330,3529,80,4181,1740,3022853,41862,23427,84585]

class APIManager:
    """Класс для работы с API"""
    URL_EMPLOYERS = "https://api.hh.ru/employers/"
    URL_VACANCIES = "https://api.hh.ru/vacancies/"
    # url_list_of_vacancies = 'https://api.hh.ru/vacancies?employer_id='
    # headers = {'User-Agent': 'api-test-agent'}

    def __init__(self, empls_list):
        self.empls_list = empls_list

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
        conn = utils.setup_connection()
        with conn.cursor() as cur:
            for i in self.empls_list:
                response = self.send_request(i)
                cur.execute(
                    'INSERT INTO employees (employee_id, company_name, open_vacancies)'
                    'VALUES (%s, %s, %s)',
                    [int(i), response["name"], int(response["open_vacancies"])]
                )
api = APIManager(EMPLOYERS_ID)
api.save_employers_info()

