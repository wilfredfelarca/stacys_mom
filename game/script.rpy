# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

default name = "Dayyo" #Dayyo is the failsafe player name. Don't ask.
default stacyLove = 0
default momLove = 0


define p = Character(_("[name]"), color="#60877b")
define s = Character(_("Stacy"), color="#b535c9")
define m = Character(_("Stacy's Mom"), color="#da203f")
define c = Character(_("Creep"), color="#905d00")

### Transforms for various uses such as tweening the characters or scenes.

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

label seq3:
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

    show mom talk_e at midright with dissolve
    show stacy neutral_a at midleft with dissolve
    s "Wanna get out of here?"

    "You find yourself nodding at the offer, and you almost feel embarrassed at how eager you are." with vpunch

    "But to be honest? You'd rather catch up with these two gorgeous ladies than having to sit through a reunion where everybody pretends to like each other."

    "When in reality, they probably used this reunion as an excuse to show off and feel better about themselves."
    scene black with dissolve
    jump seq4

label seq4:
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

label seq5start:
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

label seq5stacy:
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

label seq5mom:
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

label seq6start:
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

label seq6stacy:
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

    scene bg office with wiperight
    
    "The elevator door opens, and you see Stacy in a conference room along with five other people. They all looked exhausted."

    "You knock on the door gently and wave at Stacy through the window."

    "Her expression lights up the moment she sees you, and she immediately meets you at the door."

    show bg office_blur with dissolve
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

    jump seq7

label seq6mom:
    "seq6mom wip"

label seq7:

    #centered "this text is in the center"

    jump start_minigame #label in File 'minigame_fable_2'
    # After the minigame, it will jump to "end", as specified in said file!
    # TODO: Make a dedicated function "label" for the minigame script to jump to when its done!
    # It will work by having some dedicated plot variable that it checks via else-if to know which scene to jump to!!

label end:
    # This ends the game.
    return
