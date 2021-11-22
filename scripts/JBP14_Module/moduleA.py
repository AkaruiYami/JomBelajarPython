def hello():
    print("Hello from module A!")


# prevent the code inside this if statement from beeing executed when importing the file
if __name__ == "__main__":
    print("This is moduleA!")

print(f"This is from moduleA: {__name__}")
