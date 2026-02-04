*** Settings ***
Library    SeleniumLibrary
Suite Setup    Open Browser To App
Suite Teardown    Close Browser

*** Variables ***
${URL}    http://127.0.0.1:5000
${BROWSER}    chrome

*** Keywords ***
Open Browser To App
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

*** Test Cases ***
Register Patient
    Input Text    name=id    2
    Input Text    name=name    Sita
    Input Text    name=age    28
    Click Element    xpath=//input[@value='Female']
    Input Text    name=contact    8888888888
    Input Text    name=disease    Cold
    Select From List By Label    name=doctor    Dr. Smith
    Click Button    xpath=//button[@type='submit']
    Sleep    2s
