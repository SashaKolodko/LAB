import json

def read_json_file(file_path):
    """zitaet i vozrathaet."""
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def filter_users_by_language(data, language):
    """filtruet"""
    filtered_users = [user for user in data if user.get('language') == language]
    return filtered_users

def write_json_file(file_path, data):
    """zapisuvaet."""
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def main():
    
    input_file = 'lab.json'

    output_file = 'out.json'
    
    language_to_filter = 'Python' 

    data = read_json_file(input_file)

    filtered_users = filter_users_by_language(data, language_to_filter)

    write_json_file(output_file, filtered_users)

if __name__ == '__main__':
    main()
