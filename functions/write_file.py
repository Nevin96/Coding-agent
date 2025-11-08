import os
from google.genai import types

def write_file(working_directory,file_path,content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory,file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f"ERROR : '{file_path}' is not in working directory"
    parent_dir = os.path.dirname(abs_file_path) 
    if not os.path.isdir(parent_dir):
        try:
            os.makedirs(parent_dir)
        except Exception as e:
            return f"could not create parent dirs: {parent_dir}"
    try:
        with open(abs_file_path,'w') as f:
            f.write(content)
        return f"succesfully wrote to '{file_path}' ({len(content)} characters)"
    except Exception as ex:
        return f'failed to write to file: "{file_path}"'
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Overwrites an existing file and writes to a new file if it doesnt exist (creates rwuired parent dirs safely), constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="the path to the file to write"
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="the content to write to the file as a string"
            )
        },
    ),
)