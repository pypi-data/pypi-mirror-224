#!/bin/bash

run_and_extract() {
    local python_code="$1"
    
    # Run the Python code and redirect the output to a temporary file
    python3 -c "$python_code" > /tmp/swiftly_output.txt

    # Extract the desired output from the file
    local result=$(grep -oP 'SWIFT==<\K[^>]*' /tmp/swiftly_output.txt)

    # Remove the temporary file
    rm /tmp/swiftly_output.txt

    # Return the result
    echo "$result"
}