from datetime import datetime


def execution_time(func):
    def wrapper():
        inicial_time = datetime.now()
        func()
        finale_time = datetime.now()
        time_elapsed = finale_time - inicial_time
        print("Duracion ejecucion: " + str(time_elapsed.total_seconds()) + " Segundos")

    return wrapper


@execution_time
def random_function():
    for _ in range(1, 10000000):
        pass


random_function()
