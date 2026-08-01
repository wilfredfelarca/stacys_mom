# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

default name = "Dayyo" #Dayyo is the failsafe player name. Don't ask.
default stacyLove = 0
default momLove = 0

# Sequence 7 variables

default seen_photos = False
default seen_journal = False

define p = Character(_("[name]"), color="#53907e")
define s = Character(_("Stacy"), color="#b535c9")
define m = Character(_("Stacy's Mom"), color="#da203f")
define mx = Character(_("Debbie"), color="#da203f")
define c = Character(_("Creep"), color="#905d00")
define y = Character(_("Mr. Yoshida"), color="#5b5b5b")
define d = Character(_("???"), color="#175fa1")

### Transforms for various uses such as tweening the characters or scenes.

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

# Shakes the character once
transform oneShake:
    linear 0.03 xoffset -24
    linear 0.03 xoffset 36
    linear 0.03 xoffset 12
    linear 0.03 xoffset -18
    linear 0.03 xoffset 0

# Animates the character shaking
transform shaking:
    linear 0.1 xoffset -2
    linear 0.1 xoffset 3
    linear 0.1 xoffset 2
    linear 0.1 xoffset -3
    linear 0.1 xoffset 0
    repeat

# Animates the character stretching vertically for a brief moment
transform bounce:
    parallel:
        yoffset 0.5
        linear 0.1 yoffset 0.52
        linear 0.1 yoffset 0.48
        linear 0.1 yoffset 0.5
    parallel:
        linear 0.05 yzoom 1.1
        linear 0.1 yzoom 1

# Paces character back and forth in a loop
transform backandforth:
    linear 1 xoffset -150
    pause 1.2
    xzoom -1.0
    pause 0.5
    linear 2 xoffset 200
    pause 1.2
    xzoom 1.0
    pause 0.5
    linear 2 xoffset -200
    pause 1.2
    xzoom -1.0
    pause 0.5
    linear 2 xoffset 200
    pause 1.2
    xzoom 1.0
    pause 0.5
    repeat

transform backandforthFinish:
    linear 0.7 xoffset 0
    xzoom 1.0
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

    "The summer of '03... The summer that changed your life forever. You thought you'd grown past it, knowing it's been ages."

    "Like, c'mon, it's been ten years. You are a grown ass person with bills to pay, and an empty home waiting for you."

    "It's been hard, but you've surprisingly managed. You're getting paid, and living a comfortable life."

    "What more could you ask for? Right...?"

    "You looked back at your work ID. Your eyes glaze over your name."

    $ name = renpy.input("Your name... it's:")
    $ name = name.strip()
    if name == "":
        $ name= _("Dayyo")
    
    scene bg apartment_night with dissolve:
        zoom 1.2
        xcenter 0.5
    "Another tiring day of being a corporate slave. A nice can of cold beer sounds amazing to you right now. And maybe even some greasy fried food that could clog one's arteries."

    "Just as you were about to plop down on the couch, you felt a vibration in your pocket."

    "{i}(BZZT BZZT){/i}" with hpunch

    p "God please, anything but work-related matters... I CLOCKED OUT, OKAY? I just want to enjoy my beer, and watch my favorite show..."

    "With a sigh, you pull your phone out. An email."

    "Great, just great. It's probably your workplace asking you to do more work despite clocking out already."

    "As you opened the email, what greeted you was something you least expected."

    '{i}\"Saint Ander Dingus\' Institute of Learning invites former alumni of batch 2003 to celebrate a reunion after 10 years!\"{/i}'

    "With a snort, you toss your phone somewhere on the couch and lean back in your seat."

    "You crack your beer open, and the satisfying sound of the hiss escaping the can fills your ear as relaxation slowly consumes your entire being."

    p "Yeah, no. Not going. I haven't thought about school in a {b}decade{/b}! And I do not plan on thinking about it again anytime soon."

    "As you turn your TV on to watch the thousandth episode of The Best in Jest, another buzz from your phone disrupts the peace that was slowly starting to settle."

    "{i}(BZZT BZZT){/i}"

    "With a sigh, you decide to check your phone again. Because this time, it may be related to work."

    "Oh, how {i}wrong{/i} you were."

    "Instead, what greets you is a text with a name you haven't thought about in years."

    "{b}Stacy Collins{/b}"

    # TODO: Milo, add Stacy's Mom instrumental here.
    # play music "audio/acoustic51.mp3" fadein 3.0 volume 0.25 loop
    jump seq1a

label seq1a:
    "{i}\"Hi! Just checking, is this [name]'s number?\"{/i}"

    "{i}\"It's Stacy! Stacy Collins. I know we haven't seen each other in a decade, but I was wondering...\"{/i}"

    "{i}\"Are you attending the reunion?\"{/i}"

    "As you finish reading the text, you choke on your beer.\n
    Stacy Collins... You haven't heard that name in years."

    "How the {i}fuck{/i} did she get your number?"

    menu:
        "Reply":
            jump seq1b

        "Don't Reply":
            jump seq1End

label seq1End: ## LONELY ENDING

    "You decide it wasn't worth your time, and leave the text on read."

    "It's not worth wasting your time mingling with people you don't even like. Stacy? She's better left in the past."

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

    s "{i}It's been 10 years after all. And with the reunion coming up, I thought it gave me a perfect chance to reach out!{/i}"

    "If you were being completely honest, it feels awkward to reconnect with Stacy."

    "{i}Especially{/i} after you found her mom hot back then."

    "You even made excuses to visit her home to \"hangout\", all because you wanted a glimpse of her mother. {i}You sick bastard...{/i}"

    "Luckily, it didn't seem weird at the time considering you were neighbors."

    scene black with dissolve
    "Her mom always welcomed you with open arms, {i}literally{/i}. She'd greet you with the warmest, tightest hugs, to the point that they made your head woozy."

    jump seq2

label seq2:
    "You remember the first time you met Stacy's mom."

    scene bg house_outside with dissolve
    #show layer master at sepia

    "It was hot out, and you recently found out you and Stacy were neighbors. She invited you over, telling you her house had a newly built pool."

    "Without thinking much about it, you headed over to chill with Stacy at her new pool."

    show bg house_outside_blur with dissolve
    show mom happy_c at chrCenter with dissolve
    "What greeted you at the door was a stunning older woman who resembled Stacy a lot."

    "She was in her late 30s, or maybe even early 40s, and she looked great for her age. You remember your eyes almost popping out of their sockets from how wide they went."
    
    show mom talk_c at chrCenter with dissolve
    m "Oh! You must be [name]! Stacy told me all about you, it's so good to finally meet you, dear!"

    "Stacy told her mom about you...? But why? It's not like you were best friends or anything."

    "Yeah, sure, you both hung out from time to time..."
    
    "But it was more of a casual \"Hey wanna eat lunch together?\" or \"Wanna partner up for this project?\" type of friendship since you both didn't really talk to many people."

    "After meeting her mother, it's safe to say that..."

    "{i}Stacy's mom has got it going on.{/i}"

    show mom talk_a at chrCenter with dissolve
    m "Come in! It's sooooo hot out today."

    m "My daughter's in the backyard, probably already taking a dip in the new pool."

    show mom happy_c at chrCenter with dissolve
    m "Why don't you join her? I'll make you kids some lemonade and snacks to eat."

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

    "As she got out of the pool, you couldn't help but stare a little."

    "She looked... {i}pretty{/i}. But your mind was so distracted by seeing her mom, so you didn't even spare her another glance."

    p "Was that your mom...?"

    "You asked, gesturing behind you. You felt pathetic as your voice cracked while doing so."

    show stacy sw_b at chrCenter with dissolve
    s "Yeah, don't mind her. She's a bit much. It's why I don't really bring friends over."

    p "Eh... It's fine..."

    p "She's very... {i}welcoming{/i}, that's for sure..."

    show stacy sw_a at chrCenter with dissolve
    s "You okay...? You look a bit red."

    "Feeling embarrassed, you didn't think twice about what you were doing and-"

    scene bg underwater with wipeup
    "{size=70}SPLASH...!{/size}" with vpunch

    "You jumped in the pool with no hesitation, trying to cool yourself off. You didn't want Stacy to think you were blushing or {i}something{/i}..."

    "That would've been embarrassing. You? Blushing over her {i}mom{/i}?"

    "You'd rather {i}drown{/i} in this pool than her finding out."

    m "I made snaaacks!~"

    "As you looked over at Stacy's mom, you felt your head getting hazy again."

    "Stacy's mom stood holding a tray of lemonade and snacks, but she changed out of her clothes."

    scene bg garden_blur with dissolve
    show stacy sw_a at midleft with dissolve
    show mom sw_c at midright with dissolve
    "{i}She was in her bathing suit.{/i}"

    "It was nothing crazy; it was rather modest. But you felt yourself withering away like a Victorian man seeing someone's ankles for the first time."

    scene bg underwater with dissolve
    "Before you knew it, you felt your vision fading as you blacked out while still in the pool."

    s "{b}[name]!!!{/b}" with vpunch

    scene black with dissolve
    jump seq3

