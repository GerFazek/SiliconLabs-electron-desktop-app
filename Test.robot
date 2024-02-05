*** Settings ***
Library       Process
Library       OperatingSystem

*** Variables ***
${python_script}        silabsrobot.py
${application_name}    silicon-labs-desktop-app

*** Test Cases ***
Run Predefined Python Method
    ${result}    Run Process    python    .\\${python_script}
    Log    ${result.stdout}
    Log    ${result.stderr}
    Should Be Equal As Numbers    ${result.rc}    0
