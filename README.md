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
