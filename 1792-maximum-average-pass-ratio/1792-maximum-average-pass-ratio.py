class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        max_heap = []

        def calc_increment(pass_students, total_students):
            curr_avg = pass_students / total_students
            new_avg = (pass_students + 1) / (total_students + 1)
            return new_avg - curr_avg

        for i, (pass_students, total_students) in enumerate(classes):
            increment = calc_increment(pass_students, total_students)
            heapq.heappush(max_heap, (-increment, i))

        while extraStudents > 0:
            _, idx = heapq.heappop(max_heap)
            classes[idx][0] += 1
            classes[idx][1] += 1
            increment = calc_increment(classes[idx][0], classes[idx][1])
            heapq.heappush(max_heap, (-increment, idx))
            extraStudents -= 1

        final_avg = sum(c[0] / c[1] for c in classes)
        return final_avg / len(classes)