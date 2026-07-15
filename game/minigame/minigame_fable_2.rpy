init 15 python:
    fable_minigame_bar = 90
    fable_minigame_score = 0
    fable_you_press_button = 0
    fable_score_goal = 5 #Change this to edit the amount of presses needed
init:
    transform fable_point_move(frp):
        subpixel True
        rotate_pad True
        align(0.5,1.22)
        rotate frp
screen fable_2_minigame:
    add "minigame/Fable_bar.png" align(0.5,0.5)
    add "minigame/Fable_point.png" at fable_point_move(fable_minigame_bar)
    text "[fable_minigame_score]/[fable_score_goal]\nNumber of clicks" align(0.5,0.1)
    text "[fable_minigame_bar]\nThe meaning of the bar" align(0.5,0.2) #COMMENT THIS OUT IN THE FINAL BUILD
    text "[fable_you_press_button]" align(0.5,0.3)

    if fable_minigame_bar >= -14 and fable_minigame_bar <= 14:
        key "K_SPACE":
            if fable_you_press_button == 0:
                if fable_minigame_score < (fable_score_goal - 1):
                    action [SetVariable("fable_minigame_score", fable_minigame_score + 1), SetVariable("fable_you_press_button", fable_you_press_button + 1), Show("you_press_button_good")]
                else:
                    action Jump("end")
            elif fable_you_press_button == 1:
                action SetVariable("fable_minigame_score", fable_minigame_score + 0)
    else:
        key "K_SPACE" action [SetVariable("fable_minigame_score", 0), Show("you_press_button_bad")]

screen fable_timer_left:
    timer 0.0001 repeat True action [If(fable_minigame_bar >= -90, SetVariable("fable_minigame_bar", fable_minigame_bar - 1)),If(fable_minigame_bar == -90, Hide("fable_timer_left"), Show("fable_timer_right")), If(fable_minigame_bar == -90, SetVariable("fable_you_press_button", 0))]
screen fable_timer_right:
    timer 0.0001 repeat True action [If(fable_minigame_bar <= 90, SetVariable("fable_minigame_bar", fable_minigame_bar + 1)),If(fable_minigame_bar == 90, Hide("fable_timer_right"), Show("fable_timer_left")), If(fable_minigame_bar == 90, SetVariable("fable_you_press_button", 0))]

screen you_press_button_good:
    text "{color=#1e8e00}Good Work!{/color}" at fable_move_good
    timer 1.0 action Hide("you_press_button_good")
screen you_press_button_bad:
    #hbox at fable_move_bad:
    text "{color=#950000}Oops...\nTry Again.{/color}" at fable_move_bad
    timer 1.0 action Hide("you_press_button_bad")
transform fable_move_good:
    align(0.5,0.5)
    linear 0.05 zoom 1.3
    linear 0.5 zoom 1.0 alpha 0.0
transform fable_move_bad:
    align(0.5,0.5)
    linear 0.04 xalign 0.5
    linear 0.06 xalign 0.495
    linear 0.06 xalign 0.515
    linear 0.06 xalign 0.5
    linear 0.5 alpha 0.0
################################################################################
label start_minigame:
    show screen fable_timer_left
    call screen fable_2_minigame
################################################################################
label end_minigame: #End minigame. And jump continue game
    hide screen fable_2_minigame
    hide screen fable_timer_left
    hide screen fable_timer_right
    $ renpy.pause(0.3)
    jump end #continue game
