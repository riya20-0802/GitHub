define s = Character("Snoopy", color="#ff9900")

label start:
    scene bg room:
        size (1920, 1080)
    with dissolve

    show snoopy happy:
        zoom 1.5
        xalign 0.5
        yalign 0.75

    s "Hello, and welcome to my fall-themed game!"
    s "Do you want to go outside, or stay in here with me?"

    menu:
        "Go outside into the leaves.":
            jump outside

        "Stay in this cozy room.":
            jump stay

label outside:
    scene bg whitehouse with dissolve
    show snoopy happy:
        zoom 1.5
        xalign 0.5
        yalign 0.75

    s "Wow, look at all the autumn leaves! It's beautiful out here."
    return

label stay:
    scene bg room:
        size (1920, 1080)
    show snoopy happy:
        zoom 1.5
        xalign 0.5
        yalign 0.75

    s "Much better. It's so warm and cozy inside."
    return
