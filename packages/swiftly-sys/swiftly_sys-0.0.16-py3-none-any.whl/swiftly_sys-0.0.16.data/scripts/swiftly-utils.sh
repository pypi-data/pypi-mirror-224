#!/bin/bash

run_python_and_get_result() {
    local python_code="$1"
    
    # Run the Python code
    python3 -c "$python_code"
    
    # Determine the temp directory path (for Linux and Mac OSX)
    local temp_dir="/tmp"
    
    local result_file_path="${temp_dir}/swiftly_cli_result.txt"
    
    # Read the result
    local result=$(cat "$result_file_path")
    
    # Remove the temporary file
    rm "$result_file_path"
    
    # Return the result
    echo "$result"
}
