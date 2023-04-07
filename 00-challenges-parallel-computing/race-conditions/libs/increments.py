
def increment_shared_variable_race_condition(shared_variable):
    for i in range(100000):
        shared_variable[0] += 1
    return shared_variable[0]


def increment_shared_variable(shared_variable, lock):
    for i in range(100000):
        with lock:
            shared_variable[0] += 1
    return shared_variable[0]
