#DO NOT CHANGE THE NAMES OF THE FILE, CLASS or METHOD
class Exam:
    def PassFail(self, exam1, exam2, exam3, exam4):
        total = exam1 + exam2 + exam3 + exam4
        i = 0
        while total/6 < 55:
            total += 1
            i += 1
        return i
# For testing your code uncomment below lines.

# e = Exam()
# print(e.PassFail(15, 65, 55, 94))

# Comment or delete the above test code before submitting.
