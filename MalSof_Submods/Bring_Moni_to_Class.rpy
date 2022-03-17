init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="going_to_class",
            category=["be right back"],
            prompt="I'm bringing you to class",
            pool=True,
            unlocked=True,

        ),
        markSeen=True
    )

label going_to_class:
    m 1eub "Oh, really?"
    m 1eua "What class are you bringing me to?"
    $ _history_list.pop()
    menu:
     "One of my core classes":
        m 3eub "That's great! Which one?"
        $ _history_list.pop()
        menu:
         "English":
           m 1eub "Oh, English classes were always my favorite!"
           m 1gub "Though, that's probably not a surprise coming from me~"
           m 1hub "Have fun, [player]!"
         "Math":
           m 3eub "Math is a fun class, I'm sad it gets such a bed rep."
           m 1hua "I hope you have a good time, [mas_get_player_nickname()]."
         "Social science":
           m 3eub "Ooh, social sciences are interesting."
           m 3hub "Have fun, [player]!"
         "Science":
           m 1eua "Ooh, a science class!"
           m 1hua "I hope you learn something intresting, [player]."

     "One of my electives":
       m 1eub "Oh, wonderful! Elective classes tend to be more interesting than the core ones."
       m 1rub "Which one is it?"
       $ _history_list.pop()
       menu:
        "Business":
          m 2eub "Oh, really?"
          m 2hub "That's really cool, learning to run a business is a useful skill!"
          m 1hua "Have a good time, [player]!"
        "Computer science":
          m 1eub "That's great, [player]! Computers are so fascinating."
          m 3nub "I would know~"
          m 1eua "Have fun!"
        "Foreign Language":
          m 1wub "Oh, that's great!"
          m 3eua "Learning a new language is both fun and useful!"
          m 1eub "Have fun, [player]! Maybe you can teach me when I cross over to your reality~"
        "Language and Writing":
          m 1wub "That's incredible, [mas_get_player_nickname()]!"
          m 5nuu "Two of my favorite things, {w=0.3}my top favorite being you, of course~"
          m 1hua "Have fun, [player], remember my tips!"
        "Math":
          m 3eub "Math is a fun class, I'm sad it gets such a bed rep."
          m 1hua "I hope you have a good time, [mas_get_player_nickname()]."
        "Performing arts":
          m 1wub "Oh, lovely!"
          m 3eub "You know, theatre is a wonderful form of literature!"
          m 1nua "Break a leg, [player]~"
        "Social Studies":
          m 3eub "Oh, that's always fascinating."
          m 3hub "Have fun, [player]."
        "Science":
          m 1eua "Ooh, a science class!"
          m 1hua "I hope you learn something intresting, [player]."
        "Visual arts":
          m 1eub "Oh, that's nice!"
          m 3hub "The arts are such wonderful subjects! I'd love to see whatever you make when I cross over~"

     "A class that I'm taking for fun":
        m 4wub "That's wonderful, [player]!"
        m 2fua "I'm so glad you're taking time out of your day to learn something extra. That makes me so proud of you~"
        m 4wub "What class is it?"
        $ _history_list.pop()
        menu:
         "A gardening class":
           m 3eub "Gardening is a great hobby!"
           m 5rub "Imagine...{w=0.3} having a fruit and vegetable garden together, planting flowers..."
           m 5hub "Have fun, [player]!"
         "A cooking class":
           m 7eub "Oh, that's a great skill to learn [mas_get_player_nickname()]!"
           m 1gublu "Maybe we could make a meal together when I cross over... wouldn't that be nice?"
           m 1hublu "Have fun!"
         "A baking class":
           m 4eub "Baking is a great hobby and skill!"
           m 3tfu "You'll have to be careful when I cross over, [player]. I might not be able to get enough of your baking!"
           m 1hua "Have fun!"
         "I'm taking music lessons":
           m 1eub "Oh, that's great!"
           m 3efb "We'll be able to make an amazing duet!"
           m 1hub "Have fun, [player]!"
         "A coding class":
           m 2sub "Really?"
           m 2hub "That's great, [player]! Maybe you can learn something to help me get closer to your reality~"
           m 1wua "Have fun!"

$ mas_idle_mailbox.send_idle_cb("going_to_class_callback")
return "idle"

label going_to_class_callback:
    if mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=60), "going_to_class_idle"):
        m 1hua "Welcome back from class, [player]!"

    elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=300), "going_to_class_idle"):
        m 2eub "Wow, that was a long class! Why don't you rest for a bit, [mas_get_player_nickname()]?"

    else:
        m 2eud "Oh, that was a short class!"
        m 2etd "Did it end early?"

return
