*** Settings ***
Library    Remote    http://10.1.226.121:8270       WITH NAME    POCOBox

Library   HIDtooling.py
Library   Collections

*** Test Cases ***

Demo LED
    Enumerate LED States

Check Color LEDS
    Check LED    ${0}     ${12}    ${12}    ${0}
    Check LED    ${10}    ${22}    ${12}    ${0}
    Check LED    ${15}    ${12}    ${92}    ${0}
    Check LED    ${25}    ${12}    ${12}    ${64}

*** Keywords ***

Enumerate LED States
    : FOR  ${index}       IN RANGE    ${59}
    \   ${rgbstate}=      POCOBox.get_Keybed_RGB_LED    ${index}
    \   Log To Console    ${rgbstate}

Check LED
    [Arguments]    ${key_index}    ${r}    ${g}    ${b}
    set_single_Key_RGB   ${key_index}   ${r}    ${g}    ${b}    ${61}
    Sleep    10 ms
    ${act_rgb}=      POCOBox.get_Keybed_RGB_LED    ${key_index}
    Log To Console   ${act_rgb}
