import  os
if __name__ == '__main__':
    text = input("Enter What You Want:-")
    command = f"say {text}"
    if len(text) == 1:
        os.system("say 'oh my friend add a mining full words with out'")

    os.system(command)




