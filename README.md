# Go Program Runner from Python

This project demonstrates how to run a Go program from a Python script and pass arguments to the Go program using the Python subprocess module.

## How It Works

1. **Go Program (`main.go`)**:
   The Go program takes command-line arguments, processes them, and prints them to the console. It simply prints each argument passed to it.

2. **Python Script (`main.py`)**:
   The Python script uses the `subprocess` module to execute the Go program with arguments passed from the Python script.

### Flow:
- The Python script receives arguments as a string.
- The arguments are passed to the Go program as a command-line argument string.
- The Go program processes these arguments and prints them to the terminal.
- The Python script captures the output from the Go program and displays it in the Python terminal.

## Prerequisites

- **Go**: Make sure that Go is installed on your system. You can download Go from the official site: [Download Go](https://golang.org/dl/).
- **Python**: The script uses Python’s built-in `subprocess` and `sys` modules.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/korkuthuseyin/python_run_golang.git
   cd python_run_golang

## Example Usage

### Step 1: Build the Go Program

First, ensure that the Go program is compiled by running the following command in the directory where `main.go` is located:

```bash
go build -o go_built main.go
```
 ### Step 2: Run Python file with arguments

 ```bash
python3 main.py 'arg1 arg2 arg3'
```
Note that your arguments should be in the single quote for sending these to go file as a one string

## Example Output
```
Output from gomat:
Arguments passed to the program:
Argument 1: arg1
Argument 2: arg2
Argument 3: arg3
```