label seq3: ## REUNION - STACY BOND
    "..."

    scene bg apartment with dissolve:
        zoom 1.2
        xcenter 0.5
    "The day of the reunion, you put your best outfit on. You didn't want to show up to this reunion looking like a bum, so might as well dress up."

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

            s "{i}I'll arrive at around the same time as you then! I don't really know who I'd hang around with if I arrived before you lol.{/i}"

            p "{i}alrightyy, ill see u later then?{/i}"

            s "{i}See you! xx{/i}"

        "Leave her on read":
            "Better not get distracted... You need to make sure you look decent for this silly reunion."

    "By the time you finished getting ready, you took one last glance at the mirror."

    "That's good enough... You at least look put together."

    "It was now 5:01 pm, and thankfully your old college was relatively close to your place. Give or take 15 minutes without traffic and 20-something minutes with."

    scene black with wipeleft
    "..."

    scene bg schoolpark_sunset with wipeleft
    "Here you are again..."

    "{b}{i}Saint Ander Dingus' Institute of Learning.{/i}{/b}"

    "It was almost 6 pm by the time you arrived. You hadn't anticipated traffic to hold you off that much, but at least you made it."

    "You stand outside the main hall where the reunion was happening. You can hear the music blasting, as well as lively chatter from your other batchmates inside."

    "It almost makes you want to turn back and leave."

    "Maybe coming here was a mistake, what were you thinking?"

    "Maybe you're just afraid to face the people you went to college with and see that they're living better lives than you."

    "As you feel the urge to leave getting stronger, you see someone exit the building."

    "It was Stacy and she looked... upset."

    "The moment she saw you, her eyes lit up."

    show bg schoolpark_sunset_blur with dissolve
    show stacy neutral_b at chrCenter with dissolve
    s "[name], you made it...!"

    "There you stood, face-to-face with someone you haven't seen in a decade. You couldn't help but feel the nostalgia kicking in."

    "It's like being back in college, except this time you're both grown-ups now."

    "You look at Stacy, and you can't help but notice that she looks more like her mom now that she's grown older."

    hide stacy with dissolve
    "She goes in for a hug, and you freeze on the spot, not knowing what to do." with hpunch

    show stacy sad_c at chrCenter with dissolve
    s "This reunion sucks... Do you want to get out of here?"

    "She murmurs as she clings to you. You don't know what happened at the reunion, but all the more reason to get out of here."

    "Right...?"

    p "Hey, what happened in there?"

    show stacy sad_b at chrCenter with dissolve
    s "My ex came up to me, and he's married to the girl he cheated on me with..."

    show bg schoolpark_sunset
    hide stacy with dissolve
    "Before you could offer to take her someplace else, you see a luxurious sports car pull up towards you both."

    "Inside the car, you see none other than Stacy's mom herself."

    "{b}And she {i}still{/i} has it going on...!{/b}"

    show bg schoolpark_sunset_blur
    show mom sad_c at chrCenter with dissolve
    m "I got your text, are you okay sweetie...?"

    "You didn't think it was possible, but Stacy's mom got even hotter. She was probably in her early 50's by now, and she looked {i}great{/i}."

    show mom talk_e at chrCenter with dissolve
    "When she noticed you, she lowered her sunglasses and looked you up and down with a mix of curiosity and surprise in her eyes."

    m "[name]... is that you?"

    "You felt your ears getting red as you scrambled for your words, and it just made Stacy and her mom giggle."

    show mom talk_e at midright with easeoutright
    show stacy neutral_a at midleft with dissolve
    s "Wanna get out of here?"

    "You find yourself nodding at the offer, and you almost feel embarrassed at how eager you are." with vpunch

    "But to be honest? You'd rather catch up with these two gorgeous ladies than having to sit through a reunion where everybody pretends to like each other."

    "When in reality, they probably used this reunion as an excuse to show off and feel better about themselves."
    scene black with dissolve
    jump seq4

label seq4: ## DINER - MOM BOND
    scene bg diner with dissolve
    "It was 6:43 pm, and in a diner, you sat with both Stacy and her mother."

    "This was the last thing you expected to do on a random Saturday evening. But here you were, sitting awkwardly, and across from you was your old college classmate and her hot mom."

    "As if things couldn't get more awkward, Stacy suddenly had to step out for a moment because of a work call."

    show bg diner_blur with dissolve
    "So now it was just you and her mom. The same mom you had a thing for back when you were 20."

    show mom talk_a at chrCenter with dissolve
    m "So... how's work?"

    p "It's alright, Ms. Collins-"

    show mom wink at chrCenter with dissolve
    m "Please, just call me Debbie. All these years had passed, and you still call me Ms. Collins."

    "She teased you about it, because it was true. Even back then, she asked you to call her Debbie, but you just stuck to calling her \"Ms. Collins\" or \"ma'am\"."

    "You didn't think it would be appropriate to be on a first-name basis with your friend's mom."

    p "I shouldn't-\nIt doesn't feel right to call you by that, ma'am..."
    
    show mom wink_talk at chrCenter with dissolve
    m "Please, I insist. You make me feel {i}older{/i} when you use those terms."

    menu:
        "Keep your mouth shut":
            "You sit there awkwardly, waiting for Stacy to come back."
            
            "Because in all honesty? You wanted to get out of this situation."

            "It was getting awkward quick, and you didn't know what to do or say in front of Stacy's mom."

        "Compliment her":
            $ momLove += 1
            $ renpy.notify("Stacy's mom bond up!")
            p "There's nothing wrong with being older..."

            p "Besides, you look {i}amazing{/i} for your age, ma'am."

            show mom talk_b with dissolve
            "Stacy's mom beams as she fiddled with a piece of her hair."

            m "You really think so, sweetie?"

            m "If I didn't know you, I'd think you were flirting with me."

    hide mom with dissolve
    "You felt your face go hot as you avoided eye contact with Stacy's mom."

    "The menu has never looked more interesting than now."

    "Eventually, Stacy returned from her phone call, sitting back down whilst noticing the awkward air between you and her mother."

    show mom talk_a at midright with dissolve
    show stacy neutral_c at midleft with dissolve
    s "So, [name], Robert told me you worked at Nexus Corp. How is it?"

    "Ah yes, Nexus Corp. How else could you describe it? It's like every other tech company out there."

    "Working for a corporation isn't really fun, but at least it's steady, and you live a comfortable life because of it."

    p "Eh, you know... typical corporate stuff. It's alright... Keeps things steady for me at least."

    show stacy neutral_b at midleft with dissolve
    s "I feel you... My previous job was like that. That's why I moved."

    show mom happy_c at midright with dissolve
    m "You kids make me feel so young. This reminds me of the time I used to work in a law firm!"

    show stacy angry_c at bounce, midleft
    s "Oh please, mom. It's not the same when you own the law firm {i}yourself{/i}."

    show stacy neutral_c at midleft with dissolve
    s "You were always so busy, but you always made time for me...\nThanks for that, mom."

    "Stacy's mom was admirable. You remember when you'd visit their home back then. Her mom was always there, welcoming you with open arms and prepping food for you two."

    "You couldn't imagine how hard it was. Being a single mother was no joke, and running your own law firm?"
    
    "Stacy's mom made it look so effortless, and it's a lot easier to appreciate that now that you've grown up yourself."
    
    scene black with dissolve
    jump seq5start

