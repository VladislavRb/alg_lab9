from stable_matching import StableMatching


task_preference_lists = [
    [1, 2, 3],
    [0, 4],
    [4, 2, 1],
    [0, 3],
    [4, 1],
    [3, 0],
    [0, 2]]

employee_preference_lists = [
    [3, 5, 1, 6],
    [0, 2, 4],
    [0, 6, 2],
    [5, 0, 3],
    [2, 1, 4]]

# task_preference_lists = [
#     [0, 1],
#     [1, 0],
# ]
#
# employee_preference_lists = [
#     [1, 0],
#     [0, 1]
# ]


stm1 = StableMatching(task_preference_lists, employee_preference_lists)

stm1.fill_stable_matching()
print(["em" + str(employee.id) + ": ta" + str(employee.best_task_id) for employee in stm1.employees])

stm2 = StableMatching(employee_preference_lists, task_preference_lists)

stm2.fill_stable_matching()
print(["ta" + str(employee.id) + ": em" + str(employee.best_task_id) for employee in stm2.employees])
