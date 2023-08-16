import requests
import threading
import time

URL = 'https://jsonplaceholder.typicode.com/posts'

def heavy(n):
    global URL
    for i in range(n):
        print('Fetching...')
        requests.get(URL)
        print('Fetched!')


def threaded(theads, calc):
    # theads - количество потоков
    # calc - количество операций на поток

    threads = []

    # делим вычисления на theads потоков
    for thead in range(theads):
        t = threading.Thread(target=heavy, args=(5,))
        threads.append(t)
        t.start()

    # Подождем, пока все потоки
    # завершат свою работу.
    for t in threads:
        t.join()


if __name__ == "__main__":
    start = time.time()
    threaded(10, 50)
    end = time.time()
    print("Общее время работы: ", end - start)