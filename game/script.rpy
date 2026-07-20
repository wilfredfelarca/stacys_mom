# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

default name = "Bepis" #Bepis is the failsafe player name. Don't ask.
default stacyLove = 0
default momLove = 0


define p = Character(_("[name]"), color="#dbce8e")
define s = Character(_("Stacy"), color="#b535c9")
define m = Character(_("Stacy's Mom"), color="#da203f")

# Transforms for various uses such as tweening the characters or scenes.

#transform sepia:
    #matrixcolor TintMatrix("#d7be89")

# A new "center" transform specifically for character sprites
transform chrCenter:
    zoom 0.5
    xcenter 0.5
    yalign 0.3

# Center the sprite 25% across the screen
transform midleft:
    zoom 0.5
    xcenter 0.25
    yalign 0.3

# Center the sprite 75% across the screen
transform midright:
    zoom 0.5
    xcenter 0.75
    yalign 0.3

init:
    # Edits the length of a transition
    $ wipeup = CropMove(0.1, "wipeup")
    $ wipeleft = CropMove(0.25, "wipeleft")

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
    
    scene bg apartment_night with dissolve:
        zoom 1.2
        xcenter 0.5
    "Another tiring day of being a corporate slave. A nice can of cold beer sounds amazing to you right now. And maybe even some greasy fried food that could clog one’s arteries."

    "Just as you were about to plop down on the couch, you felt a vibration in your pocket."

    "{i}(BZZT BZZT){/i}" with hpunch

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

    scene black with dissolve
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

    scene black with dissolve
    "Her mom always welcomed you with open arms, {i}literally{/i}. She’d greet you with the warmest, tightest hugs, to the point that they made your head woozy."

    jump seq2

label seq2:
    "You remember the first time you met Stacy’s mom."

    scene bg house_outside with dissolve
    #show layer master at sepia

    "It was hot out, and you recently found out you and Stacy were neighbors. She invited you over, telling you her house had a newly built pool."

    "Without thinking much about it, you headed over to chill with Stacy at her new pool."

    show bg house_outside_blur with dissolve
    show mom happy_c at chrCenter with dissolve
    "What greeted you at the door was a stunning older woman who resembled Stacy a lot."

    "She was in her late 30s, or maybe even early 40s, and she looked great for her age. You remember your eyes almost popping out of their sockets from how wide they went."
    
    show mom talk_c at chrCenter with dissolve
    m "Oh! You must be [name]! Stacy told me all about you, it’s so good to finally meet you, dear!"

    "Stacy told her mom about you...? But why? It’s not like you were best friends or anything."

    "Yeah, you both hung out from time to time, but it was more of a casual \"Hey wanna eat lunch together?\" or \"Wanna partner up for this project?\" type of friendship since you both didn’t really talk to many people."

    "After meeting her mother, it’s safe to say that..."

    "{i}Stacy’s mom has got it going on.{/i}"

    show mom talk_a at chrCenter with dissolve
    m "Come in! It’s sooooo hot out today."

    m "My daughter’s in the backyard, probably already taking a dip in the new pool."

    show mom happy_c at chrCenter with dissolve
    m "Why don’t you join her? I’ll make you kids some lemonade and snacks to eat."

    "As if on instinct, you obeyed the older woman and found yourself walking towards the backyard of their house."

    scene bg garden with dissolve
    #show layer master at sepia
    "..."

    "You see Stacy waving at you from outside the sliding glass door."

    "And her mom was right, she was already taking a dip in the pool. She looked so carefree, it made you want to join her in the water."

    show bg garden_blur with dissolve
    show stacy sw_c at chrCenter with dissolve
    s "Hey! You made it."

    s "The water's nice, come have a dip!"

    "As she got out of the pool, you couldn’t help but stare a little."

    "She looked... {i}pretty{/i}. But your mind was so distracted by seeing her mom, so you didn’t even spare her another glance."

    p "Was that your mom...?"

    "You asked, gesturing behind you. You felt pathetic as your voice cracked while doing so."

    show stacy sw_b at chrCenter with dissolve
    s "Yeah, don’t mind her. She’s a bit much. It’s why I don’t really bring friends over."

    p "Eh... It’s fine..."

    p "She’s very... {i}welcoming{/i}, that’s for sure..."

    show stacy sw_a at chrCenter with dissolve
    s "You okay...? You look a bit red."

    "Feeling embarrassed, you didn’t think twice about what you were doing and-"

    scene bg underwater with wipeup
    "{size=70}SPLASH...!{/size}" with vpunch

    "You jumped in the pool with no hesitation, trying to cool yourself off. You didn’t want Stacy to think you were blushing or {i}something{/i}..."

    "That would’ve been embarrassing. You? Blushing over her {i}mom{/i}?"

    "You'd rather {i}drown{/i} in this pool than her finding out."

    m "I made snaaacks!~"

    "As you looked over at Stacy’s mom, you felt your head getting hazy again."

    "Stacy’s mom stood holding a tray of lemonade and snacks, but she changed out of her clothes."

    scene bg garden_blur with dissolve
    show stacy sw_a at midleft with dissolve
    show mom sw_c at midright with dissolve
    "{i}She was in her bathing suit.{/i}"

    "It was nothing crazy; it was rather modest. But you felt yourself withering away like a Victorian man seeing someone’s ankles for the first time."

    scene bg underwater with dissolve
    "Before you knew it, you felt your vision fading as you blacked out while still in the pool."

    s "{b}[name]!!!{/b}" with vpunch

    scene black with dissolve
    jump seq3

