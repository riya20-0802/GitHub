define s = Character("Snoopy", color="#ff9900")
define w = Character("Woodstock", color="#ffff00")

label start:
    play music "audio/fall_bgm.mp3" loop

    scene bg room:
        size (1920, 1080)
    with dissolve

    # Snoopy starts in the room
    show snoopy happy:
        zoom 1.5
        xalign 0.6
        yalign 0.75
    
    s "Hello, and welcome to my fall-themed game!"
    
    # Woodstock flies into his spot from the left edge of the screen!
    show woodstock happy:
        zoom 0.5
        xalign 0.38
        yalign 0.45
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
    # The outside screen fades in smoothly
    with dissolve

    show snoopy happy:
        zoom 1.5
        xalign 0.6
        yalign 0.75
    show woodstock happy:
        zoom 0.5
        xalign 0.38
        yalign 0.45

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
    
    show snoopy happy:
        zoom 1.5
        xalign 0.6
        yalign 0.75
    show woodstock happy:
        zoom 0.5
        xalign 0.38
        yalign 0.45

    # The vpunch effect shakes the entire game window vertically to simulate the landing!
    with vpunch

    s "CRUNCH! That was amazing! There are leaves stuck all over my beanie now."
    w "Chirp! (That was awesome!)"
    return

label autumn_walk:
    # Snoopy and Woodstock slide off to the right together to start their walk!
    hide snoopy
    hide woodstock
    with easeoutright

    scene bg park:
        size (1920, 1080)
    with dissolve
    
    show snoopy happy:
        zoom 1.5
        xalign 0.6
        yalign 0.75
    show woodstock happy:
        zoom 0.5
        xalign 0.38
        yalign 0.45
    with easeinleft

    s "The crisp, cool air feels so refreshing, and the trees look beautiful!"
    w "Chirp chirp... (So relaxing...)"
    return

# --- INSIDE PATH ---
label stay:
    scene bg room:
        size (1920, 1080)
    with dissolve

    show snoopy happy:
        zoom 1.5
        xalign 0.6
        yalign 0.75
    show woodstock happy:
        zoom 0.5
        xalign 0.38
        yalign 0.45

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
    
    show snoopy happy:
        zoom 1.5
        xalign 0.6
        yalign 0.75
    show woodstock happy:
        zoom 0.5
        xalign 0.38
        yalign 0.45

    s "Mmmm, the whole house smells like cinnamon and pumpkin now! Delicious!"
    w "Chirp chirp! (I want a slice!)"
    return

label take_nap:
    scene bg room:
        size (1920, 1080)
    with dissolve
    
    show snoopy happy:
        zoom 1.5
        xalign 0.6
        yalign 0.75
    show woodstock happy:
        zoom 0.5
        xalign 0.38
        yalign 0.45

    s "Zzz... the sound of the autumn wind outside is perfect sleeping music... Zzz..."
    w "Zzz..."
    return
