import re
import os
import glob

def remove_comments(input_text):
    # Remove C++ single-line comments
    input_text = re.sub(r'\/\/[^\n]*', '', input_text)
    
    # Remove C++ multi-line comments
    input_text = re.sub(r'\/\*[\s\S]*?\*\/', '', input_text)
    
    return input_text

def copy_cpp_header_without_comments(input_file):
    try:
        # Extract the file name (without extension) from the input file
        base_name, _ = os.path.splitext(input_file)
        
        # Create the output file name by adding "_output" before the extension
        output_file = f"semComents/{base_name}_output.h"

        with open(input_file, 'r') as infile:
            cpp_code = infile.read()
            
            # Remove comments from the C++ code
            cpp_code = remove_comments(cpp_code)
            
            with open(output_file, 'w') as outfile:
                outfile.write(cpp_code)
                
            print(f'Successfully copied {input_file} to {output_file} without comments.')
    except FileNotFoundError:
        print(f'Error: {input_file} not found.')
    except Exception as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    # List all .h files in the current directory
    header_files = glob.glob('*.h')
    
    for input_file in header_files:  
        copy_cpp_header_without_comments(input_file)