label seq3:
    "..."

    scene bg apartment with dissolve:
        zoom 1.2
        xcenter 0.5
    "The day of the reunion, you put your best outfit on. You didn’t want to show up to this reunion looking like a bum, so might as well dress up."

    "As you got ready, you heard your phone buzz."

    "{i}(BZZT BZZT){/i}"

    "It was Stacy."

    s "{i}Hi! What time are you arriving for the reunion?{/i}"

    menu:
        "Reply":
            $ stacyLove += 1
            $ renpy.notify("Stacy bond up!")
            p "{i}hey! ill be there at around 5:30 pm. i dont really want to be the first person to arrive haha,,{/i}"

            p "{i}what about you?{/i}"

            s "{i}I’ll arrive at around the same time as you then! I don’t really know who I’d hang around with if I arrived before you lol.{/i}"

            p "{i}alrightyy, ill see u later then?{/i}"

            s "{i}See you! xx{/i}"

        "Leave her on read":
            "Better not get distracted... You need to make sure you look decent for this silly reunion."

    "By the time you finished getting ready, you took one last glance at the mirror."

    "That’s good enough... You at least look put together."

    "It was now 5:01 pm, and thankfully your old college was relatively close to your place. Give or take 15 minutes without traffic and 20-something minutes with."

    scene black with wipeleft
    "..."

    scene bg schoolpark_sunset with wipeleft
    "Here you are again..."

    "{b}{i}Saint Ander Dingus’ Institute of Learning.{/i}{/b}"

    "It was almost 6 pm by the time you arrived. You hadn’t anticipated traffic to hold you off that much, but at least you made it."

    "You stand outside the main hall where the reunion was happening. You can hear the music blasting, as well as lively chatter from your other batchmates inside."

    "It almost makes you want to turn back and leave."

    "Maybe coming here was a mistake, what were you thinking?"

    "Maybe you’re just afraid to face the people you went to college with and see that they’re living better lives than you."

    "As you feel the urge to leave getting stronger, you see someone exit the building."

    "It was Stacy and she looked... upset."

    "The moment she saw you, her eyes lit up."

    show bg schoolpark_sunset_blur with dissolve
    show stacy neutral_b at chrCenter with dissolve
    s "[name], you made it...!"

    "There you stood, face-to-face with someone you haven’t seen in a decade. You couldn’t help but feel the nostalgia kicking in."

    "It’s like being back in college, except this time you’re both grown-ups now."

    "You look at Stacy, and you can’t help but notice that she looks more like her mom now that she’s grown older."

    hide stacy with dissolve
    "She goes in for a hug, and you freeze on the spot, not knowing what to do." with hpunch

    show stacy sad_c at chrCenter with dissolve
    s "This reunion sucks... Do you want to get out of here?"

    "She murmurs as she clings to you. You don’t know what happened at the reunion, but all the more reason to get out of here."

    "Right...?"

    p "Hey, what happened in there?"

    show stacy sad_b at chrCenter with dissolve
    s "My ex came up to me, and he’s married to the girl he cheated on me with..."

    show bg schoolpark_sunset
    hide stacy with dissolve
    "Before you could offer to take her someplace else, you see a luxurious sports car pull up towards you both."

    "Inside the car, you see none other than Stacy’s mom herself."

    "{b}And she {i}still{/i} has it going on...!{/b}"

    show bg schoolpark_sunset_blur
    show mom sad_c at chrCenter with dissolve
    m "I got your text, are you okay sweetie...?"

    "You didn’t think it was possible, but Stacy’s mom got even hotter. She was probably in her early 50’s by now, and she looked {i}great{/i}."

    show mom talk_e at chrCenter with dissolve
    "When she noticed you, she lowered her sunglasses and looked you up and down with a mix of curiosity and surprise in her eyes."

    m "[name]... is that you?"

    "You felt your ears getting red as you scrambled for your words, and it just made Stacy and her mom giggle."

    show mom talk_e at midright with dissolve
    show stacy neutral_a at midleft with dissolve
    s "Wanna get out of here?"

    "You find yourself nodding at the offer, and you almost feel embarrassed at how eager you are." with vpunch

    "But to be honest? You’d rather catch up with these two gorgeous ladies than having to sit through a reunion where everybody pretends to like each other."

    "When in reality, they probably used this reunion as an excuse to show off and feel better about themselves."
    scene black with dissolve
    jump seq4

