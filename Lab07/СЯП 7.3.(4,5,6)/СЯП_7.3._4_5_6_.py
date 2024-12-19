import os

def list_directory(path):
    """vuvod sodirgimogo direktorii."""
    try:
        items = os.listdir(path)
        print(f"soderzimoe direktorii '{path}':")
        for item in items:
            print(item)
    except FileNotFoundError:
        print(f"false: deriktoria '{path}' ne naidena.")
    except PermissionError:
        print(f"false net dostypa '{path}'.")

def create_file_or_directory(path, name, is_directory=False):
    """sozdaet fail ili deriktoriu."""
    full_path = os.path.join(path, name)
    try:
        if is_directory:
            os.makedirs(full_path)
            print(f"direktoria '{full_path}' sozdana.")
        else:
            with open(full_path, 'w') as f:
                f.write('')  
            print(f"fail '{full_path}' sozdan.")
    except FileExistsError:
        print(f"false: '{full_path}'sythestvyet.")
    except Exception as e:
        print(f"false: {e}")

def delete_file_or_directory(path):
    """ydalaem."""
    try:
        if os.path.isdir(path):
            os.rmdir(path)  
            print(f"directoria '{path}' ydalena.")
        else:
            os.remove(path)  
            print(f"fail '{path}' ydalen.")
    except FileNotFoundError:
        print(f"false: '{path}' ne naiden.")
    except OSError:
        print(f"false: '{path}' ne pystay derictoria.")
    except Exception as e:
        print(f"false : {e}")

def main():
    while True:
        print("\nmenedjer")
        print("1. raskrut direktoriy")
        print("2. sozdat fail")
        print("3. sozdat direktoriy")
        print("4. ydalit fail")
        print("5. ydalit direktoriy")
        print("6. vuxod")
        
        choice = input("(1-6): ")
        
        if choice == '1':
            path = input("pyt v direktoriy: ")
            list_directory(path)
        elif choice == '2':
            path = input("pyt v direktoriy dla sosdania fail: ")
            name = input("ima direktorii: ")
            create_file_or_directory(path, name, is_directory=False)
        elif choice == '3':
            path = input("pyt dla sozdania direktorii: ")
            name = input("ima directorii: ")
            create_file_or_directory(path, name, is_directory=True)
        elif choice == '4':
            path = input("pyt v fail: ")
            delete_file_or_directory(path)
        elif choice == '5':
            path = input("pyt v direktoriu: ")
            delete_file_or_directory(path)
        elif choice == '6':
            print("vuxod")
            break
        else:
            print("false.")

if __name__ == "__main__":
    main()
