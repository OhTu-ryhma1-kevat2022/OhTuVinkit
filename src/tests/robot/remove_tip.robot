*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Add A Tip And Delete It
    Create User And Go To Login Page
    Login And Go To Tip Creating Page
    Adding A New Tip With Valid Title And Link
    Main Page Should Be Open
    Click Button  Poista vinkki
    Handle Alert
    Page Should Not Contain  test title

*** Keywords ***
Create User And Go To Login Page
    Create User  test_user  test1234
    Go To Home And Login Page
    Home And Login Page Should Be Open

Login And Go To Tip Creating Page
    Go To Home And Login Page
    Input Text  username  test_user
    Input Text  password  test1234
    Click Button  Kirjaudu
    Go To New Tip Page

Adding A New Tip With Valid Title And Link
    Input Text  title  test title
    Input Text  link  https://testlink.com/robot
    Click Button  Lisää vinkki
