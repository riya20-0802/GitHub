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
define s = Character("Snoopy", color="#b06900")
define w = Character("Woodstock", color="#5C4033")

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
        xalign 0.20
        yalign 0.55
        zoom 0.4
    with dissolve

    w "Chirp chirp! (I want a slice!)"
    
    jump game_ending

label take_nap:
    hide snoopy
    hide woodstock
    with dissolve

    scene bg nap_time:
        size (1920, 1080)
    with dissolve
    
    s "Zzz... the sound of the autumn wind outside is perfect sleeping music... Zzz..."
    w "Zzz..."

    "Snoopy and Woodstock drifted off into a deep, peaceful sleep under their warm flannel blankets."
    "As the fire crackled in the other room, they began to share a lovely autumn dream..."

    menu:
        "Dream about being the Flying Ace soaring through the sky!":
            jump branch_dream_ace

        "Dream about a mountain of chocolate chip cookies!":
            jump branch_dream_cookies


label branch_dream_ace:
    show thought_bubble:
        xalign 0.30
        yalign 0.10
        zoom 2.0
    with dissolve

    # Forces the Flying Ace to anchor from his true center and sit in the cloud
    show dream_ace:
        xalign 0.34
        yalign 0.22
        yanchor 0.5
        zoom 0.4
    with dissolve

    "Snoopy imagined himself flying high above the orange and red trees, protecting the skies!"
    
    hide thought_bubble
    hide dream_ace
    with dissolve
    jump game_ending


label branch_dream_cookies:
    show thought_bubble:
        xalign 0.30
        yalign 0.10
        zoom 1.7
    with dissolve

    # Forces the cookie mountain to anchor from its true center and sit in the cloud
    show dream_cookies:
        xalign 0.35    # Adjusted slightly to center inside the cloud
        yalign 0.23    # Adjusted slightly to lift into the cloud bubble
        xanchor 0.5
        yanchor 0.5
        zoom 0.26      # Reduced scale from 0.5 to 0.22 to fit properly
    with dissolve

    "In their sleepy minds, a massive mountain of fresh-baked chocolate chip cookies floated by!"
    
    hide thought_bubble
    hide dream_cookies
    with dissolve
    jump game_ending




# --- CUSTOM FINAL THANK YOU OUTRO PAGE ---
label game_ending:
    # Fades out previous items and leaves a clean, elegant final room display (back to the original room)
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
