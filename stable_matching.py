class Task:
    def __init__(self, task_id: int, employee_preferences: list):
        self.id = task_id
        self.employee_preferences = employee_preferences

        self.current_preferred_employee_index = 0
        self.was_rejected = True


class Employee:
    def __init__(self, employee_id: int, task_preferences: list):
        self.id = employee_id
        self.task_preferences = task_preferences

        self.priority_dict = {}
        for i in range(len(task_preferences)):
            self.priority_dict[self.task_preferences[i]] = i

        self.offer_list = []
        self.best_task_id = None
        self.is_actively_looking = True

    def task1_has_more_priority_than_task2(self, task_id1: int, task_id2: int):
        if task_id2 is None:
            return True

        return self.priority_dict[task_id1] < self.priority_dict[task_id2]


class StableMatching:
    def __init__(self, task_preference_lists: list, employee_preference_lists: list):
        self.amount_of_tasks = len(task_preference_lists)
        self.amount_of_employees = len(employee_preference_lists)

        self.tasks = [Task(i, task_preference_lists[i]) for i in range(self.amount_of_tasks)]
        self.employees = [Employee(i, employee_preference_lists[i]) for i in range(self.amount_of_employees)]

    def fill_stable_matching(self):
        indexes = [i for i in range(self.amount_of_tasks)]
        tasks_are_assigned = [False for i in range(self.amount_of_tasks)]

        while False in list(map(lambda i: True if tasks_are_assigned[i] else not self.tasks[i].was_rejected, indexes)):
            for task in self.tasks:
                if task.was_rejected:
                    if task.current_preferred_employee_index == len(task.employee_preferences):
                        task.was_rejected = False
                        tasks_are_assigned[task.id] = True
                        continue

                    tasks_current_preferred_employee_id = task.employee_preferences[task.current_preferred_employee_index]
                    preferred_employee = self.employees[tasks_current_preferred_employee_id]

                    if preferred_employee.is_actively_looking:
                        preferred_employee.offer_list.append(task.id)
                    else:
                        task.current_preferred_employee_index += 1

            for employee in self.employees:
                if employee.is_actively_looking:
                    if len(employee.offer_list):
                        current_best_task_id = min(employee.offer_list, key=lambda t_id: employee.priority_dict[t_id])

                        if employee.task1_has_more_priority_than_task2(current_best_task_id, employee.best_task_id):
                            if employee.best_task_id is not None:
                                best_task = self.tasks[employee.best_task_id]

                                best_task.was_rejected = True
                                best_task.current_preferred_employee_index += 1

                            employee.best_task_id = current_best_task_id
                            new_best_task = self.tasks[current_best_task_id]

                            for task_id in employee.offer_list:
                                if not task_id == current_best_task_id:
                                    self.tasks[task_id].was_rejected = True
                                    self.tasks[task_id].current_preferred_employee_index += 1

                            new_best_task.was_rejected = False

                            if not employee.priority_dict[current_best_task_id]:
                                new_best_task.current_preferred_employee_index = len(new_best_task.employee_preferences)
                                tasks_are_assigned[current_best_task_id] = True
                                employee.is_actively_looking = False
                        else:
                            for task_id in employee.offer_list:
                                self.tasks[task_id].was_rejected = True
                                self.tasks[task_id].current_preferred_employee_index += 1

                        employee.offer_list = []
