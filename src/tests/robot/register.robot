*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Login Page


*** Test Cases ***
User Register Successfully With Available Username
    Go To Register Page
    Set Username  newUser
    Set Password  test1234
    Set Confirmatin Password  test1234
    Submit Register
    Main Page Should Be Open
    Log Out

User Can Not Register With Taken Username
    Go To Register Page
    Set Username  test_user
    Set Password  test1234
    Set Confirmatin Password  test1234
    Submit Register
    Register Should Fail With Message  User with username test_user already exists

User Registeration Fails With Incomplete Data
    Go To Register Page
    Set Username  newUser
    Submit Register
    Register Should Fail With Message  Username and password are required

User Registeration Fails When Passwords Do Not Match
    Go To Register Page
    Set Username  newUser
    Set Password  test1234
    Set Confirmatin Password  test123456
    Submit Register
    Register Should Fail With Message  Password do not match

*** Keywords ***
Create User And Go To Login Page
    Create User  test_user  test1234
    Go To Home And Login Page
    Home And Login Page Should Be Open

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Confirmatin Password
    [Arguments]  ${confirmation}
    Input Text  password2  ${confirmation}

Submit Register
    Click Button  Luo tunnus
Log Out
    Click Link  Kirjaudu ulos

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}