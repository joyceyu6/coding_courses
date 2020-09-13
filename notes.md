# Code with Mosh - Complete Python Course

## Shortcut

* (Code) Problems

        Shift + Command(Ctrl if Windows) + M
* Command Palette
  
        Shift + Command(Ctrl if Windows) + P
* Run Python w:
  
  * Instead of "Python3 xxx.py"
  * Search extension for "code runner" and install ".runner", then we can run code with:
  
        Ctrl + alt + n

  * (Not found) change "python -u" to "python3": "Code"->"Preferences"-->"Settings"-->"..."-->"Open Settings.json"-->search "code-runner.executorMap"-->change "User Settings", after last line, add "," type "code-runner.executorMap" then Enter, this will copy "default user settings" to "user settings"; then change "python":"python -u" to "python":"python3"

## Others

### PEP8 (Formatting Python Code)

* Command palette, type in "format", install PEP8
* later repeat and type in "format" will automatically correct OR
* Automatic formatting at "Save": Code --> Preferences --> Settings --> Search "Form
* at and tick "Format on Save"

### Python Implementations

language: define rules, implementation: exeucute code
Python->CPython(or Jython)-->Python Bytecode(or Java Bytecode)-->Python Virtual Machine-->Machine Code

* CPython (default)
* Jython: Java
* IronPython: C#
* PyPy: subset of Python
  
