image leaves_falling = SnowBlossom(im.Scale("images/leaf_particle.png", 40, 40), count=25, border=50, xspeed=(-50, 50), yspeed=(100, 250), start=5.0, fast=True)

# --- ANIMATION ROUTINES ---
transform character_jump(x_pos, y_pos):
    xalign x_pos
    yalign y_pos
    linear 0.2 yalign (y_pos - 0.25) # Leaps up into the air
    linear 0.2 yalign y_pos          # Lands back down
    
# Simple cute idling animations to keep them alive
transform snoopy_idle:
    xalign 0.6
    yalign 0.75
    linear 1.5 yalign 0.77
    linear 1.5 yalign 0.75
    repeat

transform woodstock_hover:
    xalign 0.38
    yalign 0.45
    linear 0.8 yalign 0.42
    linear 0.8 yalign 0.45
    repeat

# --- CHARACTER DEFINITIONS ---
define s = Character("Snoopy", color="#ff9900")
define w = Character("Woodstock", color="#ffff00")

# --- THE STORY ---
label start:
    play music "audio/fall_bgm.mp3" loop

    scene bg room:
        size (1920, 1080)
    with dissolve

    show snoopy happy at snoopy_idle:
        zoom 1.5
    
    s "Hello, and welcome to my fall-themed game!"
    
    show woodstock happy at woodstock_hover:
        zoom 0.5
    with easeinleft

    w "Chirp chirp! (Hi there!)"
    s "What should we do on this lovely autumn afternoon? "

    menu:
        "Go outside into the leaves.":
            jump outside

        "Stay in this cozy room.":
            jump stay

# --- OUTSIDE PATH ---
label outside:
    scene bg whitehouse:
        size (1920, 1080)
    with dissolve

    show leaves_falling

    show snoopy happy at snoopy_idle:
        zoom 1.5
    show woodstock happy at woodstock_hover:
        zoom 0.5

    s "This is so much fun! Wow, look at all the autumn leaves! It's so beautiful out here."
    w "Chirp chirp! (Let's play!)"
    s "What should we do out here in the park?"

    menu:
        "Jump right into a giant pile of leaves!":
            jump leaf_jump

        "Go for a peaceful autumn walk!":
            jump autumn_walk

label leaf_jump:
    scene bg leaves:
        size (1920, 1080)
    with dissolve
    show leaves_falling

    # Snoopy and Woodstock execute a physical jumping animation together!
    show snoopy happy at character_jump(0.6, 0.75):
        zoom 1.5
    show woodstock happy at character_jump(0.38, 0.45):
        zoom 0.5

    s "CRUNCH! That was amazing! There are leaves stuck all over my beanie now."
    w "Chirp! (That was awesome!)"
    
    jump game_ending # Sends them to the new wrap-up screen

label autumn_walk:
    hide snoopy
    hide woodstock
    with easeoutright

    scene bg park:
        size (1920, 1080)
    with dissolve
    show leaves_falling

    show snoopy happy at snoopy_idle:
        zoom 1.5
    show woodstock happy at woodstock_hover:
        zoom 0.5
    with easeinleft

    s "The crisp, cool air feels so refreshing, and the trees look beautiful!"
    w "Chirp chirp... (So relaxing...)"
    
    jump game_ending

# --- INSIDE PATH ---
label stay:
    scene bg room:
        size (1920, 1080)
    with dissolve

    show snoopy happy at snoopy_idle:
        zoom 1.5
    show woodstock happy at woodstock_hover:
        zoom 0.5

    s "Great choice! It's so warm and cozy inside!"
    s "How should we spend our cozy afternoon?"

    menu:
        "Bake a warm pumpkin pie!":
            jump bake_pie

        "Curl up on the couch and take a nap!":
            jump take_nap

label bake_pie:
    scene bg kitchen:
        size (1920, 1080)
    with dissolve
    
    show snoopy happy at snoopy_idle:
        zoom 1.5
    show woodstock happy at woodstock_hover:
        zoom 0.5

    s "Mmmm, the whole house smells like cinnamon and pumpkin now! Delicious!"
    
    # This slides the pie nicely onto the kitchen table on the left!
    show pumpkin_pie:
        xalign 0.22
        yalign 0.68
        zoom 0.4
    with dissolve

    w "Chirp chirp! (I want a slice!)"
    
    jump game_ending

label take_nap:
    scene bg room:
        size (1920, 1080)
    with dissolve
    
    show snoopy happy at snoopy_idle:
        zoom 1.5
    show woodstock happy at woodstock_hover:
        zoom 0.5

    s "Zzz... the sound of the autumn wind outside is perfect sleeping music... Zzz..."
    w "Zzz..."
    
    jump game_ending

# --- CUSTOM FINAL THANK YOU OUTRO PAGE ---
label game_ending:
    # Fades out previous items and leaves a clean, elegant final room display
    scene bg room:
        size (1920, 1080)
    with dissolve

    show snoopy happy at snoopy_idle:
        zoom 1.5
    show woodstock happy at woodstock_hover:
        zoom 0.5
    with dissolve

    s "Thanks for helping us have the best autumn afternoon!"
    w "Chirp chirp! (Thank you for playing!)"

    # Displays a final splash screen message before quitting
    "The End! Thank you for playing Snoopy's Autumn Adventure!"
    return
