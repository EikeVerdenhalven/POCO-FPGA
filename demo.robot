*** Settings ***
Library    Remote    http://10.1.226.121:8270       WITH NAME    POCOBox

Library   HIDtooling.py
Library   Collections

*** Test Cases ***

#Demo LED
#    Enumerate LED States

Check Color LEDS
    Set HID Mode
    : FOR           ${index}    IN RANGE   ${60}
    \  Check LED    ${index}     ${100}    ${100}    ${100}


*** Keywords ***

Enumerate LED States
    : FOR  ${index}       IN RANGE    ${59}
    \   ${rgbstate}=      POCOBox.get_Keybed_RGB_LED    ${index}
    \   Log To Console    ${rgbstate}


Check LED
    [Arguments]           ${key_index}    ${r}   ${g}   ${b}
    Set Key RGB Percent   ${key_index}    ${r}   ${g}   ${b}    ${61}
    Sleep    5 ms
    ${act_rgb}=             POCOBox.get_Keybed_RGB_LED    ${key_index}
    Match RGB With Error    ${act_rgb}    ${r}   ${g}   ${b}   ${0.5}
