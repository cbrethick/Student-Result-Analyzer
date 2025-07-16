def read_marks(file_path):
    students = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            name = parts[0]
            marks = list(map(int, parts[1:]))
            total = sum(marks)
            avg = total / len(marks)
            students.append({'name': name, 'total': total, 'avg': avg})
    return students

def find_topper(students):
    return max(students, key=lambda x: x['total'])

def save_results(students, topper, output_path):
    with open(output_path, 'w') as file:
        for student in students:
            file.write(f"{student['name']} - Total: {student['total']}, Average: {student['avg']:.2f}\n")
        file.write(f"\nTopper: {topper['name']} with {topper['total']} marks")

if __name__ == "__main__":
    students = read_marks('marks.txt')
    topper = find_topper(students)
    save_results(students, topper, 'results.txt')
    print("Results saved to results.txt")
