import sys


def main():
    # Check for a command-line argument (file name)
    if len(sys.argv) != 2:
        print("Error: Please provide a file name as a single argument.")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        # Open the file for reading
        with open(filename, 'r') as file:
            # Process each line in the file
            for line_num, line in enumerate(file, start=1):
                # Split the line into parts
                parts = line.split()

                # Ensure there are exactly two values
                if len(parts) != 2:
                    print(f"Error on line {line_num}: Expected 2 values, but got {len(parts)}.")
                    continue

                try:
                    # Convert parts to floats and calculate their sum
                    num1, num2 = float(parts[0]), float(parts[1])
                    print(f"Sum on line {line_num}: {num1 + num2}")

                except ValueError:
                    print(f"Error on line {line_num}: Non-numeric values encountered.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' could not be opened.")
        sys.exit(1)


if __name__ == "__main__":
    main()


