from MatrixReader import MatrixReader
from MatrixMultiplier import MatrixMultiplier

def process_matrix():
    while True:
        print("Choose an option to read the matrix:")
        print("1. From console")
        print("2. From file")
        option = input("Enter your choice (1/2): ").strip()

        if option == "1":
            matrix = MatrixReader.read_from_console()
            break
        elif option == "2":
            file_path = input("Enter the file path: ").strip()
            matrix = MatrixReader.read_from_file(file_path)
            break
        else:
            print("Invalid choice. Please select 1 or 2.\n")

    print("\nMatrix read:")
    print(MatrixReader.matrix_to_string(matrix))
    return matrix


print("Welcome to matrix computer")

print("Please provide first matrix")

m1 = process_matrix()

print("Please provide second matrix")

m2 = process_matrix()

try:
    multiplier = MatrixMultiplier(m1, m2)
    result = multiplier.compute_matrix_product()

    print("\nMatrix product is:")
    print(MatrixReader.matrix_to_string(result))
except Exception as e: print(e)