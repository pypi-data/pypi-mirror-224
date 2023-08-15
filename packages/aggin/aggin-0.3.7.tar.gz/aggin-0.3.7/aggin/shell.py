from aggin import aggin
import sys

def run():
    if len(sys.argv) == 1:
        interactive_shell()
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
        result, error = aggin.run(filename, code)  # Replace this with your interpreter logic

        if error:
            print(error.as_string())
        elif result:
            if len(result.elements) == 1:
                print(repr(result.elements[0]))
            else:
                print(repr(result))

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

if __name__ == "__main__":
    run()
