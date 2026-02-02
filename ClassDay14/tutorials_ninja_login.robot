*** Settings ***
Library    SeleniumLibrary
Library    DataDriver    file=testdata.xlsx    sheet_name=Sheet1
Test Template    TutorialsNinja Login With Excel
Test Setup    Open TutorialsNinja
Test Teardown    Close TutorialsNinja

*** Variables ***
${URL}       https://tutorialsninja.com/demo/
${BROWSER}   chrome

*** Keywords ***
Open TutorialsNinja
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Click Element    xpath=//span[text()='My Account']
    Click Element    xpath=//a[text()='Login']

TutorialsNinja Login With Excel
    [Arguments]    ${email}    ${password}
    Wait Until Element Is Visible    id=input-email    15s
    Input Text    id=input-email    ${email}
    Input Text    id=input-password    ${password}
    Click Button    xpath=//input[@value='Login']
    Wait Until Element Is Visible    xpath=//h2[text()='My Account']    15s
    Capture Page Screenshot
    Logout From TutorialsNinja

Logout From TutorialsNinja
    Click Element    xpath=//span[text()='My Account']
    Click Element    xpath=//a[text()='Logout']
    Wait Until Element Is Visible    xpath=//h1[text()='Account Logout']    10s

Close TutorialsNinja
    Close Browser

*** Test Cases ***
Login with user from Excel
    Log    Executed via DataDriver

