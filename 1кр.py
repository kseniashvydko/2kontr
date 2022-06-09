import heapq
import numpy
import time
from multiprocessing import Pool


def func():
    items = numpy.random.randint(1000000, size
    =1000000)
    print(len(items), items[:10 ** 6])
    print(heapq.nlargest(1, items))  # ищем макс элемент с помощью приоритетной очереди

def main():
    func()

if __name__ == '__main__':
    startTime = time.time()  # время начала замера
    for i in range(4):
        func()
    endTime = time.time()  # время конца замера
    totalTime = endTime - startTime  # вычисляем затраченное время
    print("Время, затраченное на выполнение данного кода(при последовательном запуске) = ", totalTime)

    startTime = time.time()  # время начала замера
    with Pool(4) as pool:
        a = []
        for _ in range(4):
            a.append(pool.apply_async(func))
        for c in a:
            c.wait()
    endTime = time.time()  # время конца замера
    totalTime = endTime - startTime  # вычисляем затраченное время
    print("Время, затраченное на выполнение данного кода(в 4 потоках) = ", totalTime)





