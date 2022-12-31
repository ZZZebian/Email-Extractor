# Email Address Extractor Tool

This email extractor tool searches through files in a specified directory and extracts any email addresses that it finds. The extracted email addresses are then written to a text file. This tool is useful for finding and organizing email addresses from a large number of files.

## Requirements

To use this email extractor tool, you will need the following:

- Python 3.x
- The `re` module, which is included with Python
- The `os` module, which is included with Python
- The `tqdm` module, which can be installed using `pip install tqdm`

## How to Use the Email Extractor Tool

Using this email extractor tool is easy:

1. Place the files that you want to extract email addresses from in the `files` directory. If the `files` directory does not exist, it will be created when you run the script.
2. Run the script using `python scrap.py`.
3. The extracted email addresses will be written to a file named `results.txt` in the same directory as the script.

## Additional Notes

Here are a few additional notes about this email extractor tool:

- The tool only processes files with the following extensions: .html, .htm, .php, .json, .xml, and .csv.
- The tool uses the ISO-8859-1 character encoding for reading and writing files.
- The tool includes a progress bar using the `tqdm` module to show the progress of the email extraction process.
- If an error occurs while processing a file, an error message will be printed.

## License

This project is licensed under the [GPL-3.0 license](LICENSE).