label seq5start: ## MALL - BRANCH
    "It's been a couple of days since you've reunited with both Stacy and her mom."
    
    "If you were gonna be honest, both women have been plaguing your mind lately."

    scene bg mall with dissolve
    "To keep your mind off them, you decided to head to your local mall."

    "You heard that a new comic book store has opened, so you decided to drop by and check it out."

    "{i}Oof-!{/i}" with vpunch

    show bg mall_blur with dissolve
    show stacy neutral_a at chrCenter with dissolve
    "What you didn't expect was to bump into Stacy at the mall. Did she live nearby? Why is she suddenly showing up everywhere recently?"

    p "Stacy?"

    show stacy neutral_c at chrCenter with dissolve
    s "Oh...! [name]!"

    s "I didn't expect to bump into you here. Do you come here often?"

    p "Yeah, I live around here actually."

    show stacy happy_c at chrCenter with dissolve
    s "Really? I just moved around this area for work!"

    s "Guess we'll be seeing each other more, huh?"

    "Amazing."

    "This is what you get for choosing to live relatively close to your old college. You never know who you'll run into out here."

    "Like that one time you bumped into that professor who grilled your research paper alive on a random Tuesday while waiting for the bus..."

    "Awkward was an understatement, but hey, at least he didn't seem to remember your pathetic ass."

    p "So... what brings you here?"

    show stacy neutral_b at chrCenter with dissolve
    s "Oh, I grabbed some lunch and wanted to watch a movie.\nWhat about you?"

    p "Oh, uh, comic book store."

    p "I heard a new one that just opened, so I decided to drop by and check it out."

    p "What movie are you watching?"

    show stacy happy_b at chrCenter with dissolve
    s "I'm watching {i}The Conjuring{/i}!"

    s "I'm about to buy tickets right now actually-"

    show stacy neutral_a at bounce, chrCenter
    "Before Stacy could finish her sentence, you see her fish her phone out of her pocket.\nIt was ringing, and you couldn't help but wonder who's calling her."

    hide stacy with dissolve
    s "Mom? Yes, what do you need?"

    show bg mall with dissolve
    "You wait for her to finish the call with her mom, thinking it would just be a quick call to check on Stacy."

    "As Stacy put the phone down, you see her look a bit conflicted."

    show bg mall_blur with dissolve
    show stacy neutral_b at chrCenter with dissolve
    s "My mom called to see if I was free today."

    s "Apparently a grocery store near her place has some good promo. Marked-down prices for fresh meat at like 4-ish pm?"

    show stacy happy_c at chrCenter with dissolve
    s "You know how mom is, always eager for good deals haha..."

    s "But yeah, she was thinking of inviting me over for a meal after the grocery run. But I'm not really sure I can make it on time."

    show stacy neutral_c at chrCenter with dissolve
    s "Since, you know... I'm about to go see a movie..."

    "You don't know if this was your imagination, but it seemed that Stacy was hinting at inviting you to go see the movie with her."

    "But at the same time, maybe subbing in to help her mom with the groceries would give you a chance to get closer with Stacy's mom... And a free meal doesn't sound too bad."

    menu:
        "Watch a movie with Stacy":
            jump seq5stacy

        "Accompany Stacy's mom with grocery shopping":
            jump seq5mom

label seq5stacy: ## CINEMA - STACY BOND
    show stacy neutral_b at chrCenter with dissolve
    p "I mean... You're already here and about to buy a ticket."

    p "You already went through the trouble to get here; I know Ms. Collins would understand."

    show stacy neutral_a at chrCenter with dissolve
    "She still looked hesitant, and you couldn't help but wonder why. Then she dropped the question."

    show stacy happy_b at chrCenter with dissolve
    s "Would you... want to watch the movie with me?"

    p "Uh... s-sure!"

    "You did something you didn't expect you'd do. You're not really a fan of horror movies, so you don't know what possessed you to watch The Conjuring with Stacy."

    scene black with dissolve
    "..."

    scene bg cinema with dissolve
    "Inside the movie theater, you've never felt more anxious than ever."

    "You usually don't mind the dark and cold atmosphere inside. But now that you're watching a horror movie? It feels creepier than usual inside."

    "You glance over at Stacy to see how she's faring while watching the movie."

    show bg cinema_blur with dissolve
    show stacy scared_d at chrCenter with dissolve
    "She also didn't seem immune to the ambience with the way she was grabbing onto the bucket of popcorn in her lap."

    "As you try to focus on the movie, you feel tension creeping up; a telltale sign that a jumpscare was about to happen."

    menu:
        "Offer your arm to Stacy":
            $ stacyLove += 1
            $ renpy.notify("Stacy bond up!")
            "Stacy looks at you with a grateful expression as she takes hold of your arm."

            show stacy scared_c at shaking, chrCenter
            "{size=70}{i}BOO!!{/i}{/size}" with vpunch

            show stacy scared_a at shaking, chrCenter with dissolve
            "As the jumpscare happened, you felt Stacy holding on to you tighter as she hid her face in your shoulder."

            "You also felt your heart drop as the cheap jumpscare appeared on the screen, but having Stacy cling to you helped."
            
            p "You okay...?"

            show stacy scared_d at shaking, chrCenter with dissolve
            "Stacy nodded, and the poor woman was shaking slightly in her seat."

            "Though, the look on her face tells that she might not last another scare..."

            scene black with wipeleft
            "Feeling bad for Stacy, you offered to leave mid-screening. You knew staying here any longer wouldn't be good for her."

        "Tug your hood over your head":
            "Sensing a jumpscare about to happen, you tug your hood over your head as you avert your eyes from the screen."

            "Again, you don't do well with horror. It's not a surprise you're cowering away behind your hood."

            show stacy scared_b at shaking, chrCenter
            s "{size=70}{i}KYAAAAAAAHHHHH!!!{/i}{/size}" with vpunch

            "You didn't expect the jumpscare to scare Stacy so badly, to the point she jolted in her seat and spilled popcorn everywhere."
            
            show stacy scared_d at bounce
            hide stacy with moveoutleft
            show bg cinema with dissolve
            "Stacy felt embarrassed about screaming and making a mess, quickly leaving the movie theater."

            scene black with wipeleft
            "Not wanting to be alone and feeling bad for her, you decided to follow after her."

    scene bg mall_blur with wipeleft
    show stacy scared_d at chrCenter with dissolve
    s "I'm sorry we didn't get to finish the film..."

    p "It's fine... Are you okay?"

    "She nodded, but you could still tell she was shaken up from the film."

    show stacy neutral_a at chrCenter with dissolve
    s "Thank you though, for coming to watch it with me."

    s "It's been a while since I saw a movie."

    show stacy happy_c at chrCenter with dissolve
    s "Even though we didn't get to finish it, it was nice hanging out."

    s "Just like the old times..."

    "{i}Just like the old times...{/i}"

    scene black with dissolve
    jump seq6start

