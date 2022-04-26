*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Login And Go To Tip Creating Page
Test Teardown  Log Out


*** Test Cases ***
Adding A New Tip Fails If All Fields Are Left Empty
    Submit New Tip
    Adding A Tip Should Fail With Message  Title and link are required!

Adding A New Tip Fails If Title Is Not Provided
    Set Link  https://testlink.com/robot
    Submit New Tip
    Adding A Tip Should Fail With Message  Title and link are required!

Adding A New Tip Fails If Link Is Not Provided
    Set Title  this is a title
    Submit New Tip
    Adding A Tip Should Fail With Message  Title and link are required!

Adding A New Tip Succeeds With Valid Title And Link
    Set Title  This is a title
    Set Link  https://testlink.com/robot
    Submit New Tip
    Adding A Tip Should Succeed

*** Keywords ***
Adding A Tip Should Fail With Message
    [Arguments]  ${message}
    New Tip Page Should Be Open
    Page Should Contain  ${message}

Adding A Tip Should Succeed
    Sleep  3 seconds
    Main Page Should Be Open
    Page Should Contain  This is a title

Submit New Tip
    Click Button  Lisää vinkki

Set Title
    [Arguments]  ${title}
    Input Text  title  ${title}

Set Link
    [Arguments]  ${link}
    Input Text  link  ${link}

Login And Go To Tip Creating Page
    Go To Home And Login Page
    Input Text  username  test_user
    Input Text  password  test1234
    Click Button  Kirjaudu
    Go To New Tip Page