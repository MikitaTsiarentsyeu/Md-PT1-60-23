repo = {'test name':["12314354", "5476578587"]}

def get_all_records():
    return '\n'.join([f"{name}:{','.join(numbers)}" for name, numbers in repo.items()])

def get_record_by_name(name):
    try:
        numbers = repo[name]
        return f"{name}:{','.join(numbers)}" 
    except KeyError:
        return ""

def add_record(name, numbers):
    repo[name] = numbers