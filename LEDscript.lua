------------------------------------------------------------------------------
-- NIHIDTool (LED) output report example script
------------------------------------------------------------------------------

inits = device:createReport(0xa0)
inits:fill(0)
device:sendOutputReport(inits)


leds0 = device:createReport(0x82)
leds0:fillRGB(63,63,63)
device:sendOutputReport(leds0)


-- sleep 2 seconds
--system.sleep(2000)

--print("setting all LED levels to 127")
--device:setLEDLevel(127)

--system.sleep(2000)

--print("all LEDs off")
--device:setLEDLevel(0)