label seq5mom: ## GROCERIES - MOM BOND
    p "Uhm... I could accompany her."

    show stacy neutral_c at chrCenter with dissolve
    s "Huh?"

    p "Your mom... I could accompany her so you can see the movie."

    show stacy neutral_b at chrCenter with dissolve
    s "But--"

    p "It's okay, I'm not busy. And besides, I'm due for some groceries anyway."

    "Stacy sighed as she nodded. You couldn't help but wonder if this was just your imagination, but she looked somewhat disappointed."

    scene bg mall with dissolve
    "She fished her phone out to call her mom, letting her know you'll accompany her on the grocery run."

    scene black with dissolve
    "..."

    scene bg city with dissolve
    "You arrive at the familiar grocery store where your family used to shop at. You haven't been here in years, especially not after your family moved out of the neighborhood."

    show bg city_blur with dissolve
    show mom talk_c at chrCenter with dissolve
    m "There you are, [name]!"

    show mom talk_d at bounce, chrCenter
    m "I can't lie, I was surprised when Stacy called to tell me that you're accompanying me for this."

    p "Oh, yeah- I bumped into her at a local mall in our city."

    p "I figured I'd accompany you because I was due for some groceries anyway, haha..."

    show mom talk_f at chrCenter with dissolve
    m "That makes sense... but in a different city? Won't that be a hassle to bring back?"

    p "Not at all...! We're in neighboring cities anyway."

    m "Alright then..."

    show mom talk_b at chrCenter with dissolve
    m "But don't be a stranger, sweetie. I really don't mind if you want a ride back. Just say the word."

    "You nod your head sheepishly, embarrassed at the idea of being driven back home like a child." with vpunch

    show mom wink_talk at chrCenter with dissolve
    m "Before you go though, at least let me make you a nice home-cooked meal after our grocery run?"

    "You sigh and give her another nod. Besides, the free meal is what you came for anyway."

    "And because you may or may not have wanted a chance to get closer with Stacy's mom. {i}You sneaky bastard.{/i}"
    
    hide mom with dissolve
    scene black with wiperight
    scene bg shop with wiperight
    "The two of you walk side by side inside the grocery store."

    "As you check your watch, you realize it's almost 4 pm."

    show bg shop_blur with dissolve
    show mom talk_d at chrCenter with dissolve
    p "Uh... guess we should head to the frozen section then? It's almost time for the sale."

    show mom happy_c at bounce, chrCenter
    m "Oh, right! Wouldn't want to miss out on those sweet deals~!"

    hide mom with dissolve
    "As you arrive at the frozen meat section, you see some staff already marking down prices for the various cuts of fresh meat."

    show meat with dissolve:
        xalign 0.5
        yalign 0.5
    "You arrived just in time! You take a browse around the different freezers."

    "But... to be honest? You didn't cook much, so you had no idea which cuts of meat could work for which dish."

    hide meat with dissolve
    show mom talk_d at midright with dissolve
    show creep speaking_a at midleft with dissolve
    "You look over at Stacy's mom to see what she's buying, only to notice a random dude checking her out inappropriately."

    menu:
        "Confront the stranger":
            "As the stranger approaches Stacy's mom, you feel a sudden spark of bravery rise within you."

            "Was it bravery, or stupidity?"

            "You're not certain, but you don't know what possessed you to come up to this six-foot-tall man who clearly towered over you."

            show creep speaking_c with dissolve
            c "Hey, gorgeous. You here by yourself?"

            show mom sad_a with dissolve
            "Stacy's mom turned to look at the man, and she looked uncomfortable at the unwanted attention."

            "Before she could respond, you stood in between her and the creep."

            $ momLove += 1
            $ renpy.notify("Stacy's mom bond up!")
            p "She's with me, dude."

            show creep speaking_a with dissolve
            c "Ha! And who are you supposed to be? Her little lap dog?"

            "You felt your blood boiling as this man ridiculed you, but you decided to stand your ground and try to make this guy go away."

            show creep speaking_b at chrCenter with easeoutright
            c "Say, you and me, how about we should ditch this loser and have some fun elsewhere..."

            show mom sad_b with dissolve
            m "I-I'm good, no thank you."

            "Like a lot of shitty men, this creep didn't back down even after Stacy's mom already said no."

            p "You heard the lady, a no's a no."

            show creep angry with dissolve
            c "Dude, get out the fucking way. I'm not talking to you."

            "The creep shoved you aside, but you didn't back down like a loser. You shoved him back, which was the biggest mistake ever." with hpunch

            "One thing led to another until eventually-" with vpunch

            $ renpy.with_statement(vpunch)
            pause 0.25
            $ renpy.with_statement(hpunch)
            pause 0.25

            scene black with vpunch
            "{size=70}{b}THWACK!!{/b}{/size}"

            "Before you knew it, your vision faded to black. The last thing you saw was Stacy's mom panicking as she ran to your side."
            
        "Try to stay out of it":
            "Like a coward, you decide to stay out of it. Especially since this man was about six feet tall and towered over you."

            show creep speaking_c at bounce, chrCenter with easeoutright
            "You see him approach Stacy's mom and invade her personal space by standing too close for comfort."

            "You didn't want to completely abandon her, so you stand behind a nearby freezer to eavesdrop on them both."

            c "Hey, gorgeous. You here by yourself?"

            show mom sad_a with dissolve
            m "Uhm... No, I'm with a friend."
            
            show creep speaking_a with dissolve
            c "Oh? I don't see them anywhere though."

            show creep speaking_b with dissolve
            c "Say, you and me, how about we should ditch this place and have some fun elsewhere..."

            m "I'm good... I don't really want to..."

            show mom sad_b with dissolve
            "Stacy's mom looked uncomfortable, and she noticed you standing behind one of the nearby freezers."

            "She kept anxiously looking towards you, compelling you to eventually come out of your hiding spot to at least try to get this creep off her back."

            p "Hey man... Uh, I don't think she wants to, haha..."

            show creep shocked with dissolve
            c "And {i}who{/i} are you?"

            p "Uh- Her daughter's old friend...?"

            show creep angry at bounce
            "The creep stared at you with a raised eyebrow, and shoved you aside like you were nothing." with hpunch

            "Feeling helpless, you look around to see what you could do to keep this creep away from bothering Stacy's mom."

            show milk with dissolve:
                xalign 0.25
                yalign 0.8
            "And there you spot it: a row of milk bottles at the nearby dairy section."

            show milk with easeoutright:
                xalign 0.5
                yalign 1.0

            show milk with easeoutright:
                xalign 0.5
                yalign -3.0
            hide milk
            show creep shocked
            "Without thinking, you panicked and tossed one at the guy." with hpunch

            show creep angry at oneShake, chrCenter
            "You didn't really know what to expect when you threw it. But upon hitting the creep, the milk bottle spilled open and drenched the guy."

            "Luckily, it doesn't shatter but the guy looked pissed off, and next thing you know you see his fist flying at you."

            scene black with vpunch
            "{size=70}{b}THWACK!!{/b}{/size}"

            "Your vision fades to black as you feel your body hit the ground."

    "..."

    scene bg living with dissolve
    "After the incident, you find yourself sitting in the familiar home you kept frequenting during the summer of '03."

    "The Collins residence, a.k.a Stacy's home before she moved out on her own."

    show bg living_blur with dissolve
    show mom sad_c at chrCenter with dissolve
    "Stacy's mom kept fussing over you as she held an ice pack over the fresh black eye on the right side of your face."

    m "Oh god... This looks... {i}awful...{/i}"

    m "I'm sorry you got punched because of me, sweetie..."

    p "I-It's fine, Ms. Collins..."

    p "That guy was being a creep anyway... and a nuisance."

    p "I was being reckless, I'm sorry for worrying you."

    show mom happy_a with dissolve
    "Stacy's mom looked at you with such kindness in her eyes. To make you feel better, she got to work on preparing that home cooked meal she promised."

    hide mom with dissolve
    show food with dissolve:
        xalign 0.5
        yalign 0.4
        zoom 1.75
    "In the end, it was worth the wait. Despite the throbbing pain on the right side of your face, you got to enjoy a delicious home-cooked meal."

    "{i}And{/i} you got to spend time with Stacy's mom, so a win is a win!"

    scene black with dissolve
    jump seq6start

label seq6start: ## BAKERY - BRANCH
    "Ever since that day, you've been getting more chances to hang out with Stacy and her mom."

    scene bg park_blur with dissolve
    show stacy happy_c at chrCenter with dissolve
    "Just the other day, you and Stacy went out for a jog at the park. It was a nice change of scenery instead of being cooped up at home all day."

    scene bg kitchen_blur with dissolve
    show mom talk_a at chrCenter with dissolve
    "And not only that, but you also got to spend some time with her mom. She was experimenting with her cooking and called you over to test some apple pie she baked."

    show bg skyclear with dissolve
    show mom talk_a at midright with easeoutright
    show stacy happy_c at midleft with dissolve
    "Either way, both times spent with women were pleasant. Pleasant to the point it's made you look forward to the next time you get to hang out with either of them."

    scene black with dissolve
    "But in life, it's not always sunshine and rainbows. God, you wish. You still have bills to pay, and work to worry about."

    "You're fortunate enough to have a stable job that sustains you well. But sometimes you get swamped with work to the point you arrive home and just collapse in bed."
    
    "Sometimes you forget how draining it is to work in a corporation."

    "But you chose this life, so there's not much you could do. It's all you've known this past few years, and it's what keeps you afloat."

    scene bg city with dissolve
    "You check your watch and for once, you got to leave work early! You don't know what possessed you to lock in and finish your work this fast, but at least you're free!"

    "To celebrate, you decided to pass by a nearby bakery to treat yourself to a sweet treat."

    scene bg bakery_outside with dissolve
    "{i}\"Buy a dozen, get a dozen free!\"{/i}"

    "You stare at the promo poster pasted on the bakery's window."

    "{i}\"Celebrate Little Patisserie's 1st birthday with this week-long sale!\"{/i}"

    "I guess it's your lucky day today, seeing how the sale just started and you were able to get off work to catch it."

    "You didn't want to pass this opportunity up; a sale is a sale after all... And you'd take any opportunity to save some money and get a bargain."

    "But do you {i}really{/i} need two dozen pastries...? On one hand, it would be nice to stock up on pastries to indulge in. But you're just one person."

    "You don't know how long it'd take you to eat through 24 pastries, and it'd be a waste if they went bad before you could fully enjoy them all..."

    "...!\nAn idea went off in your head like a light bulb."

    scene bg bakery_inside with dissolve
    "You head inside and decide to participate in the ongoing promo."

    show package with easeinbottom:
        xalign 0.5
        yalign 0.5
    "You pick up a bunch of pastries that you think would taste good. From croissants to donuts, you soon walk out with two boxes of pastries."

    "This could be the perfect opportunity to spend some more time with Stacy {i}or{/i} her mom."

    menu:
        "Bring a box to Stacy":
            hide package with dissolve
            jump seq6stacy

        "Bring a box to Stacy's mom":
            hide package with dissolve
            jump seq6mom

