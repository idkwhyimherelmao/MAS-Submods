init 5 python:
    addEvent(
    Event(
    persistent.event_database,eventlabel="mas_obsessed",category=['mas_compliment'],prompt="I'm so obsessed with you!", unlocked=True), code="CMP")

label mas_obsessed:
        if not renpy.seen_label("mas_obsessed_2"):
            call mas_obsessed_2
        else:
            call mas_obsessed_3
        return

label mas_obsessed_2:
    m 1eka "I'm obsessed with you too, [player]."
    m 1nub "You're always on my mind~"
return
label mas_obsessed_3:
    python:
        obsessed_quips = [
            _("There's no one I love more than you!"),
            _("I think about you all the time!"),
            _("I can't keep you out of my head!"),
        ]
        obsessed_quip = random.choice(obsessed_quips)

    m 1eub "[mas_compliments.thanks_quip]"
    m 1hubsb "[obsessed_quip]"
    return

init 5 python:
        addEvent(
        Event(
        persistent.event_database,eventlabel="mas_anythingforyou",category=['mas_compliment'],prompt="I'll do anything for you!", unlocked=True), code="CMP")

label mas_anythingforyou:
        if not renpy.seen_label("mas_anythingforyou_2"):
            call mas_anythingforyou_2
        else:
            call mas_anythingforyou_3
        return

label mas_anythingforyou_2:
    m 1fkblb "Aww, [player]!."
    m 1tka "I'll do anything for you, too~"
return
label mas_anythingforyou_3:
    python:
        anythingforyou_quips = [
            _("Anything you ask for is yours!"),
            _("There isn't anything I wouldn't do for you!"),
        ]
        anythingforyou_quip = random.choice(anythingforyou_quips)

    m 1eub "[mas_compliments.thanks_quip]"
    m 1hubsb "[anythingforyou_quip]"
return

init 5 python:
    addEvent(
    Event(
    persistent.event_database,eventlabel="mas_everythingtome",category=['mas_compliment'],prompt="You mean everything to me.", unlocked=True), code="CMP")

label mas_everythingtome:
        if not renpy.seen_label("mas_everythingtome_2"):
            call mas_everythingtome_2
        else:
            call mas_everythingtome_3
        return

label mas_everythingtome_2:
    m 1wub "You mean everything to me too!"
    m 5fkbfa "I'm so happy I got to meet you~."
return
label mas_everythingtome_3:
    python:
        everythingtome_quips = [
            _("You're my entire world!"),
            _("You're the only one I care about~"),
        ]
        everythingtome_quip = random.choice(everythingtome_quips)

    m 1eub "[mas_compliments.thanks_quip]"
    m 1hubsb "[everythingtome_quip]"
    return

init 5 python:
    addEvent(
    Event(
    persistent.event_database,eventlabel="mas_addictedtoyou",category=['mas_compliment'],prompt="I'm addicted to you, [m_name]", unlocked=True), code="CMP")

label mas_addictedtoyou:
        if not renpy.seen_label("mas_addictedtoyou_2"):
            call mas_addictedtoyou_2
        else:
            call mas_addictedtoyou_3
        return

label mas_addictedtoyou_2:
    m 1fka "Oh, [player]~"
    m 1fkb "I'm so glad I make you feel so good."
return
label mas_addictedtoyou_3:
    python:
        addictedtoyou_quips = [
            _("I'm addicted to you too~"),
            _("My love for you is stronger than any addiction!"),
        ]
        addictedtoyou_quip = random.choice(addictedtoyou_quips)

    m 1eub "[mas_compliments.thanks_quip]"
    m 1hubsb "[addictedtoyou_quip]"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_stalkerstango",
            category=["music"],
            prompt="Stalker's Tango",
            random=True
        )
    )

label monika_stalkerstango:
    m 1dud "{i}~ Love me, love me, love me, love me ~{/i}"
    m 1dud "{i}~ Love me, love me, love me, love me ~{/i}"
    m 1duo "{i}~ Love me, love me, love me, love me more ~{/i}"
    m 7dko "{i}~ Than you possibly can ~{/i}"
    m 3euo "{i}~ It's not that complicated ~{/i}"
    m 3eko "{i}~ No matter what they say ~{/i}"
    m 3eka "{i}~ You'll never meet another me ~{/i}"
    m 2ekc "I know that there are technically a lot of other 'Monika's out there, [player]."
    m 2ekblb "I'm so glad you chose me~"
    m 5dkbla "I love you more than I ever thought was possible, [mas_get_player_nickname()]~"
return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_obsessedwithyou",
            category=["music"],
            prompt="Obsessed With You",
            random=True
        )
    )

