#!/bin/bash


# Define color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color


# Assigning default file names
expected_file="expected_output.txt"
output_file="output.txt"
diff_file="diff_output.txt"

# Override default file names if arguments are provided
if [[ $# -eq 3 ]]; then
  expected_file=$1
  output_file=$2
  diff_file=$3
elif [[ $# -ne 0 ]]; then
  echo "Usage: $0 [expected output file] [output file] [diff output file]"
  echo "       If no files are provided, defaults to comparing expected_output.txt and output.txt"
  exit 1
fi

# Check if the expected file exists
if [ ! -f "$expected_file" ]; then
  echo -e "${RED}Output file $expected_file not found.${NC}"
  exit 1
fi

# Check if the output file exists
if [ ! -f "$output_file" ]; then
  echo -e "${RED}Output file $output_file not found.${NC}"
  exit 1
fi

# Comparing files
diff $expected_file $output_file > $diff_file

# Check the exit status of the diff command
if [ $? -eq 0 ]; then
  echo -e "${GREEN}Test passed: Files $expected_file and $output_file are identical.${NC}"
  if [ -f "$diff_file" ]; then
      rm "$diff_file"  
  fi
else
  echo -e "${RED}Test failed: Files $expected_file and $output_file differ.${NC}"
  echo "Showing differences saved to $diff_file" 
  cat $diff_file
fi

#delete diff file if exists