label seq6stacy: ## OFFICE - STACY BOND
    "As you've made your mind up, you pull your phone out and shoot Stacy a text."

    p "{i}hey, are you free rn?{/i}"

    s "{i}Not really, sorry [name]...{/i}"

    s "{i}I'm stuck at work and my team's pretty stressed about this project we're handling because of some issues we encountered.{/i}"

    p "{i}oh, im sorry to hear that.. is there anything i can do to help?{/i}"

    s "{i}It's okay [name], you don't have to go through the trouble.{/i}"

    scene bg bakery_inside with dissolve:
        zoom 1.7
        xalign 0.5
        yalign 0.8
    show package with dissolve:
        xalign 0.5
        yalign 0.75
        zoom 1.25
    "You gaze at the spare box of pastries in your free hand."

    p "{i}i have some spare pastries w me, if you'd like..?{/i}"

    p "{i}idk, maybe it could help cheer up everybody's spirits{/i}"

    s "{i}Really? Are you sure? You don't have to, I'd feel bad...{/i}"

    p "{i}please, i insist! itd be a good lil break for all of you too.{/i}"

    scene bg city with dissolve
    "Stacy sent you the address of her office, and it's actually pretty near the bakery! It's a five-minute walk, and you make your way there easily."

    scene black with wipeleft
    "You enter the building and take the elevator to the 8th floor where Stacy's at, box of pastries in hand."

    "{i}DING!{/i}"

    scene bg meeting with wiperight
    
    "The elevator door opens, and you see Stacy in a conference room along with five other people. They all looked exhausted."

    "You knock on the door gently and wave at Stacy through the window."

    "Her expression lights up the moment she sees you, and she immediately meets you at the door."

    show bg meeting_blur with dissolve
    show stacy happy_a at chrCenter with dissolve
    show package with easeinbottom:
        xalign 0.7
        yalign 0.75
        zoom 0.8
    s "[name]! Thank you so much for these, you're the sweetest..."

    "Stacy's co-workers saw that you brought some pastries over, and their expressions also lit up."

    hide package with easeoutbottom
    "You set the box of baked goods on the table, and each of Stacy's co-workers thanked you as they each took one."

    "Bringing over some baked goods seemed to lift everyone's spirits up. Before you left, Stacy pulled you aside to talk to you privately."

    show stacy happy_c with dissolve
    s "Hey, I just wanted to thank you again for coming."

    s "You didn't have to do all this, you know?"

    $ stacyLove += 1
    $ renpy.notify("Stacy bond up!")
    show stacy happy_b at bounce
    s "But I-- no, {i}we{/i} appreciate it so much."

    p "I'm glad I was able to brighten up everyone's spirits, even if it's just a little bit."

    "Stacy had a look of pure gratitude in her eyes, and the next thing she did caught you off-guard."

    hide stacy with dissolve
    "You were pulled into a sudden hug, and for some reason, you felt your heart do a flip. You didn't want to just stand there awkwardly, so you reciprocated the gesture." with hpunch

    show stacy happy_c at chrCenter with dissolve
    "When the hug broke, you couldn't help but feel a bit disappointed. You're not sure why you feel this way, but you do."

    "You gave her one last tiny wave as you left to go home."

    scene black with dissolve
    "Sure, this wasn't a full-on hangout, but at least you got to see Stacy today! You hoped your little act of kindness left a good impression on her."

    "Safe to say you're looking forward to the next time you'll spend some time with Stacy."

    jump seq7a

label seq6mom: ## HOUSE - MOM BOND
    "As you've made your mind up, you pull your phone out and shoot Stacy's mom a text."

    "You don't know how you've reached the point in your life where you have your friend's mom's phone number in your contacts, but you do. Own up to it."

    p "{i}ms collins, are you free right now?{/i}"

    m "{i}Hi, sweetie! You messaged just in time!{/i}"

    m "{i}I'm hosting a dinner party in a bit, I'm just doing prep at the moment.{/i}"

    m "{i}Why don't you come over?{/i}"

    "A dinner party? I guess this is the perfect time to spend some time together with Stacy's mom. But you somehow feel shy at the thought of being surrounded by other people older than you."

    "And besides, she might be busy with prepping for the dinner party right now. What if you burden her?"

    p "{i}is it really okay?{/i}"

    p "{i}would it be okay if i at least helped you with prepping?{/i}"

    m "{i}Please, I insist you come, [name]!{/i}"

    m "{i}You know you're always welcome here, right?{/i}"

    show bg bakery_inside with dissolve:
        zoom 1.7
        xalign 0.5
        yalign 0.8
    show package with easeinbottom:
        xalign 0.5
        yalign 0.75
        zoom 1.25
    "You looked down sheepishly at the box of pastries in your free hand, and decided: {i}it's now or never.{/i}"

    scene black with wipeleft
    "You take a bus ride to the Collins residence, and the ride feels bumpier than usual. You hold on tight to the boxes of pastries, just so that they won't get messed up or jostled too much."

    scene bg house_outside with wipeleft
    "Eventually, you arrive in the familiar neighborhood. You stand outside the familiar house, feeling nervous as you ring the doorbell."

    m "Cooooming!~"

    "You hear Stacy's mom call from inside the house. She answers the door with the most genuine smile on her face. She always knew how to make you feel welcome at her home."

    show bg house_outside_blur with dissolve
    show mom talk_a at chrCenter with dissolve
    m "I'm so glad you made it, dear!"

    m "Come in!"

    "You smile sheepishly at the older woman. She notices the box of pastries you held in one hand and tilts her head curiously."
    
    show mom talk_b with dissolve
    m "Ooooh, what'd you bring, sweetie?"

    p "Oh, this...? They're pastries from Little Patisserie."

    show mom happy_c at bounce
    "Stacy's mom beamed, her eyes shining with excitement."

    m "Little Patisserie! I love that bakery~!"

    p "R-Really? I'm glad then..."

    p "I got a variety in these boxes; hopefully they'd be enough for everyone later."

    m "That's perfect, [name]. Thank you for bringing them over!"

    scene bg living with dissolve
    "You helped Stacy's mom with prepping for the dinner party before the guests arrived. You had to admit, you had a nice time with her."

    "As the guests poured in, you felt your social anxiety acting up. You knew there was gonna be a group, but you didn't expect this much..."

    "The dinner party went on and you kept to yourself the entire time, not wanting to embarrass yourself in front of these other older people."

    "Slowly but surely, people started to leave until it was just you and Stacy's mom."

    "You offered to stay with her and help clean up."

    scene bg living_blur with dissolve
    show mom talk_c at chrCenter with dissolve
    m "How was dinner, [name]? Did you enjoy the new dishes I made?"
    
    "You smile and nod at Stacy's mom sheepishly as you wipe down her dining table."

    p "The food was amazing, Ms. Collins... Your cooking never disappoints."

    show mom happy_a with dissolve
    "Stacy's mom returns the smile, and you don't know if it was your imagination, but she also looked a bit sheepish."

    "Awkward silence filled the air as both of you cleaned up, with Stacy's mom washing the dishes, and you clearing out the table."

    show mom talk_f with dissolve
    m "[name]?"

    p "Yes, ma'am....?"

    $ momLove += 1
    $ renpy.notify("Stacy's mom bond up!")
    show mom talk_b with dissolve
    m "{i}Thank you.{/i} For always helping out when you can."

    m "And enjoying my cooking..."

    show mom talk_a with dissolve
    m "Ever since Stacy moved out, I've been trying to adjust to the quiet space... I appreciate when you go out of your way to spend time with me."

    "You feel your ears heating up, flustered at how genuine Stacy's mother was."

    p "I-It's my pleasure, ma'am."

    show mom wink_talk with dissolve
    m "I still do hope you drop the formalities though... Just call me Debbie, sweetheart."

    "She teases you again and giggles as she watches you avoid eye contact."

    scene black with dissolve
    "Despite feeling socially anxious, you'd say you had a nice time today!"
    
    "The food was great, and you got a bit of alone time with Stacy's mother as you helped her prep for the dinner party and clean afterwards."

    "Safe to say you're looking forward to the next time you'll spend some time with Stacy's mom."

    jump seq7a

label seq7a:
    scene bg apartment with dissolve:
        zoom 1.2
        xcenter 0.5
    "At this point in your life, getting a message from either Stacy or her mom no longer surprised you. You check your phone as you feel it vibrate in your pocket."

    "{i}(BZZT BZZT){/i}"

    s "{i}Hey, are you free today? Wanna come over?{/i}"

    p "{i}sure. to do what exactly?{/i}"

    s "{i}Summon a demon.{/i}"

    "...???"

    s "{i}Just kidding LOL. My mom needs help with her computer, but she's in a rush to leave for some yoga class right now.{/i}"

    s "{i}I don't really know how to deal with it, but since you're pretty good at computers, I figured you could help?{/i}"

    s "{i}I'm also dog-sitting for her right now, and I figured we could have a movie marathon after you deal with her computer.{/i}"

    s "{i}How does that sound?{/i}"

    p "{i}sure, why the hell not? i have the day off work anyway.{/i}"

    scene black with wipeleft
    "..."

    scene bg house_outside with wipeleft
    "As you rung the doorbell of the familiar doorstep, you see Stacy's mom."

    show bg house_outside_blur with dissolve
    show mom sad_b at chrCenter with dissolve
    m "[name]! Thank heavens, you're here."

    m "I assume Stacy's told you about my computer?"

    p "Uhh... Yeah, she did. What's exactly the issue with it?"

    show mom sad_a with dissolve
    m "I'm not really sure, but it's gotten so slow ever since I downloaded some \"virus cleaner\" I saw online."

    p "Virus cleaner-?"

    m "Yeah... Anyways, I'll catch you later, okay?"

    show mom talk_e with dissolve
    m "Just ask Stacy to lead you to my computer. I have a yoga class to attend."

    scene bg hallway with dissolve
    "As Stacy's mom left, you made your way inside the house. What greets you is a stubby, short-legged dog barking happily."

    s "Porkchop! Come here, boy!" with hpunch

    "You see Stacy chasing after the dog with a bag of treats in her hand."

    scene bg hallway_blur with dissolve
    show stacy neutral_b at chrCenter with dissolve
    s "Oh, hey! You made it. The computer's upstairs in the master bedroom."

    s "I'll start making us snacks while you work on the computer. Just come back down when you're done."

    scene bg bedroom with wipeleft
    "As you made your way to the master bedroom, you couldn't help but feel like you're intruding. So you hurry and find the computer to get it over with."

    show popups with hpunch
    "Upon opening the computer, you were blasted with back to back pop-ups of random programs launching at startup."

    p "Holy malware...!"

    p "Let's see... How would I fix this?"

    hide popups with dissolve
    "After clicking around for' what felt like forever, you managed to rid the PC of malware."

    "You take a deep breath and lean back in your seat."

    show bg bedroom with dissolve:
        zoom 1.7
        xalign 0.5
        yalign 1.0
    "You look around, and notice a small wooden chest under the bed."

    "You don't know what's gotten into you, but you decided to snoop around and see what the chest contained."

    "As expected, it was locked. Any normal person would see this and leave the locked container alone, but you are one nosy bastard."

    "After looking around, you spot some bobby pins on the vanity and decide to use it to try and get to the wooden chest."

    jump start_minigame #label in File 'minigame_fable_2'
    # After the minigame, it will jump to "seq7b", as specified in said file!

