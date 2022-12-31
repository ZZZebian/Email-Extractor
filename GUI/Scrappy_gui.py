import re
import os
from PyQt5 import QtWidgets, QtGui

class EmailExtractor(QtWidgets.QWidget):
  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
    # Create a QIcon object from the file path of the icon
    icon = QtGui.QIcon('icon.png')
    # Set the window icon using the setWindowIcon method
    self.setWindowIcon(icon)

    # Set the window title and size
    self.setWindowTitle('Email Extractor By Zebs v0.1 - GUI')
    self.setGeometry(300, 300, 300, 150)

    # Create the directory selection button and label
    self.dirButton = QtWidgets.QPushButton('Select Directory', self)
    self.dirLabel = QtWidgets.QLabel(self)
    self.dirLabel.setText('No directory selected')
    
    # Create the save directory selection button and label
    self.saveDirButton = QtWidgets.QPushButton('Select Save Directory', self)
    self.saveDirLabel = QtWidgets.QLabel(self)
    self.saveNameLabel = QtWidgets.QLabel(self)
    self.saveDirLabel.setText('No save directory selected')
   



    # Create the start button and output label
    self.startButton = QtWidgets.QPushButton('Start', self)
    self.outputLabel = QtWidgets.QLabel(self)
    self.outputLabel.setText('No output yet')

    # Create the layout
    layout = QtWidgets.QVBoxLayout(self)
    layout.addWidget(self.dirButton)
    layout.addWidget(self.dirLabel)
    layout.addWidget(self.saveDirButton)
    layout.addWidget(self.saveDirLabel)
    layout.addWidget(self.saveNameLabel)
    layout.addWidget(self.startButton)
    layout.addWidget(self.outputLabel)
    
    # Set the layout
    self.setLayout(layout)

    # Connect the buttons to their respective functions
    self.dirButton.clicked.connect(self.selectDirectory)
    self.saveDirButton.clicked.connect(self.selectSaveDirectory)
    self.startButton.clicked.connect(self.start)
    # Create a progress bar
    self.progressBar = QtWidgets.QProgressBar(self)
    # Add the progress bar to the layout
    layout.addWidget(self.progressBar)
    
  def selectDirectory(self):
    # Open a dialog to select the top-level directory containing the files
    directory = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Directory')
    # Update the label with the selected directory
    self.dirLabel.setText(directory)
    self.outputLabel.setText('Press Start to Extract')
    
  def selectSaveDirectory(self):
    # Open a dialog to select the directory for the saved file
    options = QtWidgets.QFileDialog.Options()
    options |= QtWidgets.QFileDialog.ReadOnly
    file_name, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', '', 'Text Files (*.txt);;All Files (*)', options=options)
    # Update the label with the selected directory
    self.saveDirLabel.setText(os.path.dirname(file_name))
    self.saveNameLabel.setText(os.path.basename(file_name))
    


  def start(self):
    # Get the top-level directory containing the files
    top_level_directory = self.dirLabel.text()
    # Set the regex pattern to match email addresses
    pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    # Compile the regex pattern
    regex = re.compile(pattern)
    # Create a set to store the email addresses
    emails = set()
    
    # Get the selected save directory
    save_dir = self.saveDirLabel.text()
    save_name = self.saveNameLabel.text()

    
   
    # Open the file to write the results to
    with open(os.path.join(save_dir, save_name), 'w', encoding='ISO-8859-1') as outfile:
      # Get the total number of files to process
      num_files = sum([len(files) for r, d, files in os.walk(top_level_directory)])
      # Initialize a counter to keep track of the number of files processed
      count = 0
      # Iterate through the directories in the top-level directory
      for root, directories, filenames in os.walk(top_level_directory):
        # Iterate through the files in the current directory
        for filename in filenames:
          if filename.endswith(('.html', '.htm', '.php', '.json', '.xml', '.csv', '.txt')):
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
            # Increment the counter
            count += 1
            # Update the output label with the current progress
            progress = 100 * count / num_files
            # Set the progress bar range
            self.progressBar.setRange(0, 100)
            # Set the progress bar value
            self.progressBar.setValue(int(progress)+2)
            #print(progress)
    # Update the output label with the total number of emails extracted
    self.outputLabel.setText(f'{len(emails)} emails extracted')
if __name__ == '__main__':
  app = QtWidgets.QApplication([])
  window = EmailExtractor()
  window.show()
  app.exec_()