*** Settings ***
Library  SeleniumLibrary
Library  ../../AppLibrary.py

*** Variables ***
${SERVER}  127.0.0.1:5000
${BROWSER}  headlesschrome
${DELAY}  0.05 seconds
${HOME URL}  http://${SERVER}
${LOGIN URL}  http://${SERVER}
${REGISTER URL}  http://${SERVER}/register

*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Home And Login Page Should Be Open
    Title Should Be  OhTu-Vinkit-Etusivu

Main Page Should Be Open
    Title Should Be  OhTu-Vinkit-Main

Register Page Should Be Open
    Title Should Be  OhTu-Vinkit-Register

Go To Home And Login Page
    Go To  ${HOME URL}

Go To Register Page
    Go To  ${REGISTER URL}

Log Out
    Click Link  Kirjaudu ulos
