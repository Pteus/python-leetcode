from typing import Counter, List

students = [1, 1, 1, 0, 0, 1]
sandwiches = [1, 0, 0, 0, 1, 1]


def countStudents(students: List[int], sandwiches: List[int]) -> int:
    res = len(sandwiches)
    cnt = Counter(students)

    for s in sandwiches:
        if cnt[s] != 0:
            res -= 1
            cnt[s] -= 1
        else:
            return res

    return res


print(countStudents(students, sandwiches))