label seq4:
    scene bg diner with dissolve
    "It was 6:43 pm, and in a diner, you sat with both Stacy and her mother."

    "This was the last thing you expected to do on a random Saturday evening. But here you were, sitting awkwardly, and across from you was your old college classmate and her hot mom."

    "As if things couldn’t get more awkward, Stacy suddenly had to step out for a moment because of a work call."

    show bg diner_blur with dissolve
    show mom neutral with dissolve
    "So now it was just you and her mom. The same mom you had a thing for back when you were 20."

    m "So... how's work?"

    p "It's alright, Ms. Collins-"

    show mom wink with dissolve
    m "Please, just call me Debbie. All these years had passed, and you still call me Ms. Collins."

    "She teased you about it, because it was true. Even back then, she asked you to call her Debbie, but you just stuck to calling her \"Ms. Collins\" or \"ma’am\"."

    "You didn’t think it would be appropriate to be on a first-name basis with your friend’s mom."

    p "I shouldn’t-\nIt doesn’t feel right to call you by that, ma’am..."
    
    show mom neutral with dissolve
    m "Please, I insist. You make me feel {i}older{/i} when you use those terms."

    menu:
        "Keep your mouth shut":
            "You sit there awkwardly, waiting for Stacy to come back."
            
            "Because in all honesty? You wanted to get out of this situation."

            "It was getting awkward quick, and you didn’t know what to do or say in front of Stacy’s mom."

        "Compliment her":
            $ momLove += 1
            $ renpy.notify("Stacy's mom bond up!")
            p "There's nothing wrong with being older..."

            p "Besides, you look {i}amazing{/i} for your age, ma’am."

            show mom happy with dissolve
            "Stacy's mom beams as she fiddled with a piece of her hair."

            m "You really think so, sweetie?"

            m "If I didn’t know you, I’d think you were flirting with me."

    hide mom with dissolve
    "You felt your face go hot as you avoided eye contact with Stacy's mom."

    "The menu has never looked more interesting than now."

    show stacy neutral at midleft with dissolve
    show mom neutral at midright with dissolve
    "Eventually, Stacy returned from her phone call, sitting back down whilst noticing the awkward air between you and her mother."

    s "So, [name], Robert told me you worked at Nexus Corp. How is it?"

    "Ah yes, Nexus Corp. How else could you describe it? It’s like every other tech company out there."

    "Working for a corporation isn’t really fun, but at least it’s steady, and you live a comfortable life because of it."

    p "Eh, you know... typical corporate stuff. It’s alright... Keeps things steady for me at least."

    show stacy sad at midleft with dissolve
    s "I feel you... My previous job was like that. That's why I moved."

    show mom happy at midright with dissolve
    m "You both make me feel young. It reminds me of the time I used to work in a law firm."

    show stacy neutral at midleft with dissolve
    s "You were always so busy, but you always made time for me. Thanks for that, mom."

    "Stacy’s mom was admirable. You remember when you’d visit her back then. Her mom was a hard worker, yet she always had time for Stacy."

    "You couldn’t imagine how hard it was. Being a single mother was no joke, but Stacy’s mom made it look so effortless. You had to give her credit for that, at least."
    
    scene black with dissolve
    jump seq5

label seq5:
    "(sequence 5 wip)"

label seq6:
    "(sequence 6 wip)"

label seq7:

    jump start_minigame #label in File 'minigame_fable_2'
    # After the minigame, it will jump to "end", as specified in said file!
    # TODO: Make a dedicated function "label" for the minigame script to jump to when its done!
    # It will work by having some dedicated plot variable that it checks via else-if to know which scene to jump to!!

label end:
    # This ends the game.
    return
