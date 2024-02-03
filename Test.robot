*** Settings ***
Library       Process
Library       OperatingSystem

*** Variables ***
${python_script}        siliconlabs.py
${application_name}    silicon-labs-desktop-app
${python_executable}   C:\\Users\\Lenovo T490\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe

*** Test Cases ***
Run Predefined Python Method
    ${result}    Run Process    ${python_executable}    .\\${python_script}
    Log    ${result.stdout}
    Log    ${result.stderr}
    Should Be Equal As Numbers    ${result.rc}    0
