import os
import sys

def parse_structure(structure_text):
    lines = structure_text.strip().split('\n')
    root = lines[0].strip('/')
    structure = {root: {}}
    path_stack = [structure[root]]
    indent_stack = [-1]

    for line in lines[1:]:
        indent = len(line) - len(line.lstrip('│ ├─'))
        name = line.split('─')[-1].strip()

        while indent <= indent_stack[-1]:
            path_stack.pop()
            indent_stack.pop()
            if not path_stack:  # Ensure we always have the root
                path_stack = [structure[root]]
                indent_stack = [-1]

        if name.endswith('/'):
            name = name.rstrip('/')
            new_dir = {}
            path_stack[-1][name] = new_dir
            path_stack.append(new_dir)
            indent_stack.append(indent)
        else:
            path_stack[-1][name] = None

    return structure

def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if content is None:
            # It's a file
            with open(path, 'w', encoding='utf-8') as f:
                pass  # Creates an empty file
            print(f"Created file: {path}")
        else:
            # It's a directory
            os.makedirs(path, exist_ok=True)
            print(f"Created directory: {path}")
            create_structure(path, content)

def read_file_with_encoding(file_path, encodings=['utf-8', 'cp932', 'shift_jis', 'euc-jp']):
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                return f.read()
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError(f"Unable to decode the file with any of the following encodings: {encodings}")

def main(structure_file):
    try:
        structure_text = read_file_with_encoding(structure_file)
    except FileNotFoundError:
        print(f"Error: File '{structure_file}' not found.")
        return
    except UnicodeDecodeError as e:
        print(f"Error: {str(e)}")
        return
    except IOError:
        print(f"Error: Unable to read file '{structure_file}'.")
        return

    structure = parse_structure(structure_text)
    root_dir = list(structure.keys())[0]

    create_structure('.', structure)
    print(f"Project structure created successfully in directory: {root_dir}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <path_to_structure_file>")
    else:
        main(sys.argv[1])