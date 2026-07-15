# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

default name = "Bepis" #Bepis is the failsafe player name. Don't ask.

define p = Character(_("[name]"), color="#dbce8e")
define s = Character(_("Stacy"), color="#b535c9")
define m = Character(_("Stacy's Mom"), color="#da203f")

# Transforms for various uses such as tweening the characters or scenes.
transform sepia:
    matrixcolor TintMatrix("#d7be89")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg room
    scene black

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    "The summer of '03... The summer that changed your life forever. You thought you’d grown past it, knowing it’s been ages."

    "Like, c’mon, it’s been ten years. You are a grown ass person with bills to pay, and an empty home waiting for you."

    "It’s been hard, but you’ve surprisingly managed. You’re getting paid, and living a comfortable life."

    "What more could you ask for? Right...?"

    "You looked back at your work ID. Your eyes glaze over your name."

    $ name = renpy.input("Your name... it's:")
    $ name = name.strip()
    if name == "":
        $ name= _("Bepis")
    
    "Another tiring day of being a corporate slave. A nice can of cold beer sounds amazing to you right now. And maybe even some greasy fried food that could clog one’s arteries."

    "Just as you were about to plop down on the couch, you felt a vibration in your pocket."

    "{i}(BZZT BZZT){/i}"

    p "God please, anything but work-related matters... I CLOCKED OUT, OKAY? I just want to enjoy my beer, and watch my favorite show..."

    "With a sigh, you pull your phone out. An email."

    "Great, just great. It’s probably your workplace asking you to do more work despite clocking out already."

    "As you opened the email, what greeted you was something you least expected."

    '{i}\"Saint Ander Dingus’ Institute of Learning invites former alumni of batch 2003 to celebrate a reunion after 10 years!\"{/i}'

    "With a snort, you toss your phone somewhere on the couch and lean back in your seat."

    "You crack your beer open, and the satisfying sound of the hiss escaping the can fills your ear as relaxation slowly consumes your entire being."

    p "Yeah, no. Not going. I haven't thought about school in a {b}decade{/b}! And I do not plan on thinking about it again anytime soon."

    "As you turn your TV on to watch the thousandth episode of The Best in Jest, another buzz from your phone disrupts the peace that was slowly starting to settle."

    "{i}(BZZT BZZT){/i}"

    "With a sigh, you decide to check your phone again. Because this time, it may be related to work."

    "Oh, how {i}wrong{/i} you were."

    "Instead, what greets you is a text with a name you haven’t thought about in years."

    "{b}Stacy Collins{/b}"

    # TODO: Milo, add Stacy's Mom instrumental here.
    # play music "audio/acoustic51.mp3" fadein 3.0 volume 0.25 loop
    jump seq1a

label seq1a:
    "{i}\"Hi! Just checking, is this [name]’s number?\"{/i}"

    "{i}\"It’s Stacy! Stacy Collins. I know we haven’t seen each other in a decade, but I was wondering...\"{/i}"

    "{i}\"Are you attending the reunion?\"{/i}"

    "As you finish reading the text, you choke on your beer.\n
    Stacy Collins... You haven’t heard that name in years."

    "How the {i}fuck{/i} did she get your number?"

    menu:
        "Reply":
            jump seq1b

        "Don't Reply":
            jump seq1End

label seq1End: ## LONELY ENDING

    "You decide it wasn’t worth your time, and leave the text on read."

    "It’s not worth wasting your time mingling with people you don’t even like. Stacy? She’s better left in the past."

    "{i}Especially{/i} not after you found her mom hot."

    "You lean back in your seat and turn your show back on."

    # play music "audio/bestInJest.mp3" fadein 1.0 volume 0.1
    # Optional: Insert some Best In Jest audio here, just a snippet

    p "This... This is life."
    jump end

label seq1b:
    p "{i}stacy? yeah, its me [name]. how did you get my number?{/i}"

    s "{i}Your old buddy Robert gave me your number! I found out recently that we were co-workers in this new job I got haha.{/i}"

    s "{i}I asked him for your number because I wanted to catch up with you!{/i}"

    s "{i}It’s been 10 years after all. And with the reunion coming up, I thought it gave me a perfect chance to reach out!{/i}"

    "If you were being completely honest, it feels awkward to reconnect with Stacy."

    "{i}Especially{/i} after you found her mom hot back then."

    "You even made excuses to visit her home to \"hangout\", all because you wanted a glimpse of her mother. {i}You sick bastard...{/i}"

    "Luckily, it didn’t seem weird at the time considering you were neighbors."

    "Her mom always welcomed you with open arms, {i}literally{/i}. She’d greet you with the warmest, tightest hugs, to the point that they made your head woozy."

    jump seq2

