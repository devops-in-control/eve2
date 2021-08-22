*** Settings ***
Documentation     Test suite for charger request page
...
...               This test has a workflow that is created using keywords in
...               the imported resource file.
Library           SeleniumLibrary
Library      XvfbRobot



*** Variables ***
${SERVER}         localhost:8080
${BROWSER}        Firefox
${DELAY}          0
${VALID PHONE NUMBER}     0612345678
${INVALID PHONE NUMBER}    061234567a
${REQUEST URL}    http://${SERVER}/order/
${SUCCESS URL}    http://${SERVER}/order/
${ERROR MESSAGE}    Please enter a valid phone number for shipping updates.

*** Keywords ***
Open Browser To Request Page
    Open Browser    ${REQUEST URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    ${DELAY}
    Request Page Should Be Open

Request Page Should Be Open
    Title Should Be    Request charger

Input Phone Number
    [Arguments]    ${phone_number}
    Input Text    phone_number    ${phone_number}

Submit Request
    Click Button    submit_request

Success Page Should Be Open
    Location Should Be    ${SUCCESS URL}
    Title Should Be    Success

Error Message Is Visible
    Element Should Contain  id:invalid-phone-number     ${ERROR MESSAGE}


*** Test Cases ***
Invalid Phone Number
    Open Browser To Request Page
    Input Phone Number    ${INVALID PHONE NUMBER}
    Submit Request
    Request Page Should Be Open
    Error Message Is Visible
    [Teardown]    Close Browser
    
Valid Phone Number
    Open Browser To Request Page
    Input Phone Number    ${VALID PHONE NUMBER}
    Submit Request
    Success Page Should Be Open
    [Teardown]    Close Browser