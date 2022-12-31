import re
import os
from tqdm import tqdm

# Set the top-level directory containing the files to search
top_level_directory = 'C:/Users/andre/Desktop/Scrap/html_files/'

# Set the regex pattern to match email addresses
pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'

# Compile the regex pattern
regex = re.compile(pattern)

# Create a set to store the email addresses
emails = set()

# Open a file to write the results to
with open(r'C:\Users\andre\Desktop\Scrap\results.txt', 'w', encoding='ISO-8859-1') as outfile:
  # Get the total number of files to process
  num_files = sum([len(files) for r, d, files in os.walk(top_level_directory)])
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
