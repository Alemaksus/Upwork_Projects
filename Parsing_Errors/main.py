import requests
from bs4 import BeautifulSoup

"""
Ошибки при парсинге дейсвительно нужно обрабатывать. В качестве готовый альтернативы этой функции советую сторонюю
 библиотеку tenacity. Она позволяет оборачивать функции в декоратор @retry, или использовать аналогичный 
 контекстный менеджер. Можно также ограничить количество попыток, настроить задержку между попытками вплоть до 
 экспоненциальной выдержки. 
 Можно указать для каких исключений повторять попытку, либо при каком результате функции. 
 Ну и самое сочное, это также работает для асинхронных функций (@retry и контекстный менеджер AsyncRetrying)
"""



def test_request(url, retry=5):
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"
    }

    try:
        response = requests.get(url=url, headers=headers)
        print(f"[+] {url} {response.status_code}")
    except Exception as ex:
        time.sleep(3)
        if retry:
            print(f"[INFO] retry={retry} => {url}")
            return test_request(url, retry=(retry - 1))
        else:
            raise
    else:
        return response


def main():
    with open("Parsing_Errors/labirint_21_01_2022_10_54_async.txt") as file:
        books_urls = file.read().splitlines()

    for book_url in books_urls:
        # test_request(url=book_url)

        try:
            r = test_request(url=book_url)
            soup = BeautifulSoup(r.text, "lxml")
            print(f"{soup.title.text}\n{'-' * 20}")
        except Exception as ex:
            continue


if __name__ == "__main__":
    main()
