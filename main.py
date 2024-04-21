import pandas as pd
from tkinter import Tk, messagebox
from tkinter.filedialog import askopenfilename

Tk().withdraw()


def json_method():

    required_field_index = 0
    required = ('PolicyName', 'PolicyDocument')

    while required_field_index < 3:
        filename = askopenfilename(title='Select file', filetypes=[('json files', "*.json")])
        data = pd.read_json(filename)
        while required_field_index < 2:
            policy = data.get(required[required_field_index])
            if policy is None:
                messagebox.showinfo(title='Error', message=f"Your JSON file does not contain required "
                                                           f"'{required[required_field_index]}'"
                                                           f" content, can't process further.")
                filename = askopenfilename(title='Select file', filetypes=[('json files', "*.json")])
                data = pd.read_json(filename)
                required_field_index = 0
            else:
                required_field_index += 1

        try:
            policy = data.get('PolicyDocument', {}).get('Statement')[0].get('Resource')
            required_field_index += 1
            if policy == "*":
                return False
            else:
                return True
        except TypeError:
            messagebox.showinfo(title='Error', message=f"Your JSON file does not contain required 'Resource'"
                                                       f" content, can't process further.")
            required_field_index = 0


print(json_method())


