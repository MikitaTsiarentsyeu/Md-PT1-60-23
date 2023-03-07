def file_reader(file_name):
    try:
        file = open (file_name)
        file = file.read()
        return file
    except FileNotFoundError:
        return "File not found" 
    except:
        return "Invalid filename"

print(file_reader('Task7_1.py')) 