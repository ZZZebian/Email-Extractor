import re
import os
from tqdm import tqdm

# Get the directory containing the Python script
script_directory = os.path.dirname(__file__)

# Set the top-level directory to the "files" directory within the script directory
top_level_directory = os.path.join(script_directory, 'files')

# Check if the top-level directory exists
if not os.path.exists(top_level_directory):
  # Print a message if the top-level directory doesn't exist
  print(f'Directory {top_level_directory} does not exist. We will create it, make sure to place your files there.')
  directory_created = True
  # Create the top-level directory
  os.makedirs(top_level_directory)
else:
  directory_created = False
# Set the regex pattern to match email addresses
pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'

# Compile the regex pattern
regex = re.compile(pattern)

# Create a set to store the email addresses
emails = set()

# Set the path to the output file
output_file = os.path.join(script_directory, 'results.txt')

# Get the total number of files to process
num_files = sum([len(files) for r, d, files in os.walk(top_level_directory)])

# Check if the top-level directory is empty
if num_files == 0 and directory_created == False:
  # Print a message if the top-level directory is empty
  print(f'Directory {top_level_directory} is empty. Make sure to place your files there.')
  
if num_files > 0:
  # Open a file to write the results to
  with open(output_file, 'w', encoding='ISO-8859-1') as outfile:
    # Initialize the progress bar
    pbar = tqdm(total=num_files)
    
    # Iterate through the directories in the top-level directory
    for root, directories, filenames in os.walk(top_level_directory):
      # Iterate through the files in the current directory
      for filename in filenames:
        # Check if the file is one of the types we want to process
        if filename.endswith(('.html', '.htm', '.php', '.json', '.xml', '.csv')):
          try:
            # Open the file
            with open(os.path.join(root, filename), 'r', encoding='ISO-8859-1') as file:
              # Read the contents of the file
              contents = file.read()
              # Search for matches in the file contents
              matches = regex.finditer(contents)
              # Iterate through the matches
              for match in matches:
                # Add the email address to the set if it is not already present
                email = match.group()
                if email not in emails:
                  emails.add(email)
                  # Write the email address to the output file
                  outfile.write(email + '\n')
            # Update the progress bar
            pbar.update(1)
          except Exception as e:
            # Print an error message if an exception is raised
            print(f'Error processing {filename}: {e}')
    # Close the progress bar
      pbar.n = num_files
      pbar.close()
    if len(emails) == 0:
      print('No email addresses were found.')
    else:
      print(f'{len(emails)} email addresses were found and written to {output_file}.')