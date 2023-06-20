import os

if __name__ == '__main__':
    print("Welcome to robo speaker 1")

    while True:
        x = input("Enter what you want to say: ")
        if x == 'q':
            os.system("say 'bye bye sathi'")
            break
        command = f"say {x}"
        os.system(command)
