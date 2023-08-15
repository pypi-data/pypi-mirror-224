from . import aggin
import sys

def run():
    if len(sys.argv) == 1:
        interactive_shell()  # Call your existing interactive shell function
    elif len(sys.argv) == 2:
        filename = sys.argv[1]
        run_file(filename)
    else:
        print("Usage:")
        print("aggin - Run the interactive shell")
        print("aggin <filename.nig> - Run the specified .nig file")

def run_file(filename):
    with open(filename, 'r') as file:
        code = file.read()
        aggin.RUN(f'RUN("{filename}")')

def interactive_shell():
    while True:
        text = input('aggin > ')
        if text.strip() == "":
            continue
        result, error = aggin.run('<stdin>', text)

        if error:
            print(error.as_string())
        elif result:
            if len(result.elements) == 1:
                print(repr(result.elements[0]))
            else:
                print(repr(result))
