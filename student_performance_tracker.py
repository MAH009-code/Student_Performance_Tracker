from typing import List, Dict

class Student:
    def __init__(self, name: str, scores: List[int]):
        self.name: str = name
        self.scores: List[int] = scores

    def calculate_average(self):
        return sum(self.scores) / len(self.scores)

    def is_passing(self, passing_score: int = 40):
        return all(score >= passing_score for score in self.scores)


class PerformanceTracker:
    def __init__(self):
        self.students: Dict[str, Student] = {}

    def add_student(self, name: str, scores: List[int]):
        if name in self.students:
            print(f"Student {name} already exists. Updating their scores.")
        self.students[name] = Student(name, scores)

    def calculate_class_average(self):
        if not self.students:
            return 0.0
        total_scores: float = sum(student.calculate_average() for student in self.students.values())
        return total_scores / len(self.students)

    def display_student_performance(self):
        if not self.students:
            print("No students in the system.")
            return

        for student in self.students.values():
            avg: float = student.calculate_average()
            status: str = "Passing" if student.is_passing() else "Failing"
            print(f"Student: {student.name}, Average: {avg:.2f}, Status: {status}")


def main():
    tracker = PerformanceTracker()
    print("Welcome to the Student Performance Tracker!")

    while True:
        try:
            name: str = input("Enter the student's name (or type 'done' to finish): ").strip()
            if name.lower() == 'done':
                break

            scores: List[int] = []
            for subject in ["Math", "Science", "English"]:
                score: int = int(input(f"Enter the score for {subject}: "))
                scores.append(score)

            tracker.add_student(name, scores)
        except ValueError:
            print("Invalid input. Please enter numeric values for scores.")

    print("\nStudent Performance Summary:")
    tracker.display_student_performance()

    class_avg: float = tracker.calculate_class_average()
    print(f"\nClass Average Score: {class_avg:.2f}")


if __name__ == "__main__":
    main()
