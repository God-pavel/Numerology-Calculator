class MatrixReader:

    @staticmethod
    def read_from_console():
        print("Enter the matrix row by row. Separate numbers with spaces.")
        print("Enter an empty line to finish.")
        result = []
        while True:
            line = input("Row: ").strip()
            if line == "":
                break
            row = list(map(int, line.split()))
            result.append(row)
        return result

    @staticmethod
    def read_from_file(file_path):
        result = []

        try:
            with open(file_path, "r") as file:
                for line in file:
                    row = list(map(int, line.split()))
                    result.append(row)
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
        except ValueError:
            print("Error: Invalid data in the file. Ensure all elements are integers.")

        return result

    @staticmethod
    def matrix_to_string(matrix):
        return "\n".join(" ".join(f"{elem:5}" for elem in row) for row in matrix)