*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser


*** Test Cases ***



*** Keywords ***
Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Home And Login Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Kirjaudu

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Text  password  ${password}

Create User And Go To Login Page
    Create User  test_user  test1234
    Go To Home And Login Page
    Home And Login Page Should Be Open