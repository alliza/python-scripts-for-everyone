import os

SQL_FOLDER_PATH = '' # add your source folder
EXPORT_FOLDER_NAME = 'json-folder'
DESCRIPTION = 'description'

def main():
    try:
        # Create the export folder if it doesn't already exist
        export_folder_path = create_export_folder()
        
        # Loop through all the files in the SQL folder
        for filename in os.listdir(SQL_FOLDER_PATH):
            # Check if the current item is a file
            if os.path.isfile(os.path.join(SQL_FOLDER_PATH, filename)):
                # Get the full path of the current SQL file
                sql_file_path = os.path.abspath(os.path.join(SQL_FOLDER_PATH, filename))
                # Modify the last line of the SQL file
                sql_lines = modify_last_line(sql_file_path)
                # Export the modified SQL file to JSON format
                export_json_file(sql_file_path, sql_lines, export_folder_path)
    except OSError as e:
        print(f'Error: {e}')

def modify_last_line(sql_file_path):
    # Open the input SQL file for reading and create an empty list to store the modified lines
    with open(sql_file_path, 'r') as infile:
        lines = infile.readlines()
        # Loop over the lines in the list and modify the last line of each
        for i in range(len(lines)):
            lines[i] = lines[i].rstrip() + "\\n"
        # Join the modified lines to a single line 
        modified_lines = ''.join(lines)
    return modified_lines

def export_json_file(sql_file_path, sql_lines, export_folder_path):
    # Get the base name of the SQL file without the extension
    sql_basename = os.path.splitext(os.path.basename(sql_file_path))[0]
    # Create the export file path with the JSON extension
    export_file_path = os.path.join(export_folder_path, f"{sql_basename}.json")
    # Open the output file for writing and write the modified lines to it in JSON format
    with open(export_file_path, 'w') as outfile:
        template = '{ \n "name": "' + sql_lines + '",\n "description": "' + DESCRIPTION + '" \n}'
        outfile.write(template)

def create_export_folder():
    # Get the current directory path where the Python file exists
    current_folder_path = os.path.dirname(os.path.abspath(__file__))
    # Create the export folder path by joining the current directory path with the export folder name
    export_folder_path = os.path.join(current_folder_path, EXPORT_FOLDER_NAME)
    # Create the export folder if it doesn't already exist and print a message
    if not os.path.exists(export_folder_path):
        os.makedirs(export_folder_path)
        print(f"Created folder: {export_folder_path}")
    else:
        print(f"Folder already exists: {export_folder_path}")
    return export_folder_path

if __name__ == '__main__':
    main()
