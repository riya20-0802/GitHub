define s = Character("Snoopy", color="#ff9900")
define w = Character("Woodstock", color="#ffff00")

label start:
    scene bg room:
        size (1920, 1080)
    with dissolve

    # Snoopy shifts slightly right from the center
    show snoopy happy:
        zoom 1.5
        xalign 0.6
        yalign 0.75
    
    s "Hello, and welcome to my fall-themed game!"
    
    # Woodstock shifts right to stay close to Snoopy
    show woodstock happy:
        zoom 0.5
        xalign 0.38
        yalign 0.45
    with dissolve

    w "Chirp chirp! (Hi there!)"
    s "Do you want to go outside, or stay in here with me?"

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

    show snoopy happy:
        zoom 1.5
        xalign 0.6
        yalign 0.75
    show woodstock happy:
        zoom 0.5
        xalign 0.38
        yalign 0.45

    s "Wow, look at all the autumn leaves! It's beautiful out here."
    w "Chirp chirp! (Let's play!)"
    s "What should we do out here in the yard?"

    menu:
        "Jump straight into a giant pile of leaves!":
            jump leaf_jump

        "Go for a peaceful autumn walk.":
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

    s "CRUNCH! That was amazing! There are leaves stuck all over my beanie now."
    w "Chirp! (That was awesome!)"
    return

label autumn_walk:
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

    s "The cool air feels so refreshing, and the trees look beautiful."
    w "Chirp chirp... (So peaceful...)"
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

    s "Much better. It's so warm and cozy inside."
    s "How should we spend our cozy afternoon?"

    menu:
        "Bake a warm pumpkin pie.":
            jump bake_pie

        "Curl up on the couch and take a nap.":
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
