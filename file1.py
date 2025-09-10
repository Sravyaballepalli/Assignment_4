filename = "output.txt"

# Step 1: Take input and write to file
text = input("Enter text to write to the file: ")
with open(filename, "w") as file:
    file.write(text + "\n")
print(f"Data successfully written to {filename}.")

# Step 2: Take additional input and append to file
additional_text = input("Enter additional text to append: ")
with open(filename, "a") as file:
    file.write(additional_text + "\n")
print("Data successfully appended.")

# Step 3: Read and display final content of the file
print(f"\nFinal content of {filename}:")
with open(filename, "r") as file:
    print(file.read())