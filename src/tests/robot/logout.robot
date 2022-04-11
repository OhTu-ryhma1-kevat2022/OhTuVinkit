*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Log In


*** Test Cases ***
Message Should Be Displayed Indicating User Has Logged Out
    Log Out
    Logout Should Succeed With Message  Olet kirjautunut ulos!

*** Keywords ***
Logout Should Succeed With Message
    [Arguments]  ${message}
    Home And Login Page Should Be Open
    Page Should Contain  ${message}

Log Out
    Click Link  Kirjaudu ulos

Create User And Log In
    Create User  test_user  test1234
    Go To Home And Login Page
    Input Text  username  test_user
    Input Text  password  test1234
    Click Button  Kirjaudu
