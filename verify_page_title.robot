*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}      https://www.google.com
${BROWSER}  chrome

*** Test Cases ***
Verify Page Title And Capture Screenshot
    Open Browser    ${URL}    ${BROWSER}
    Set Selenium Speed    5s
    Maximize Browser Window
    Title Should Be    Google
    Capture Page Screenshot
    Close Browser

