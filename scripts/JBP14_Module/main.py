import moduleA
from folderA.moduleB import hello

if __name__ == "__main__":
    hello()
    moduleA.hello()
    print(f"This is from main file: {__name__}")
