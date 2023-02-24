import time

# Line number to replace in the destination file
replace_line = 8

while True:
    # Open the source file for reading
    with open('file1.txt', 'r') as file1:
        # Read the contents of the specific line you want to replace
        content_to_replace = file1.readlines()[2]  # replace 2 with the line number you want to replace

    # Open the destination file for reading and writing
    with open('test2.html', 'r+') as test2:
        # Read the existing contents of the file into a list
        existing_content = test2.readlines()
        # Replace the specified line with the new content
        existing_content[replace_line-1] = content_to_replace  # replace_line-1 to account for 0-based indexing
        # Move the file pointer to the beginning of the file
        test2.seek(0)
        # Write the modified contents back to the file
        test2.writelines(existing_content)
        # Truncate any remaining content at the end of the file
        test2.truncate()

    # Pause the script for five seconds before repeating
    time.sleep(5)