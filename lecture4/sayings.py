def main():
    hello('world')
    goodbye('world')

def hello(name):
    print(f'hello, {name}')

def goodbye(name):
    print(f'goodbye, {name}')

# This is a special variable whose value is automatically set by Python to be "main" when you run a file from the command line, as by running python3 sayings.py
if __name__ == '__main__':
    main()