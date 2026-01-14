def write_numbers_to_file(filename):
    try:
        with open(filename, "w") as file:
            for i in range(1, 101):
                file.write(str(i) + "\n")
        print("Numbers written successfully")

    except FileNotFoundError:
        print("Error: File path not found")

    except PermissionError:
        print("Error: Permission denied to write file")

    except Exception as e:
        print("Unexpected error:", e)
