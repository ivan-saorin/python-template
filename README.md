# python-template
# A python template project

No problem at all, here are the instructions for setting up a Python project with a virtual environment that can be launched from the command line on Windows 11, with additional chapters on how to easily maintain a `requirements.txt` file, how to run your `main.py` file as a Windows command with parameter parsing, how to organize your sources and tests in separate directories, how to have colored console logging, and how to set up the project as a template in your GitHub account, and how to add the command to the virtual environment in case you don't want to change your PATH environment variable:

## Setting up a Python Project with Virtual Environment on Windows 11

1. Install Python: Go to the [Python download page](https://www.python.org/downloads/windows/) and download the latest version of Python for Windows. Follow the installation instructions to complete the installation.

2. Open a command prompt: Press `Win + R` keys, type `cmd` and press `Enter` to open a command prompt.

3. Create a project directory: In the command prompt, navigate to the location where you want to create your project directory using the `cd` command. Once you are in the desired location, create a new directory for your project using the `mkdir` command. For example, to create a project directory named `my_project`, type:

    ```
    cd C:\projects
    mkdir my_project
    cd my_project
    ```

4. Create a virtual environment: In the command prompt, type the following command to create a virtual environment:

    ```
    python -m venv my_env
    ```

    This will create a new directory named `my_env` within your project directory.

5. Activate the virtual environment: To activate the virtual environment, type the following command:

    ```
    .\my_env\Scripts\activate
    ```

    You should see the name of your virtual environment in parentheses at the beginning of your command prompt, indicating that the virtual environment is now active.

6. Install dependencies: Install any required packages or libraries for your project using the `pip` command. For example, to install `numpy`, type:

    ```
    pip install numpy
    ```

7. Maintain `requirements.txt`: To easily maintain a `requirements.txt` file that lists all of the dependencies for your project, use the `pip freeze` command. This will output a list of all installed packages and their versions in the format `package==version`. To save this list to a file named `requirements.txt`, type:

    ```
    pip freeze > requirements.txt
    ```

8. Organize your project files: Organize your source code files in a directory named `src`, and your test files in a directory named `tests`. For example:

    ```
    my_project/
        src/
            main.py
        tests/
            test_main.py
    ```

9. Add parameters parsing to your `main.py` file: To parse parameters passed to your `main.py` file from the command line, you can use the built-in `argparse` module in Python. Here is an example code snippet for adding two optional parameters `--input_file` and `--output_file` to your `main.py` file:

    ```python
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", help="input file path")
    parser.add_argument("--output_file", help="output file path")
    args = parser.parse_args()

    input_file = args.input_file
    output_file = args.output_file
    
    # Your code here
    ```

10. Create a Windows command for your `main.py` file: To be able to run your `main.py` file as a Windows command, you need
to create a batch file with a `.cmd` extension that calls the `python` command and passes the parameters to your `main.py` file. Here is an example batch file named `run_my_project.cmd`:

    ```
    @echo off
    setlocal EnableDelayedExpansion
    
    set "SCRIPT_DIR=%~dp0"
    set "SCRIPT_DIR=!SCRIPT_DIR:%CD%\=!"
    set "SCRIPT_DIR=!SCRIPT_DIR:\=\\!"
    set "PROJECT_NAME=my_project"
    
    python !SCRIPT_DIR!src\main.py %*
    ```

    Save this file in your project directory.

11. Add colored console logging to your `main.py` file: To add colored console logging to your `main.py` file, you can use the `colorlog` module. Here is an example code snippet for adding colored logging to your `main.py` file:

    ```python
    import logging
    import colorlog
    
    # Create a logger object
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    
    # Create a colored console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = colorlog.ColoredFormatter(
        '%(log_color)s%(levelname)s:%(message)s%(reset)s'
    )
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    
    # Log some messages with different levels
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')
    ```

12. Add the command to the virtual environment: If you don't want to change your PATH environment variable, you can add the command to run your `main.py` file to the virtual environment. To do this, create a new batch file named `activate.bat` in the `Scripts` directory of your virtual environment (e.g., `my_env\Scripts\activate.bat`) with the following content:

    ```
    @echo off
    set "PATH=%PATH%;%VIRTUAL_ENV%\..\"
    ```

    This will add the parent directory of the virtual environment (i.e., the directory containing the `python.exe` executable) to the `PATH` environment variable when the virtual environment is activated.

13. Set up the project as a template in your GitHub account: To set up your project as a template in your GitHub account, you can follow these steps:

    a. Create a new repository on GitHub with a name that ends with `-template`. For example, `my-project-template`.
    
    b. Clone the repository to your local machine using the command line. For example:
    
        ```
        git clone https://github.com/your-username/my-project-template.git
        cd my-project-template
        ```
    
    c. Copy the contents of your project directory (excluding the virtual environment directory) to the cloned repository directory. For example:
    
        ```
        cp -r /path/to/my_project/* .
        ```
    
    d. Commit the changes and push to the `main` branch:
    
        ```
        git add .
        git commit -m "Initial commit"
        git push -u origin main
        ```
    
    e. Your project template is now ready to be used by others. When someone wants to create a new project using your template, they can click the "Use this template" button on your repository page and enter the necessary information.
