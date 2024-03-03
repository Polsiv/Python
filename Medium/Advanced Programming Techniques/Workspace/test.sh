#!/bin/bash

YELLOW='\033[0;33m'
NC='\033[0m' # No Color

# Assigning default file names
command="python " #If the code is not compiled, use here the interpreter
main_module="main.py"
expected_output="expected_output.txt"
generated_output="output.txt"
diff_output="diff_output.txt"

if [ $# -eq 1 ]; then
  main_module=$1
elif [ $# -eq 2 ]; then
  main_module=$1
  expected_output=$2
elif [ $# -eq 3 ]; then
  main_module=$1
  expected_output=$2
  generated_output=$3
elif [ $# -gt 3 ]; then
  echo "Usage: $0 [executable name] [expected output name] [generated output name]"
  echo "       If no arguments are provided, defaults names are assigned: 'main', 'expected_output.txt' and 'generated_output.txt'"
  exit 1
fi

# Check if the program exists
if [ ! -f "$main_module" ]; then 
  echo -e "${YELLOW}Main module $main_module not found.${NC}"
  exit 1
fi

echo -e "Invoking $command$main_module"
$command$main_module > $generated_output

bash file_compare.sh $expected_output $generated_output $diff_output