#!/bin/bash

run_and_extract() {
    local python_code="$1"
    
    # Run the Python code, display the output to the user, and redirect the output to a temporary file
    python3 -c "$python_code" | tee /tmp/swiftly_output.txt

    # Extract the desired output from the file using awk
    local result=$(awk -F'SWIFT==<|>==LY' '/SWIFT==</ {print $2}' /tmp/swiftly_output.txt)

    # Remove the temporary file
    rm /tmp/swiftly_output.txt

    # Return the result
    echo "$result"
}
