# Remitly Internship 2024 - JSON Policy Analyzer

### This Python script analyzes a JSON file to determine, if its 'PolicyDocument', in which there is 'Resource' field, contains one single (*). In that case, the script returns 'False', then 'True' in any other case.

## Requirements:

- Python 3.x 
- pandas library
- tkinter library

## How to use:

1. Run the script: python main.py
2. A dialog box will appear asking you to select JSON file - others are disabled
3. The script will validate the chosen file for two required fields (as in AWS::IAM::Role Policy definition) : 'PolicyName' and 'PolicyDocument'.
4. If a required field is missing, an error message will be shown, and you'll be prompted to choose another file.
5. If both fields are present, the script will check the 'Resource' field within 'PolicyDocument'.
6. If the 'Resource' field contains exactly one wildcard (*), the script will return False. Otherwise, it will return True.

### Notes:

Folder 'test_Files_JSON' is used for Unit Tests. All of them are described in python unitTests.py file, as well as which one contains which problem, that program should catch.