*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Login Page


*** Test Cases ***
User Login Succeed With Correct Credentials
    Input Credentials  test_user  test1234
    Submit Credentials
    Login Should Succeed

Login Fails With Incorrect Username
    Input Credentials  wrongPerson  test1234
    Submit Credentials
    Login Should Fail With Message  Incorrect username or password

Login Fails With Incorrect Password
    Input Credentials  test_user  wongpass
    Submit Credentials
    Login Should Fail With Message  Incorrect username or password

Login Fails With Empty Fields
    Submit Credentials
    Login Should Fail With Message  Username and password are required

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

Input Credentials
    [Arguments]  ${username}  ${password}
    Set Username  ${username}
    SEt Password  ${password}