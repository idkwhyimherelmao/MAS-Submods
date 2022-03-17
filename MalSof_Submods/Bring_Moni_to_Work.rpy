init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="bring_to_work",
            category=["be right back"],
            prompt="I'm bringing you to work",
            pool=True,
            unlocked=True,

        ),
        markSeen=True
    )

label bring_to_work:
    m 1eub "Oh, really?"
    m 1eua "What kind of work are you doing?"
    $ _history_list.pop()
    menu:
     "Office work":
        m 1eub "Alright, [player]."
        m 7tfu "Just don't get in trouble for having your girlfriend with you at work!"
        m 2lkc "I'd hate for you to get repremanded by your boss."
        m 1hub "I hope you have a good day at work, [mas_get_player_nickname()]~"

     "Freelance work":
        m 1eub "That's great, [player]!"
        m 3lub "Being able to do the job you like, setting your own hours, getting to work from home sometimes..."
        m 1hua "Good luck!"

     "Voulenteer work":
        m 1wub "Oh, that's great!"
        m 1eka "It's so kind of you to voulenteer your time."
        m 3wub "When I cross over to your world, we can voulenteer together!"
        m 3hua "Have a good time, [mas_get_player_nickname()]!"


$ mas_idle_mailbox.send_idle_cb("bring_to_work_callback")
return "idle"

label bring_to_work_callback:
    if mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=60), "bring_to_work_idle"):
        m 1hua "Welcome back from work, [player]!"

    elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=300), "bring_to_work_idle"):
        m 2eub "Wow, that was long! Why don't you rest for a bit, [mas_get_player_nickname()]?"

    else:
        m 2eua "Oh, that was short!"
        m 2etb "Are you done working?"

return
