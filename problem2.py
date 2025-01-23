while True:
    if bumper_a.pressing() and bumper_b.pressing(): 
        led_h.on()
        led_g.off()
    else:
        led_h.off()
        led_g.on()
