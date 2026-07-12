#!/bin/bash

# Check if a problem name was provided
if [ -z "$1" ]; then
  echo "Error: Please provide a problem name."
  echo "Usage: ./make_prob.sh \"two-sum\""
  exit 1
fi

# Assign the argument to a variable
PROBLEM_NAME=$1

# Create the directory and the empty README.md
mkdir -p "$PROBLEM_NAME"
touch "$PROBLEM_NAME/README.md"
touch "$PROBLEM_NAME/solution.py"

echo "Created directory '$PROBLEM_NAME' with an empty README.md"