label seq7b:
    p "Aha! Opened!" with vpunch

    "You don't know what to expect inside the chest, but hopefully it's nothing scandalous."

    "As you peer inside, you find a journal and a couple of photo albums."

    jump seq7menu

label seq7menu:
    menu:
        "Pick up the photo album" if not seen_photos:
            $ seen_photos = True

            scene bg bedroom_blur with dissolve:
                zoom 1.7
                xalign 0.5
                yalign 1.0
            "As you pick the photo album up, you flip it open."

            "Inside, there are photos of a young Stacy and her mom. Her mom looked so much like her when she was younger, and Stacy was an adorable kid."

            "The more you flip through the album, the more you get to see memories of a young Stacy growing up, along with photos of her mom."

            "You can't help but notice the amount of love put into this album. Every page had a little note that Stacy's mom wrote about each photographed moment."

            "From little moments like Stacy's first time at a theme park, or her photo from her first day of high school. You can tell that this photo album was made with love and care."

            "As you reach the last page of the album, you notice a missing photo with a little note written:"

            "{i}\"May 19th, 1985. The day I first held Stacy in my arms.\"{/i}"

            "You double check around the photo album, and you find a hidden compartment. Inside was a folded polaroid, which you assume is the missing photo."

            "In the photo was Stacy's mom holding a newborn Stacy. Next to her was a handsome man who looked to be Stacy's father."

            "But knowing Stacy, you knew her father wasn't present in her life, so seeing him in this photo was a bit of a surprise."

            scene bg bedroom with dissolve:
                zoom 1.7
                xalign 0.5
                yalign 1.0

            jump seq7menu

        "Pick up the the journal" if not seen_journal:
            $ seen_journal = True
            "As you pick up the leather journal, you can tell it's been well loved."

            "You flip it open and you see pages upon pages filled with writing. You obviously didn't have time to read all of them. Because if you did, you'd be here all day."

            "One section of the journal stuck out to you as you feel an envelope stuck between two pages."

            "You see something written on the envelope."

            "{i}\"To my dearest Stacy\"{/i}"

            "It's a letter addressed to Stacy. You wanted to snoop and read what was inside... But you didn't want to rip it open, especially since the envelope was sealed shut."

            "You turn your attention to the pages the letter was sandwiched between."

            "They were two different entries, written a day apart."

            scene black with dissolve

            centered "{i}October 24, 1985{/i}"

            centered "{i}Steve told me he doesn't love me anymore. I honestly don't know what to do anymore.\nOur daughter is barely a year old, and the idea of raising her alone... It's terrifying.{/i}"

            centered "{i}I don't know what prompted him to say this. I thought our marriage was going along fine, but I guess I thought wrong. I did my best to be the best wife...{/i}"

            centered "{i}Was I not enough?{/i}"

            centered "..."

            centered "{i}October 26, 1985{/i}"

            centered "{i}Steve has started to pack his belongings. He's also barely coming home now...\nI guess I know why he's been coming home late from work these past few months.{/i}"

            centered "{i}I'm wondering, has he found someone else?{/i}"

            centered "{i}Either way, I have to stay strong for me and Stacy.\nIf I have to raise her by myself, so be it. I don't need a man to provide a good life for my daughter.{/i}"

            centered "{i}I don't know when I'll be ready to tell Stacy about her father.\nIn the meantime, I've written this letter that I'll give her whenever I'm ready to.{/i}"

            centered "{i}I know she deserves to know the truth, but... not right now.\nI don't want her to experience heartbreak this early in her life.\nWhat would I even tell her? That her father didn't want her?\n\nThe idea is just too cruel to tell.{/i}"

            centered "{i}For as long as I can, I'll protect her.\nBut I know I can't keep this from her forever.{/i}"

            centered "{i}My Stacy, the light of my life. I'm sorry it had to be this way, but I promise to love you and be there for you the best I can.{/i}"

            scene bg bedroom with dissolve:
                zoom 1.7
                xalign 0.5
                yalign 1.0

            jump seq7menu

        "Leave":
            jump seq7c

label seq7c:
    "After going through the contents of the box, a wave of guilt washes over you."

    "You snooped around the belongings of people who trusted you enough to let you in their home. Not to mention your snooping has led you to find out vulnerable information you're not supposed to."

    "With a sigh, you put everything back where you found it."

    "Panic rises when you hear Stacy calling out for you downstairs." with vpunch

    s "[name]? You done yet? Is the computer issue that bad?"

    "You didn't want her to catch you meddling with her mother's belongings, so you scramble to lock the chest with the bobby pins you used before she catches you in the act."

    scene bg bedroom with vpunch:
        xalign 0.5
        yalign 0.5
        zoom 1.1
    "With a stroke of luck, you manage to lock the chest and put everything back together. You scramble to sit in front of the desk so it looks like you were still working on her mom's computer."

    show bg bedroom_blur with dissolve
    show stacy neutral_b at chrCenter with dissolve
    s "How's the computer?"

    p "I-It's alright, haha..."

    p "It was infested with malware, but I was able to track down the main threats without having to wipe her computer..."

    p "It should be alright now."

    show stacy happy_b at bounce
    s "Great! I just finished baking us some brownies and cooking up some popcorn. I've set the TV up downstairs, so our movie marathon should be good to go!"

    "Phew... Almost caught. You don't know how you would've explained yourself if Stacy had caught you in the act of snooping through her mother's personal belongings."
    
    scene black with dissolve
    "You follow her downstairs and you both enjoy a lazy afternoon of binge watching shitty romcoms."

    "But in the back of your mind, the contents that chest lingers. Your view of both women has been put in a different light, now knowing what both have been through."

    "..."

    jump seq8

