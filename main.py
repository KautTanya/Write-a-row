"""Write-a-row"""
input_text = input("Enter the text: ")
new_file = open("file.txt", "w+")


def add_row(text):
    """Add text in file"""
    new_file.write(text)
    new_file.seek(0)
    content = new_file.read()
    return content


print(add_row(input_text))
