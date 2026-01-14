def read_file(filename):
    try:
        with open(filename, "r") as file:
            print("File content:")
            print(file.read())

    except FileNotFoundError:
        print("Error: File not found")

    except PermissionError:
        print("Error: Permission denied")

    except Exception as e:
        print("Unexpected error:", e)