label seq8: ## FINAL BRANCH
    scene bg office with dissolve
    "It's been a week since you last saw Stacy or her mom. You've been busier than ever at work, and you just yearn for a break."

    "{color=#76915e}Co-worker{/color}" "Hey, [name], would it be okay if you also handled this report? I'm lagging behind on some, and I could really use the extra help."

    p "Again? Are you serious, man?"

    p "Fine, but this is the last time. I'm swamped with other shit I have to worry about."

    "{color=#76915e}Co-worker{/color}" "Thank you!! I'll make it up to you, I promise."

    "You wave your co-worker off as you get back to the pile of paperwork on your desk. You don't know why you took the extra work when you already have so much on your plate."

    "You'd been working yourself like a dog this past week, and you've never felt more dead inside. As you go through the pile of paperwork, you hear a gentle knock to your desk."

    "It's your boss' assistant."

    "{color=#54416e}Assistant{/color}" "Mr. Yoshida's asking for you."

    "You don't know why, but being called up in your boss' office hits you with anxiety. You started overthinking your work performance, afraid that you're about to lose this job."

    p "U-Uh, sure. I'll head over now."

    scene black with wiperight

    "As you make your way to your boss' office, you feel beads of sweat form at your forehead."

    "{i}Is this it? Are you about to get fired?{/i}"

    "{i}Are you about to lose the only reason you get up everyday?{/i}"

    "As sad as it sounds, it is true... These past few years, this job of yours is the only thing pushing you to wake up everyday. No matter how much you're sick of it, it's still something you've grown used to."

    "Standing outside the door to your boss' office, you brace yourself for bad news. You knock gently, and hear him tell you to come in."

    y "[name]! Come in, come in."

    scene bg boss_office with wiperight
    "You enter nervously, but to your surprise, your boss seems to be in a good mood. Which was {i}extremely{/i} rare..."

    p "You called for me, sir...?"

    show bg boss_office_blur with dissolve
    show boss at chrCenter with dissolve:
        yalign 0.1
    y "I have good news for you."

    show boss at backandforth:
        yalign 0.1
    y "Remember that project proposal you presented a month ago?"

    "At the mention of good news, you felt relief flood your wellbeing. You straighten up as he mentioned your project proposal."

    "Truth be told, you almost forgot about that proposal. You spent countless nights preparing for it, but the reaction you got the day you presented it made you think it wasn't a hit with your boss."

    "You didn't mind though. Even if you spent so much time on it, you really weren't that passionate about the project. So the possible rejection didn't sting as much as you expected."

    p "The one for developing an app that offers easy food delivery? What about it, sir?"

    y "I took the most promising proposals from our branch and brought them over to the higher ups."

    y "Yours was the only one approved."

    "You felt your eyes widen at the revelation."

    show boss at backandforthFinish:
        yalign 0.1
    y "Not only that, they {i}loved{/i} the idea."

    p "They did...?"

    y "Very much so, they even want to give you a promotion as lead project head."

    y "But the catch is, you will be moving to a different city to start work on this project."

    "Feeling overwhelmed with the sudden barrage of good news, you stood there frozen. You didn't have time to process everything immediately."

    p "Can... Can I think about this for a moment, sir?"

    show boss at bounce:
        yalign 0.1
    y "Think? What more can you think of? If I were you, I'd immediately take the offer!"

    p "I really am grateful for this once in a lifetime opportunity, but..."

    p "This is a big change, is it possible for me to request some time to think about it?"

    show boss at bounce, chrCenter:
        xzoom -1.0
        yalign 0.1
    y "Fine, but don't keep the higher ups waiting for too long."

    y "I'll give you until the end of the week to decide."

    p "T-Thank you, Mr. Yoshida...!"

    scene black with dissolve

    "As you left work, you felt a rollercoaster of emotions. On one hand, you were grateful you got this once in a lifetime opportunity."

    "But at the same time... {i}is it really worth it...?{/i}"

    "You weren't passionate about that project at all, and if you took this opportunity, there's a high chance you wouldn't even be happy working on it. Let alone {i}leading{/i} it."

    scene bg park_night with dissolve

    "You find yourself walking along the park, deep in thought."

    "You zone out, and you find yourself thinking about the two women who've added light to your life as of late."

    scene bg schoolpark_sunset_blur with dissolve
    show stacy happy_c at chrCenter with dissolve
    "{b}{i}Stacy...{/i}{/b}"

    scene bg house_outside_blur with dissolve
    show mom happy_a at chrCenter with dissolve
    "{b}{i}Her mom, Debbie...{/i}{/b}"

    scene bg nightsky with dissolve
    "You don't want to admit it, but the idea of losing touch with them scares you. You're scared that your life would return to how it usually was."

    "Bleak...\nBoring..."
    
    "{i}Lonely...{/i}"

    show stacy happy_c at midleft with easeinbottom
    show mom happy_a at midright with easeinbottom
    "But one of them had begun to shine in your heart. You truly treasure the times you've spent with both, your heart can deny it no longer; one of them has truly won your heart."

    "And it was..."
    menu:
        "Stacy":
            if stacyLove >= 3:
                jump stacyEnd
            else:
                jump badEnd

        "Stacy's mom":
            if momLove >= 3:
                jump momEnd
            else:
                jump badEnd

label badEnd:
    "It would be..."
    hide stacy with dissolve

    "It..."
    hide mom with dissolve
    pause(1.0)
    
    scene black with dissolve
    "..."

    "A few months passed by since you reconnected with both Stacy and her mom."

    "You decided to not confess to the one that caught your heart. It pained you to do so, but it's for the best."

    "{i}You weren't brave nor strong enough to. You're a coward, that's what you are.{/i}"

    "Despite being surrounded by beautiful women who were excited to reconnect with you, nothing really happened after all of that."

    "Until eventually, your worst fear happened. Distance grew once more between you and the mother-daughter duo."

    "Ever since you got promoted, you've been busier than ever with work. Not to mention you had to relocate to a different city for your job."

    "And the rare chance you did get some free time, you'd rather use it to laze around at home watching tv and drinking beer."

    "Perhaps it's some sort of \"skill issue\" on your end. Or maybe you were dumb enough to miss the signs thrown your way."

    scene bg bar with dissolve
    "Feeling lonelier than ever, you decide to switch it up for once and drag your feet to a local bar near your new place. Way to spend your time off work I guess."

    "{color=#874b1e}Bartender{/color}" "What will it be for you tonight?"

    p "I don't know... Something strong I guess? I just want to get wasted, man. Go ham."

    "The bartender nods at you and turns around to start whipping something up."

    "When he was done, he slid it over trying to act all cool like those bartenders in shows and movies."

    "Almost like salt on a fresh wound, the drink tips over and spills all over you." with vpunch

    p "WHAT THE FUCK, MAN?"

    p "COULDN'T YOU HAVE JUST GIVEN ME MY DRINK LIKE A NORMAL PERSON?"

    "{color=#874b1e}Bartender{/color}" "I am SO sorry! Let me get you something for that--"

    "As the bartender tries to move behind the counter to grab you a rag to dry yourself off with, he slips on some banana peel like he came out straight from a cartoon."

    "{color=#874b1e}Bartender{/color}" "GAAAAAHHH! My ass...!" with vpunch

    p "You {i}cannot{/i} be serious..."

    "You feel a headache coming up after witnessing this looney tunes type of situation. Until you feel a firm tap on your back."

    d "Rough night? Here, let me help you with that."

    "You look over to see an older gentleman handing you his handkerchief. His voice caught your attention, with how smooth and silky it was. The type of voice you could listen to all night if you had to."

    show bg bar_blur with dissolve
    show dad talk_a at midleft with easeinleft
    "Not to mention, this man looked gorgeous. A \"silver fox\" as one could call him."

    p "T-Thanks..."

    show dad talk_a at chrCenter with easeinbottom
    d "So... What brings you here? Surely somebody as attractive as you can snag someone to drink with. But it seems you're alone."

    p "Yeah, about that... I don't know. I guess I just wanted to drink my sorrows away."

    p "I just recently reconnected with an old friend and her mom."

    p "Maybe I expected something more, but nothing worked out. And now I'm in a new city, feeling as lonely as ever."

    show dad talk_b with dissolve
    d "That's life for you, bud. Though, I'm a bit confused, are you also close to this person's mom? Why is she part of the conversation?"

    p "Look man, I don't feel like talking about it."

    p "But trust me, {i}Stacy's mom had it going on.{/i}"

    show dad talk_a at bounce
    d "Stacy? That name takes me back..."

    p "It does? Why...?"

    d "I had a daughter-- Well, I don't think it's fair I call her that."

    show dad talk_b with dissolve
    d "I was barely in her life anyways..."

    "As you take a closer look at this man, you notice that he looked oddly familiar. You couldn't pinpoint what it was about him, but the more he talked, the more you were able to put the pieces together."

    d "Yeah, I don't even know how I managed to get with her mother."

    show dad talk_c with dissolve
    d "That woman looked like she walked straight out a magazine."

    "All of this sounded like a coincidence... Surely, it cannot be the same people..."

    "Right...?"

    hide dad with dissolve
    show dadcg with easeinbottom
    "Little did you know, the man you were sitting with at the bar was Stacy's dad himself."

    "The same deadbeat who walked out on his wife and newborn kid."

    "You were ashamed to admit it, but honestly?"

    "{b}{i}Stacy's dad is actually pretty bad...{/i}{/b}\n{size=20}(pls get better standards.){/size}"

    jump end

