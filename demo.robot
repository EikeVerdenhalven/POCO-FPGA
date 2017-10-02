*** Settings ***
Library    Remote    http://10.1.226.121:8270       WITH NAME    POCOBox

Library   HIDtooling.py
Library   Collections

*** Test Cases ***

#Demo LED
#    Enumerate LED States

Check Color LEDS
    Set HID Mode
    : FOR           ${index}     IN RANGE   ${61}
    \  Check LED    ${index}     ${0}      ${0}       ${99}
    \  Check LED    ${index}     ${0}      ${99}      ${0}
    \  Check LED    ${index}     ${99}     ${0}       ${0}


*** Keywords ***

Enumerate LED States
    : FOR  ${index}       IN RANGE    ${59}
    \   ${rgbstate}=      POCOBox.get_Keybed_RGB_LED    ${index}
    \   Log To Console    ${rgbstate}


Check LED
    [Arguments]           ${key_index}    ${r}   ${g}   ${b}
    Set Key RGB Percent   ${key_index}    ${r}   ${g}   ${b}    ${61}
#    Sleep    2 ms
    ${act_rgb}=             POCOBox.get_Keybed_RGB_LED    ${key_index}
    Match RGB With Error    ${act_rgb}    ${r}   ${g}   ${b}   ${8}
