class Date:
    def __init__(self, date):
        self.date = date

    @staticmethod
    def validation(date_dict):
        if 1 < date_dict['day'] > 31:
            raise ValueError('Такого числа не существует')
        if 1 < date_dict['month'] > 12:
            raise ValueError('Такого месяца не существует')
        if 0 < date_dict['year'] // 1000 > 9:
            raise ValueError('Формат года неверный, должен быть ГГГГ')

    @classmethod
    def get_date_as_int(cls, date):
        date_dict = {'day': int(''.join(date[:2])), 'month': int(''.join(date[3:5])), 'year': int(''.join(date[6:]))}
        if not Date.validation(date_dict):
            return date_dict


my_date = Date('39-04-2022')
print(Date.get_date_as_int('19-12-2021'))

