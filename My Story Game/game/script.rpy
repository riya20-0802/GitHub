define s = Character("Snoopy", color="#ff9900")

label start:
    # This line loops your track perfectly in the background
    play music "audio/fall_bgm.mp3" loop

    scene bg room:
        size (1920, 1080)
    with dissolve

    show snoopy happy at truecenter:
        zoom 1.5
        yalign 0.75

    s "Hello, and welcome to my fall-themed game!"
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

    show snoopy happy at truecenter:
        zoom 1.5
        yalign 0.75

    s "Wow, look at all the autumn leaves! It's beautiful out here."
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
    show snoopy happy at truecenter:
        zoom 1.5
        yalign 0.75

    s "CRUNCH! That was amazing! There are leaves stuck all over my beanie now."
    s "Thanks for playing with me!"
    return

label autumn_walk:
    scene bg park:
        size (1920, 1080)
    with dissolve
    show snoopy happy at truecenter:
        zoom 1.5
        yalign 0.75

    s "The cool air feels so refreshing, and the trees look beautiful."
    s "Thanks for going on a walk with me!"
    return

# --- INSIDE PATH ---
label stay:
    scene bg room:
        size (1920, 1080)
    with dissolve

    show snoopy happy at truecenter:
        zoom 1.5
        yalign 0.75

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
    show snoopy happy at truecenter:
        zoom 1.5
        yalign 0.75

    s "Mmmm, the whole house smells like cinnamon and pumpkin now! Delicious!"
    s "Thanks for baking with me!"
    return

label take_nap:
    scene bg room:
        size (1920, 1080)
    with dissolve
    show snoopy happy at truecenter:
        zoom 1.5
        yalign 0.75

    s "Zzz... the sound of the autumn wind outside is perfect sleeping music... Zzz..."
    s "Thanks for relaxing with me!"
    return
