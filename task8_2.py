import re
from time import perf_counter, sleep

# декоратор для измерения времени выполнения функций
def time_profile(func):
    def wrapper(*args):
        print('#-' * 30)
        start = perf_counter()
        decor_func = func(*args)
        time_cost = perf_counter() - start
        print('*' * 30)
        print(f'ВРЕМЯ ВЫПОЛНЕНИЯ - {time_cost:.10f}')
        sleep(5)
        return decor_func
    return wrapper


# мой первый вариант (время выполнения 2.2 сек)
@time_profile
def log_parse(file):
    all_result = []
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            pattern_1 = re.compile(r'\b(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
            pattern_2 = re.compile(r'\d{2}/[A-Z][a-z]+/\d{4}(?::\d{2}){3}\s\+\d{4}')
            pattern_3 = re.compile(r'"([A-Z]+)\b')
            pattern_4 = re.compile(r'/[a-z]+/\w+')
            pattern_5 = re.compile(r'\s(\d{3})\s')
            pattern_6 = re.compile(r'\s\d{3}\s(\d{1,4})\s"-"')
            result1 = re.findall(pattern_1, line)
            result2 = re.findall(pattern_2, line)
            result3 = re.findall(pattern_3, line)
            result4 = re.findall(pattern_4, line)
            result5 = re.findall(pattern_5, line)
            result6 = re.findall(pattern_6, line)
            result_line = (result1, result2, result3, result4, result5, result6)
            all_result.append(result_line)
    return all_result


# немного оптимизированный вариант (время выполения 0.5 сек)
@time_profile
def log_parse_v2(file):
    all_result = []
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read().splitlines()
        pattern = re.compile(r'\b(?P<remote_addr>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
                             r'(?P<request_date>\d{2}/[A-Z][a-z]+/\d{4}(?::\d{2}){3}\s\+\d{4})'
                             r'"(?P<request_type>[A-Z]+)\b'
                             r'(?P<requested_resource>/[a-z]+/\w+)'
                             r'\s(?P<response_code>\d{3})\s'
                             r'\s\d{3}\s(?P<response_size>\d{1,4})\s"-"')
        for line in content:
            res_iter = re.finditer(pattern, line)
            for i in res_iter:
                all_result.append(i.group(0))

    return all_result


if __name__ == '__main__':
    for el in log_parse('nginx_logs.txt'):
        print(el)

    for el in log_parse_v2('nginx_logs.txt'):
        print(el)