label seq2:
    scene black

    "You remember the first time you met Stacy’s mom."

    scene bg house_outside with dissolve
    show layer master at sepia

    "It was hot out, and you recently found out you and Stacy were neighbors. She invited you over, telling you her house had a newly built pool."

    "Without thinking much about it, you headed over to chill with Stacy at her new pool."

    show mom neutral with dissolve
    show bg house_outside_blur with dissolve
    "What greeted you at the door was a stunning older woman who resembled Stacy a lot."

    "She was in her late 30s, or maybe even early 40s, and she looked great for her age. You remember your eyes almost popping out of their sockets from how wide they went."

    m "Oh! You must be [name]! Stacy told me all about you, it’s so good to finally meet you, dear!"

    "Stacy told her mom about you...? But why? It’s not like you were best friends or anything."

    "Yeah, you both hung out from time to time, but it was more of a casual \"Hey wanna eat lunch together?\" or \"Wanna partner up for this project?\" type of friendship since you both didn’t really talk to many people."

    "After meeting her mother, it’s safe to say that..."

    "{i}Stacy’s mom has got it going on.{/i}"

    m "Come in! It’s sooooo hot out today."

    m "My daughter’s in the backyard, probably already taking a dip in the new pool."

    m "Why don’t you join her? I’ll make you kids some lemonade and snacks to eat."

    "As if on instinct, you obeyed the older woman and found yourself walking towards the backyard of their house."

    scene bg garden with dissolve
    show layer master at sepia
    "..."

    "You see Stacy waving at you from outside the sliding glass door."

    "And her mom was right, she was already taking a dip in the pool. She looked so carefree, it made you want to join her in the water."

    show bg garden_blur with dissolve
    s "Hey! You made it."

    s "The water's nice, come have a dip!"

    "As she got out of the pool, you couldn’t help but stare a little."

    "She looked... {i}pretty{/i}. But your mind was so distracted by seeing her mom, so you didn’t even spare her another glance."

    p "Was that your mom...?"

    "You asked, gesturing behind you. You felt pathetic as your voice cracked while doing so."

    s "Yeah, don’t mind her. She’s a bit much. It’s why I don’t really bring friends over."

    p "Eh... It’s fine..."

    p "She’s very... {i}welcoming{/i}, that’s for sure..."

    s "You okay...? You look a bit red."

    "Feeling embarrassed, you didn’t think twice about what you were doing and-"

    "{size=70}SPLASH...!{/size}" with vpunch

    "You jumped in the pool with no hesitation, trying to cool yourself off. You didn’t want Stacy to think you were blushing or {i}something{/i}..."

    "That would’ve been embarrassing. You? Blushing over her {i}mom{/i}?"

    "You'd rather {i}drown{/i} in this pool than her finding out."

    m "I made snaaacks!~"

    "As you looked over at Stacy’s mom, you felt your head getting hazy again."

    "Stacy’s mom stood holding a tray of lemonade and snacks, but she changed out of her clothes."

    show mom bathsuit with dissolve
    "{i}She was in her bathing suit.{/i}"

    "It was nothing crazy; it was rather modest. But you felt yourself withering away like a Victorian man seeing someone’s ankles for the first time."

    "Before you knew it, you felt your vision fading as you blacked out while still in the pool."

    s "{b}[name]!!!{/b}" with vpunch

    scene black
    jump seq3

label seq3:
    "..."

    "The day of the reunion, you put your best outfit on. You didn’t want to show up to this reunion looking like a bum, so might as well dress up."



label seq7:

    jump start_minigame #label in File 'minigame_fable_2'
    # After the minigame, it will jump to "end", as specified in said file!
    # TODO: Make a dedicated function "label" for the minigame script to jump to when its done!
    # It will work by having some dedicated plot variable that it checks via else-if to know which scene to jump to!!

label end:
    # This ends the game.
    return
