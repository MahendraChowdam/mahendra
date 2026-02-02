*** Settings ***
Library    SeleniumLibrary
Suite Setup       Open Application
Suite Teardown    Close Application
Test Setup        Start Test
Test Teardown     End Test

*** Variables ***
${URL}      https://www.google.com
${BROWSER}  chrome

*** Keywords ***
Open Application
    Log    ===== SUITE SETUP: Opening browser =====
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Sleep    3s

Close Application
    Log    ===== SUITE TEARDOWN: Closing browser =====
    Sleep    2s
    Close Browser

Start Test
    Log    ----- TEST SETUP: Starting test -----
    Sleep    2s

End Test
    Log    ----- TEST TEARDOWN: Ending test -----
    Sleep    2s

*** Test Cases ***
Verify Google Title
    [Tags]    smoke
    Title Should Be    Google
    Sleep    2s
    Capture Page Screenshot
    Sleep    2s

Verify Page Contains Text
    [Tags]    regression
    Page Should Contain    Google
    Sleep    2s
    Capture Page Screenshot
    Sleep    2s