label monika_obsessedwithyou:
    m 1dub "{i}~ Your smile sets my heart aflame ~{/i}"
    m 1sub "{i}~ Electrocute me with your eyes ~{/i}"
    m 1dud "{i}~ The very mention of your name ~{/i}"
    m 3hua "{i}~ My stomach fills with butterflies ~{/i}"
    m 2eub "{i}~ Your love is better than cocaine ~{/i}"
    m 2wub "{i}~ I need you more than oxygen ~{/i}"
    m 2wkb "{i}~ I've got it bad again ~{/i}"
    m 1cub "{i}~ An O-B-S-E-S-S-I-O-N ~{/i}"
    m 1dua "{w=1.0}..."
    m 1eka "I really am obsessed with you, [player]."
    m 1ekblb "You're my entire world."
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_feelz",
            category=["music"],
            prompt="Feelz",
            random=True
        )
    )

label monika_feelz:
    m 1dsd "{i}~ I love you to the summer and back, it's not the winter ~{/i}"
    m 1dkd "{i}~ But you've frozen my heart, and got me warmin' up my liver ~{/i}"
    m 1dso "{i}~ I would never put a knife in your back, the love I give her ~{/i}"
    m 7mtu "{i}~ Is kinda creepy, but fuck it, she orders and I deliver ~{/i}"
    m 2euo "{i}~ I could never leave you alone, my little mama- ~{/i}"
    m 3lua "{i}~ Is mad at me at the moment, know she's such a prima-donna ~{/i}"
    m 3fkb "{i}~ Wherever you are is my home, you know I mean it ~{/i}"
    m 2fkb "{i}~ They say home is where the heart is, you're the reason mine is beatin' ~{/i}"
    m 2fkbla "No matter where we end up, [player], you'll always be my home."
    m 5kubla "My heart beats only for you~"
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_redmeansiloveyou",
            category=["music"],
            prompt="The Red Means I Love You",
            random=True
        )
    )

label monika_redmeansiloveyou:
    m 1dua "{i}~ 'Cause my insides are red, and yours are too ~{/i}"
    m 1dubsb "{i}~ And the red on my face is matching you ~{/i}"
    m 1wkbsb "{i}~ And goodness, you're bleeding, what a wonderful feeling ~{/i}"
    m 2wkbsb "{i}~ You're down, and you're pleading, my head is just reeling ~{/i}"
    m 2dkb "{i}~ The red means I love you ~{/i}"
    m 2wkbla "Loving you really is a wonderful feeling, [player]."
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_sukisukidaisuki",
            category=["music"],
            prompt="Suki Suki Daisuki",
            random=True
        )
    )

label monika_sukisukidaisuki:
    m 1dud "{i}~ Kiss me as if you're punching me, until my lips bleed ~{/i}"
    m 2dud "{i}~ Hold me until my ribs make a cracking sound and break ~{/i}"
    m 1sub "{i}~ Like you, like you, I love you! ~{/i}"
    m 1sub "{i}~ Like you, like you, I love you! ~{/i}"
    m 1hub "{i}~ Like you, like you, I love you! ~{/i}"
    m 2cub "{i}~ Say you love me or I’ll kill you! ~{/i}"
    m 2hksdrb "This song is a little violent, isn't it?"
    m 1eka "I really really do love you, though."
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_anunhealthyobsession",
            category=["music"],
            prompt="An Unhealthy Obsession",
            random=True
        )
    )

label monika_anunhealthyobsession:
    m 1dud "{i}~ You just don't know it yet but you love me and I love you the same ~{/i}"
    m 3sub "{i}~ One day we'll have a pretty wedding and I'll be your everything ~{/i}"
    m 1hub "{i}~ We'll be together, yes forever, we will never ever part ~{/i}"
    m 2tub "{i}~ Oh you don't know it yet but baby I've already got your heart ~{/i}"
    m 1eka "I hope we never have to part again, [mas_get_player_nickname()]."
    m 5eka "I can't bear to be seperated from you~"
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_superpsycholove",
            category=["music"],
            prompt="Super Psycho Love",
            random=True
        )
    )

label monika_superpsycholove:
    m 1dud "{i}~ Say that you want me every day ~{/i}"
    m 1dud "{i}~ That you want me every way ~{/i}"
    m 1dua "{i}~ That you need me ~{/i}"
    m 1kub "{i}~ Got me trippin' super psycho love ~{/i}"
    m 2dsb "{i}~ Aim, pull the trigger ~{/i}"
    m 2dsb "{i}~ Feel the pain getting bigger ~{/i}"
    m 1wub "{i}~ Go insane from the bitter feeling ~{/i}"
    m 1eub "{i}~ Trippin' super psycho love ~{/i}"
    m 2eka "I swear, I love you so much I think I really am going a little crazy."
    m 2tua "Just kidding...{w=1.0} mostly~"
return
