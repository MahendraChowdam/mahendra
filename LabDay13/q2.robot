*** Settings ***
Library    DataDriver    file=testdata.csv
Test Template    Validate Login Using Keyword

*** Keywords ***
Validate Login Using Keyword
    [Arguments]    ${username}    ${password}
    Login Keyword    ${username}    ${password}

Login Keyword
    [Arguments]    ${username}    ${password}
    Run Keyword If    '${username}' == 'admin' and '${password}' == 'admin123'
    ...    Login Should Pass
    ...    ELSE
    ...    Login Should Fail

Login Should Pass
    Log    Login Successful
    Should Be Equal    PASS    PASS

Login Should Fail
    Log    Login Failed
    Should Be Equal    FAIL    FAIL

*** Test Cases ***
Login test using CSV
    Log    Executed using external CSV