label stacyEnd:
    hide mom with easeoutright
    show stacy happy_c at chrCenter with easeinleft
    "All this time you've known Stacy, you only saw her as a friend. It was always her mom you had a crush on."

    "But that is not the case anymore."

    scene bg park_night with dissolve
    "You reach for your phone and dial Stacy's number."

    "She answers almost immediately, which makes your heart pound louder in your ears."

    s "{i}Hello? [name], did you need something?{/i}"

    p "Stacy, please meet me at Seashell Coast!"

    s "{i}H-Huh...? Why? The sun hasn't come up yet.{/i}"

    p "Please... this is {i}really{/i} important..."

    "You can feel Stacy's hesitation through the phone call, but she sighs as she agrees to meet you at the local beach in your city."

    scene black with wipeleft
    "The moment the call ended, you ran straight from the park with one place in mind:"

    scene bg beach_night with wipeleft
    "{i}Seashell Coast.{/i}"

    "You thought this would be the perfect place to confess your love to someone you've known for so long."

    "A beautiful beach covered in golden sand that glimmers under both the moon and sunlight, and water a beautiful shade of blue that reminded you of Stacy's eyes."
    
    scene bg beach_night with dissolve:
        zoom 1.3
        xalign 0.5
        yalign 1.0
    "You arrive first, panting. Good, you had time to calm yourself down before meeting with Stacy. You take a deep breath and inhale that fresh sea salt air."

    "You straighten up and start practicing in your head how you'll confess your love to Stacy."

    "You pace back and forth, mumbling to yourself. You waited anxiously, afraid that Stacy wouldn't show up and leave you hanging."

    "But you trusted her, she wouldn't break your heart like this."

    "Right...?"

    scene bg beach_night with dissolve
    "Before you could overthink any further, you feel a gentle tap on your shoulder."

    "It's her."

    scene bg beach_sunset_blur with dissolve
    show stacy neutral_b at chrCenter with dissolve
    "{i}Stacy...{/i}"

    s "You wanted to meet me...?"

    "By the time she arrived, the sun had already started to rise, helping set the ambience for your confession."

    "You take a deep breath once more and hold both Stacy's hands in yours."

    show stacy neutral_a at oneShake
    s "...!"

    s "[name]...? Wha-"

    p "Stacy Collins..."

    p "I've known you since we were in college."

    p "I'm gonna be honest and not lie to you saying that I fell head over heels the moment I met you."

    p "Because that's not the case with my feelings, and there's nothing wrong with that. These past few weeks, my admiration for you has grown tenfold."

    show stacy neutral_c at oneShake
    "Stacy looks at you with hope in her eyes... Maybe she's hoping for something... Something with you."

    p "What I'm saying is..."

    p "{i}Stacy, you're the one for me.{/i}"

    show stacy sad_a at oneShake
    pause 0.75
    show stacy sad_a at oneShake
    pause 0.25
    show stacy sad_a at oneShake
    pause 0.75

    show stacy sad_c at oneShake:
        zoom 0.65
        yalign 0.3
    "Tears formed in Stacy's eyes as she hugged you tightly." with vpunch
    
    s "[name]..."

    s "I... I-I..."

    show stacy sad_c at oneShake
    "She couldn't stop the tears falling from her eyes as she clung to you tightly."

    s "I feel the same way..."

    show stacy sad_c at chrCenter with dissolve
    "She pulled back to meet your gaze."

    s "All my life, the people I've dated always wanted my mom over me."

    s "They'd be interested at first, but when they meet my mom, it's like they stopped caring about me."

    show stacy sad_a with dissolve
    s "I know it's a harmless crush most of the time, but I can't help it... I can't help but feel worthless every time it happens."

    s "I felt bad even resenting my own mother at one point, because it's {i}not{/i} her fault..."

    show stacy sad_b with dissolve
    s "I'm sorry... Did I ramble too much?"

    scene bg beach_sunset with dissolve
    "You cupped Stacy's face with both your hands as you slowly leaned in for a kiss. Bold move, but to your surprise, Stacy kissed you first."

    show bg beach_sunset_blur with dissolve
    show stacycg with easeinleft
    "When the kiss broke, Stacy looked at you with watery eyes."

    p "Is this enough proof of me choosing you?"

    "She chuckles softly and hugs you again."
    
    "{b}{i}In the end, Stacy was indeed the girl for you.{/i}{/b}"

    jump end

label momEnd:
    hide stacy with easeoutleft
    show mom happy_a at chrCenter with easeinleft
    "She's all you want and you've waited for so long..."

    "{i}Stacy's mom...{/i}"

    "{i}Debbie Collins...{/i}"

    scene bg park_night with dissolve
    "You reach for your phone and hesitate... You don't know what you're doing, this all feels so wrong..."

    "But at the same time, you can't find it in yourself to care anymore. You've liked Stacy's mom for the longest time, and now that you're older and have a stable job, it feels like the right time to make a move."

    "You could be the person that would make Stacy's mom feel loved again."

    "You mustered up the courage and called Stacy's mom."

    p "Hello, Ms. Collins?"

    m "{i}Oh, hello sweetheart! Did you need something?{/i}"

    p "Uhm... I was wondering if you're free at the moment?"

    m "{i}I am, why?{/i}"

    "You swallow hard, it's now or never...!"

    p "Would you... like to have dinner with me?"

    p "I-I know of a good restaurant in my city, and I thought you could appreciate the good food..."

    "You did your best to not be a stuttering mess, but to your dismay your voice still cracked as you nervously asked Stacy's mom out to dinner."

    "The moment you heard a soft giggle through the phone, you felt your shoulders relax."

    m "{i}I would {b}love{/b} to, [name].{/i}"

    "When the phone call ended, you jumped for joy. You managed to ask Stacy's mom out to dinner!" with vpunch

    scene black with wipeleft
    "You send her the address of the restaurant as you make your way there on foot. Luckily, this restaurant was pretty near your office, give or take a 15 minute walk."

    scene bg fancy_hallway with wipeleft
    "As you arrived at the restaurant, the usually long line outside it was nowhere to be found. Perfect timing."

    "It's as if it was fate for you to have dinner here with her, the waiter letting you know that there was a vacant table for two."

    "You've heard great things about this restaurant online. People seem to love the food and the ambience it offers."

    scene bg lobby with dissolve
    "As you enter the establishment, you can't help but notice the place being on the fancier side."

    "You get seated and you straighten up as you wait for Stacy's mom to arrive."

    "In the meantime, you decided to peruse through the menu to possibly order some starters for both you and Stacy's mom."

    "You clear your throat as you sit there nervously, looking around to see if Stacy's mom has arrived yet."

    "You then feel a gentle tap behind you, you look over and it's her..."

    "The woman you've been yearning for all these years."

    show bg lobby_blur with dissolve
    show mom talk_a at chrCenter with dissolve
    "Stacy's mom."

    "She smiles as she takes a seat across from you."

    m "I'm sorry... I hope I didn't make you wait long, [name]."

    p "It's alright, Mi- Debbie... It's fine, Debbie."

    show mom talk_d at bounce
    "You caught her off guard by the shift, this was the first time you've ever used her first name. She's insisted time and time again for you to use it, but you were always so respectful and polite with her."

    show mom wink_talk with dissolve
    mx "Looks like you finally decided to call me by name, hm?"

    "You felt your ears ringing and going hot at her teasing, but you tried to not make it obvious that she had this effect on you."

    show mom talk_b with dissolve
    mx "I like it... I like hearing you call me by my name, sweetie."

    p "I-I'm glad then, Debbie..."

    p "I... I hope I'm not overstepping any boundaries by calling you by your first name."

    p "...Am I?"

    show mom happy_c at bounce
    "Debbie smiles at you and shakes her head."

    mx "Loosen up, hon! It really doesn't bother me."

    p "I ordered some appetizers, they should be here anytime soon."

    scene bg lobby with dissolve
    "As if on cue, a waiter pulls up to your table and lays out a tasty looking appetizer to start your dinner off."

    "As the dinner went on, you spent the entire time mustering up your courage to confess to Debbie."

    show bg lobby_blur with dissolve
    show mom talk_f at chrCenter with dissolve
    "Debbie definitely noticed that something was on your mind. You've barely touched your food after all."

    "You take one long gulp and downed your entire glass of champagne as a way to hype yourself up."

    "Fueled by both your boldness and alcohol, you begin to blurt out the confession to Debbie."

    p "Debbie... You..."

    p "{b}{i}You're all I want, and I've waited for so long...!{/i}{/b}" with vpunch

    "Your eyes widen and you instinctively, covering your mouth now that you realize what you said out loud."

    show mom talk_e with dissolve
    "Debbie also stares back at you in shock. She was stunned for a moment, unsure if what happened was truly real."

    show mom wink
    "Before you could take back your confession, you feel a kiss on your cheek." with vpunch

    mx "Are you sure you do, sweetheart? I'm way older than you..."

    p "Well, we're both adults, aren't we...?"

    p "But whenever you're around, I always feel my heart doing this weird... thing. I can never explain what it was up until recently."

    p "Debbie, I have feelings for you, and I don't care if you're my friend's mom!"

    scene bg lobby with dissolve
    "Debbie chuckles softly at your confession, and you're unsure whether she's reciprocated your feelings or not."

    show bg lobby_blur with dissolve
    show momcg with easeinright
    mx "Let's get you home and sobered up, okay?"

    mx "Then we'll properly talk."

    "You didn't expect to fumble your confession like this, but you could tell that Debbie shared the same feelings as you. And honestly, bless her soul for being such an understanding woman."

    "No matter how hard you tried, Stacy was never the girl for you because..."

    "{i}{b}You're in love with Stacy's mom.{/i}{/b}"

    jump end

label end:
    "{b}-- THE END --{/b}"
    #menu:
        #"anti-skip menu":
            #"test"

    # This ends the game.
    return
