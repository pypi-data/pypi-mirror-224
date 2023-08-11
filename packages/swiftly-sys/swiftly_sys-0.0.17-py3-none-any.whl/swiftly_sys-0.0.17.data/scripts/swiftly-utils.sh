#!/bin/bash

read_cli_result() {
    local temp_dir="/tmp"

    local result_file_path="${temp_dir}/swiftly_cli_result.txt"
    
    # Read the result
    local result=$(cat "$result_file_path")
    
    # Remove the temporary file
    rm "$result_file_path"
    
    # Return the result
    echo "$result"
}
