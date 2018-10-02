class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.queue == []

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        self.queue.pop()

    def size(self):
        return len(self.queue)


def hot_potato(name_list, num):
    sim_queue = Queue()
    for name in name_list:
        sim_queue.enqueue(name)
    while sim_queue.size() > 1:
        for i in range(num):
            sim_queue.enqueue(sim_queue.dequeue())
        sim_queue.dequeue()
    return sim_queue.dequeue()



print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))


# import random
# # Completed program for the printer simulation
# class Printer:
#     def __init__(self, ppm):
#         self.page_rate = ppm
#         self.current_task = None
#         self.time_remaining = 0
#     def tick(self):
#         if self.current_task != None:
#             self.time_remaining = self.tim
#             self.current_task = None
#
#     def busy(self):
#         if self.current_task != None:
#             return True
#
#         else:
#             return False
#
#     def start_next(self, new_task):
#         self.current_task = new_task
#         self.time_remaining = new_task.get_pages() * 60 / self.page_rate
#
# class Task:
#     def __init__(self, time):
#
#         self.timestamp = time
#         self.pages = random.randrange(1, 21)
#
#     def get_stamp(self):
#         return self.timestamp
#
#     def get_pages(self):
#         return self.pages
#
#     def wait_time(self, current_time):
#         return current_time - self.timestamp
#
# def simulation(num_seconds, pages_per_minute):
#     lab_printer = Printer(pages_per_minute)
#     print_queue = Queue()
#     waiting_times = []
#     for current_second in range(num_seconds):
#         if new_print_task():
#             task = Task(current_second)
#             print_queue.enqueue(task)
#         if (not lab_printer.busy()) and (not print_queue.is_empty()):
#             next_task = print_queue.dequeue()
#             waiting_times.append(next_task.wait_time(current_second))
#             lab_printer.start_next(next_task)
#         lab_printer.tick()
#     average_wait = sum(waiting_times) / len(waiting_times)
#     print("Average Wait %6.2f secs %3d tasks remaining." %(average_wait, print_queue.size()))
#
#
# def new_print_task():
#     num = random.randrange(1, 181)
#     if num == 180:
#         return True
#     else:
#         return False
#
# for i in range(10):
#     simulation(3600, 5)


class Deque:
    def __init__(self):
        self.deque = []

    def size(self):
        return len(self.deque)

    def is_empty(self):
        return self.deque == []

    def add_rear(self, item):
        self.deque.insert(0, item)

    def remove_rear(self):
        return self.deque.pop(0)

    def add_front(self, item):
        self.deque.append(item)

    def remove_front(self):
        return self.deque.pop()


def check_Palindrome(input_string):
    deuqe = Deque()
    for chr in input_string:
        deuqe.add_front(chr)

    for chr in input_string:
        if deuqe.remove_front() == chr:
            pass
        else:
            return False

    return True


print(check_Palindrome("lsdkjfskf"))
print(check_Palindrome("radar"))

