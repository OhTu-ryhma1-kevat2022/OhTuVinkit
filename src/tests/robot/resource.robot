*** Settings ***
Library  SeleniumLibrary
Library  ./AppLibrary.py

*** Variables ***
${SERVER}  127.0.0.1:5000
${BROWSER}  headlesschrome
${DELAY}  1.0 seconds
${HOME URL}  http://${SERVER}
${LOGIN URL}  http://${SERVER}
${REGISTER URL}  http://${SERVER}/register
${NEW TIP URL}  http://${SERVER}/new_book_tip

*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Home And Login Page Should Be Open
    Title Should Be  OhTu Vinkit - Etusivu

Main Page Should Be Open
    Title Should Be  OhTu Vinkit - Main

Register Page Should Be Open
    Title Should Be  OhTu Vinkit - Register

New Tip Page Should Be Open
    Title Should Be  OhTu Vinkit - Lisää vinkki

Go To Home And Login Page
    Go To  ${HOME URL}

Go To Register Page
    Go To  ${REGISTER URL}

Go To New Tip Page
    Go To  ${NEW TIP URL}

Log Out
    Click Link  Kirjaudu ulos
