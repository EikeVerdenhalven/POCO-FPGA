*** Settings ***
Library    Remote    http://10.1.226.121:8270       WITH NAME    POCOBox


*** Test Cases ***

Demo RGB LED
   Enumerate LED States

*** Keywords ***

Enumerate LED States
    ${rgbstates}=         POCOBox.get_keybed_LEDs
    : FOR  ${index}       IN RANGE    ${59}
    \   ${rgbstate}=      POCOBox.get_Keybed_RGB_LED    ${index}
    \   Log To Console    ${rgbstate}
