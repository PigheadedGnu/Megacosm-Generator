#

self.redis.lpush('magicitem_kind', 'scroll')


self.redis.lpush('scroll_name_template', '{{ params.strength[\'name\'] }} {{ params.effect_description[\'name\'] }} scroll')
self.redis.lpush('scroll_name_template', '{{ params.strength[\'name\'] }} scroll of {{ params.effect_description[\'name\'] }}')
self.redis.lpush('scroll_name_template', 'scroll of {{ params.strength[\'name\'] }} {{ params.effect_description[\'name\'] }}')
self.redis.lpush('scroll_name_template', '{{ params.npc.name.shortname }}\'s {{ params.effect_description[\'name\'] }}')

#TODO need more like this (and need these formatted)
#                <option type="daze">can daze an opponent for a few seconds</option>
#                <option type="identification">can identify other magical items</option>
#                <option type="shield">projects the user through a magical shield</option>
#                <option type="knocking">can unlock or unbolt any lock</option>
#                <option type="darkness">summons a region of magical darkness</option>


HSET scroll_effect_description adnauseum    {"name":"ad nauseum",    "description":"causes sudden and severe nausea" }
self.redis.lpush('scroll_effect', 'adnauseum')
HSET scroll_effect_description aging    {"name":"aging",    "description":"causes instant aging" }
self.redis.lpush('scroll_effect', 'aging')
HSET scroll_effect_description animalmagnetism    {"name":"animal magnetism",    "description":"causes you to become irresistible" }
self.redis.lpush('scroll_effect', 'animalmagnetism')
HSET scroll_effect_description antidote    {"name":"antidote",    "description":"removes the effect of any poison" }
self.redis.lpush('scroll_effect', 'antidote')
HSET scroll_effect_description anti-paralysis    {"name":"anti-paralysis",    "description":"cures paralysis" }
self.redis.lpush('scroll_effect', 'anti-paralysis')
HSET scroll_effect_description assassinsevasion    {"name":"assassin\'s evasion",    "description":"increases your natural stealth ability" }
self.redis.lpush('scroll_effect', 'assassinsevasion')
HSET scroll_effect_description auraofprotection    {"name":"aura of protection",    "description":"provides arcane protection" }
self.redis.lpush('scroll_effect', 'auraofprotection')
HSET scroll_effect_description awaken    {"name":"awaken",    "description":"wakes a sleeping person" }
self.redis.lpush('scroll_effect', 'awaken')
HSET scroll_effect_description babbling    {"name":"babbling",    "description":"causes uncontrollable speaking of nonsense" }
self.redis.lpush('scroll_effect', 'babbling')
HSET scroll_effect_description barkskin    {"name":"barkskin",    "description":"causes hardening of the skin granting natural armor" }
self.redis.lpush('scroll_effect', 'barkskin')
HSET scroll_effect_description bearendurance    {"name":"bear endurance",    "description":"increases the endurance of the user" }
self.redis.lpush('scroll_effect', 'bearendurance')
HSET scroll_effect_description beautification    {"name":"beautification",    "description":"makes the user appear more attractive" }
self.redis.lpush('scroll_effect', 'beautification')
HSET scroll_effect_description befuddlement    {"name":"befuddlement",    "description":"makes the user become confused and reckless" }
self.redis.lpush('scroll_effect', 'befuddlement')
HSET scroll_effect_description beguiling    {"name":"beguiling",    "description":"makes the user appear more trustworthy" }
self.redis.lpush('scroll_effect', 'beguiling')
HSET scroll_effect_description beneficialmutation    {"name":"beneficial mutation",    "description":"provides some sort of beneficial mutation" }
self.redis.lpush('scroll_effect', 'beneficialmutation')
HSET scroll_effect_description berserkrage     {"name":"berserk rage ",    "description":"throws the user into an uncontrollable rage" }
self.redis.lpush('scroll_effect', 'berserkrage ')
HSET scroll_effect_description bless    {"name":"bless",    "description":"grants the blessing of an unknown deity" }
self.redis.lpush('scroll_effect', 'bless')
HSET scroll_effect_description blessingofthefae    {"name":"blessing of the fae",    "description":"causes the user to turn into a fairy" }
self.redis.lpush('scroll_effect', 'blessingofthefae')
HSET scroll_effect_description blindness    {"name":"blindness",    "description":"causes immediate blindness" }
self.redis.lpush('scroll_effect', 'blindness')
HSET scroll_effect_description blindnessremoval    {"name":"blindness removal",    "description":"restores sight to the blind" }
self.redis.lpush('scroll_effect', 'blindnessremoval')
HSET scroll_effect_description bliss    {"name":"bliss",    "description":"causes the user immediately to become blissful and happy" }
self.redis.lpush('scroll_effect', 'bliss')
HSET scroll_effect_description blood    {"name":"blood",    "description":"provides sustenance for creatures that drink blood" }
self.redis.lpush('scroll_effect', 'blood')
HSET scroll_effect_description blood-replenishing    {"name":"blood-replenishing",    "description":"restores lost blood from a severely injured person" }
self.redis.lpush('scroll_effect', 'blood-replenishing')
HSET scroll_effect_description bloodroot    {"name":"bloodroot",    "description":"causes the blood to become unappealing to blood drinkers" }
self.redis.lpush('scroll_effect', 'bloodroot')
HSET scroll_effect_description bloodthirst    {"name":"bloodthirst",    "description":"causes an unnatural, literal thirst for blood" }
self.redis.lpush('scroll_effect', 'bloodthirst')
HSET scroll_effect_description blur    {"name":"blur",    "description":"causes the user to become blurry and difficult to hit" }
self.redis.lpush('scroll_effect', 'blur')
HSET scroll_effect_description bottledgenie    {"name":"bottled genie",    "description":"turns the drinker into a genie and binds them to the bottle" }
self.redis.lpush('scroll_effect', 'bottledgenie')
HSET scroll_effect_description brilliance    {"name":"brilliance",    "description":"grants amazing insight" }
self.redis.lpush('scroll_effect', 'brilliance')
HSET scroll_effect_description bruiseremoval    {"name":"bruise removal",    "description":"removes minor injuries" }
self.redis.lpush('scroll_effect', 'bruiseremoval')
HSET scroll_effect_description bulge-eye    {"name":"bulge-eye",    "description":"causes user\'s eyes to bulge unnaturally" }
self.redis.lpush('scroll_effect', 'bulge-eye')
HSET scroll_effect_description bullstrength    {"name":"bull strength",    "description":"grants the user powerful physical strength" }
self.redis.lpush('scroll_effect', 'bullstrength')
HSET scroll_effect_description burn-healing    {"name":"burn-healing",    "description":"soothes and heals minor to severe burns" }
self.redis.lpush('scroll_effect', 'burn-healing')
HSET scroll_effect_description cacophony    {"name":"cacophony",    "description":"causes the user to hear incredibly loud, continual noise" }
self.redis.lpush('scroll_effect', 'cacophony')
HSET scroll_effect_description cagedimp    {"name":"caged imp",    "description":"makes the user subconsciously mischievous" }
self.redis.lpush('scroll_effect', 'cagedimp')
HSET scroll_effect_description calming    {"name":"calming",    "description":"calms the user of shock, trauma, etc" }
self.redis.lpush('scroll_effect', 'calming')
HSET scroll_effect_description catalyst    {"name":"catalyst",    "description":"causes another scroll or potion to double in potency" }
self.redis.lpush('scroll_effect', 'catalyst')
HSET scroll_effect_description catseye    {"name":"cats eye",    "description":"improves vision and enhances night vision" }
self.redis.lpush('scroll_effect', 'catseye')
HSET scroll_effect_description catsgrace    {"name":"cat\'s grace",    "description":"grants user uncanny grace" }
self.redis.lpush('scroll_effect', 'catsgrace')
HSET scroll_effect_description cheese    {"name":"cheese",    "description":"makes anything taste edible (although possibly still dangerous)" }
self.redis.lpush('scroll_effect', 'cheese')
HSET scroll_effect_description clone    {"name":"clone",    "description":"causes a painful splitting into two beings, one of which immediately dies" }
self.redis.lpush('scroll_effect', 'clone')
HSET scroll_effect_description coagulatedblood     {"name":"coagulated blood ",    "description":"provides slight satiation for vampires and carnivores" }
self.redis.lpush('scroll_effect', 'coagulatedblood ')
HSET scroll_effect_description confusion    {"name":"confusion",    "description":"confuses the user" }
self.redis.lpush('scroll_effect', 'confusion')
HSET scroll_effect_description coughing    {"name":"coughing",    "description":"provokes a powerful coughing fit" }
self.redis.lpush('scroll_effect', 'coughing')
HSET scroll_effect_description cunning    {"name":"cunning",    "description":"grants the user unsurpassed cleverness" }
self.redis.lpush('scroll_effect', 'cunning')
HSET scroll_effect_description cupid    {"name":"cupid",    "description":"causes the drinker to have an immediate romantic infatuation with whoever they see next" }
self.redis.lpush('scroll_effect', 'cupid')
HSET scroll_effect_description cureboils    {"name":"cure boils",    "description":"will heal painful or unsightly boils" }
self.redis.lpush('scroll_effect', 'cureboils')
HSET scroll_effect_description curecorruption    {"name":"cure corruption",    "description":"heals diseased or corrupted flesh" }
self.redis.lpush('scroll_effect', 'curecorruption')
HSET scroll_effect_description curedisease    {"name":"cure disease",    "description":"cures most diseases" }
self.redis.lpush('scroll_effect', 'curedisease')
HSET scroll_effect_description cureinsanity    {"name":"cure insanity",    "description":"calms the most unsound mind" }
self.redis.lpush('scroll_effect', 'cureinsanity')
HSET scroll_effect_description curemutation    {"name":"cure mutation",    "description":"will remove any unnatural mutations" }
self.redis.lpush('scroll_effect', 'curemutation')
HSET scroll_effect_description cureparalysis    {"name":"cure paralysis",    "description":"cures paralysis" }
self.redis.lpush('scroll_effect', 'cureparalysis')
HSET scroll_effect_description cureweakness    {"name":"cure weakness",    "description":"removes any unnatural weakness" }
self.redis.lpush('scroll_effect', 'cureweakness')
HSET scroll_effect_description currentstopper    {"name":"current stopper",    "description":"prevents electrocution" }
self.redis.lpush('scroll_effect', 'currentstopper')
HSET scroll_effect_description curseofthelycan    {"name":"curse of the lycan",    "description":"infects the user with lycanthropy" }
self.redis.lpush('scroll_effect', 'curseofthelycan')
HSET scroll_effect_description curseremoval    {"name":"curse removal",    "description":"removes most magical or supernatural curses" }
self.redis.lpush('scroll_effect', 'curseremoval')
HSET scroll_effect_description darkvision    {"name":"darkvision",    "description":"allows the user to see in the dark" }
self.redis.lpush('scroll_effect', 'darkvision')
HSET scroll_effect_description daylight    {"name":"daylight",    "description":"allows the user to see as if there was daylight present" }
self.redis.lpush('scroll_effect', 'daylight')
HSET scroll_effect_description deafness    {"name":"deafness",    "description":"causes complete loss of hearing" }
self.redis.lpush('scroll_effect', 'deafness')
HSET scroll_effect_description death-cap    {"name":"death-cap",    "description":"causes death if used" }
self.redis.lpush('scroll_effect', 'death-cap')
HSET scroll_effect_description deathward    {"name":"death ward",    "description":"prevents user from dying" }
self.redis.lpush('scroll_effect', 'deathward')
HSET scroll_effect_description deathwish    {"name":"deathwish",    "description":"causes subconscious desire to die through reckless behavior" }
self.redis.lpush('scroll_effect', 'deathwish')
HSET scroll_effect_description decay    {"name":"decay",    "description":"immediately causes flesh to rot" }
self.redis.lpush('scroll_effect', 'decay')
HSET scroll_effect_description deflection    {"name":"deflection",    "description":"provides some protection from attacks" }
self.redis.lpush('scroll_effect', 'deflection')
HSET scroll_effect_description degeneration    {"name":"degeneration",    "description":"causes a random ability to reduce" }
self.redis.lpush('scroll_effect', 'degeneration')
HSET scroll_effect_description delaypoison    {"name":"delay poison",    "description":"prevents the onset of toxic substances" }
self.redis.lpush('scroll_effect', 'delaypoison')
HSET scroll_effect_description desire    {"name":"desire",    "description":"causes the user to desperately desire something or someone" }
self.redis.lpush('scroll_effect', 'desire')
HSET scroll_effect_description despair    {"name":"despair",    "description":"causes a deep depression over the hopelessness of the situation" }
self.redis.lpush('scroll_effect', 'despair')
HSET scroll_effect_description detectcreature    {"name":"detect creature",    "description":"gives the user insight on the location of any nearby creatures" }
self.redis.lpush('scroll_effect', 'detectcreature')
HSET scroll_effect_description detectthings    {"name":"detect things",    "description":"gives the user insight on the location of a specific object" }
self.redis.lpush('scroll_effect', 'detectthings')
HSET scroll_effect_description dexterity    {"name":"dexterity",    "description":"grants the user impressive dexterity" }
self.redis.lpush('scroll_effect', 'dexterity')
HSET scroll_effect_description discord    {"name":"discord",    "description":"makes the drinker become irritable and pick fights" }
self.redis.lpush('scroll_effect', 'discord')
HSET scroll_effect_description diseaseremoval    {"name":"disease removal",    "description":"cures drinker of most diseases" }
self.redis.lpush('scroll_effect', 'diseaseremoval')
HSET scroll_effect_description divinepower    {"name":"divine power",    "description":"grants the user strength from an unknown deity" }
self.redis.lpush('scroll_effect', 'divinepower')
HSET scroll_effect_description divinerestoration    {"name":"divine restoration",    "description":"restores the user as a favor from an unknown deity" }
self.redis.lpush('scroll_effect', 'divinerestoration')
HSET scroll_effect_description dizziness    {"name":"dizziness",    "description":"makes the drinker dizzy and lightheaded" }
self.redis.lpush('scroll_effect', 'dizziness')
HSET scroll_effect_description dogbane    {"name":"dogbane",    "description":" is poisonous to anything with canine ancestry" }
self.redis.lpush('scroll_effect', 'dogbane')
HSET scroll_effect_description dragondung    {"name":"dragon dung",    "description":"causes the drinker to defecate a small number of coins" }
self.redis.lpush('scroll_effect', 'dragondung')
HSET scroll_effect_description dragonsbreath    {"name":"dragon\'s breath",    "description":"grants the user the ability to breathe fire like a dragon" }
self.redis.lpush('scroll_effect', 'dragonsbreath')
HSET scroll_effect_description dreamless    {"name":"dreamless",    "description":"prevents the user from dreaming during sleep" }
self.redis.lpush('scroll_effect', 'dreamless')
HSET scroll_effect_description drowsiness    {"name":"drowsiness",    "description":"makes the drinker incredibly drowsy" }
self.redis.lpush('scroll_effect', 'drowsiness')
HSET scroll_effect_description education    {"name":"education",    "description":"grants knowledge on a specific subject" }
self.redis.lpush('scroll_effect', 'education')
HSET scroll_effect_description embiggenment    {"name":"embiggenment",    "description":"enlarges the user by one size" }
self.redis.lpush('scroll_effect', 'embiggenment')
HSET scroll_effect_description endureelements    {"name":"endure elements",    "description":"grants resistance to the elements" }
self.redis.lpush('scroll_effect', 'endureelements')
HSET scroll_effect_description endure_elements      {"name":"endure elements",      "description":"increases resistance to the elements"    }
self.redis.lpush('scroll_effect', 'endure_elements')
HSET scroll_effect_description enlargement    {"name":"enlargement",    "description":"enlarges the user by one size" }
self.redis.lpush('scroll_effect', 'enlargement')
HSET scroll_effect_description enlightenment    {"name":"enlightenment",    "description":"provides the user with a random bonus on a given skill" }
self.redis.lpush('scroll_effect', 'enlightenment')
HSET scroll_effect_description euphoria    {"name":"euphoria",    "description":"induces an irrational happiness" }
self.redis.lpush('scroll_effect', 'euphoria')
HSET scroll_effect_description exploding    {"name":"exploding",    "description":"causes an explosive reaction when exposed to certain substances" }
self.redis.lpush('scroll_effect', 'exploding')
HSET scroll_effect_description fatiguing    {"name":"fatiguing",    "description":"causes user to feel fatigued" }
self.redis.lpush('scroll_effect', 'fatiguing')
HSET scroll_effect_description fearremoval    {"name":"fear removal",    "description":"removes fear caused by a specific source" }
self.redis.lpush('scroll_effect', 'fearremoval')
HSET scroll_effect_description fireprotection    {"name":"fire protection",    "description":"protects the user from fire and heat" }
self.redis.lpush('scroll_effect', 'fireprotection')
HSET scroll_effect_description flatulence    {"name":"flatulence",    "description":"causes uncontrollable, loud and unsavory gas" }
self.redis.lpush('scroll_effect', 'flatulence')
HSET scroll_effect_description flesheater    {"name":"flesh eater",    "description":"causes uneven and grotesque disfigurement" }
self.redis.lpush('scroll_effect', 'flesheater')
HSET scroll_effect_description flight    {"name":"flight",    "description":"grants the ability to fly" }
self.redis.lpush('scroll_effect', 'flight')
HSET scroll_effect_description flinch    {"name":"flinch",    "description":"causes the user to flinch uncontrollably" }
self.redis.lpush('scroll_effect', 'flinch')
HSET scroll_effect_description forgetfulness    {"name":"forgetfulness",    "description":"makes the user forgetful" }
self.redis.lpush('scroll_effect', 'forgetfulness')
HSET scroll_effect_description foxcunning     {"name":"fox cunning ",    "description":"makes the user more clever than normal" }
self.redis.lpush('scroll_effect', 'foxcunning ')
HSET scroll_effect_description freezing    {"name":"freezing",    "description":"lowers the body temperature of the drinker" }
self.redis.lpush('scroll_effect', 'freezing')
HSET scroll_effect_description friendship    {"name":"friendship",    "description":"grants the drinker the ability to become fast friends with someone upon meeting them" }
self.redis.lpush('scroll_effect', 'friendship')
HSET scroll_effect_description frostbite    {"name":"frostbite",    "description":"causes frost damage to drinker" }
self.redis.lpush('scroll_effect', 'frostbite')
HSET scroll_effect_description frostguard    {"name":"frostguard",    "description":"increases ice resistance" }
self.redis.lpush('scroll_effect', 'frostguard')
HSET scroll_effect_description fungal    {"name":"fungal",    "description":"causes user to grow unsightly fungal growths" }
self.redis.lpush('scroll_effect', 'fungal')
HSET scroll_effect_description fungiface    {"name":"fungiface",    "description":"makes the user\'s face erupt in fungus" }
self.redis.lpush('scroll_effect', 'fungiface')
HSET scroll_effect_description fury    {"name":"fury",    "description":"induces an uncontrollable rage towards others" }
self.redis.lpush('scroll_effect', 'fury')
HSET scroll_effect_description gaseousform    {"name":"gaseous form",    "description":"user takes a gaseous form" }
self.redis.lpush('scroll_effect', 'gaseousform')
HSET scroll_effect_description girding    {"name":"girding",    "description":"gives the user extra endurance" }
self.redis.lpush('scroll_effect', 'girding')
HSET scroll_effect_description grace    {"name":"grace",    "description":"grants the user unnatural grace" }
self.redis.lpush('scroll_effect', 'grace')
HSET scroll_effect_description hair    {"name":"hair",    "description":"causes user to grow thick, beautiful hair on their head" }
self.redis.lpush('scroll_effect', 'hair')
HSET scroll_effect_description hair-raising    {"name":"hair-raising",    "description":"causes the user\'s hair to stand on end" }
self.redis.lpush('scroll_effect', 'hair-raising')
HSET scroll_effect_description hallucination    {"name":"hallucination",    "description":"causes drinker to hallucinate" }
self.redis.lpush('scroll_effect', 'hallucination')
HSET scroll_effect_description hare    {"name":"hare",    "description":"causes user to grow a hare on their head" }
self.redis.lpush('scroll_effect', 'hare')
HSET scroll_effect_description haste                {"name":"haste",                "description":"allows user to move with extreme speed"  }
self.redis.lpush('scroll_effect', 'haste')
HSET scroll_effect_description hate    {"name":"hate",    "description":"causes a growing dislike of a person or thing" }
self.redis.lpush('scroll_effect', 'hate')
HSET scroll_effect_description healing              {"name":"healing",              "description":"can heal various wounds and ailments"    }
self.redis.lpush('scroll_effect', 'healing')
HSET scroll_effect_description heartbreak    {"name":"heartbreak",    "description":"causes an irrational feeling of loss and heartbreak" }
self.redis.lpush('scroll_effect', 'heartbreak')
HSET scroll_effect_description herbicide    {"name":"herbicide",    "description":"causes damage or death to plant-based life" }
self.redis.lpush('scroll_effect', 'herbicide')
HSET scroll_effect_description heroism    {"name":"heroism",    "description":"causes unusual recklessness and remission of fear" }
self.redis.lpush('scroll_effect', 'heroism')
HSET scroll_effect_description hiccuping    {"name":"hiccuping",    "description":"causes uncontrollable hiccuping" }
self.redis.lpush('scroll_effect', 'hiccuping')
HSET scroll_effect_description hidefromanimals    {"name":"hide from animals",    "description":"prevents animals from detecting the user" }
self.redis.lpush('scroll_effect', 'hidefromanimals')
HSET scroll_effect_description hidefromundead    {"name":"hide from undead",    "description":"prevents undead from detecting the user" }
self.redis.lpush('scroll_effect', 'hidefromundead')
HSET scroll_effect_description holyflame    {"name":"holy flame",    "description":"burns the drinker with a righteous flame" }
self.redis.lpush('scroll_effect', 'holyflame')
HSET scroll_effect_description hyena    {"name":"hyena",    "description":"causes hysteria and fits of uncontrollable laughter" }
self.redis.lpush('scroll_effect', 'hyena')
HSET scroll_effect_description ignition    {"name":"ignition",    "description":"causes user to uncontrollably belch flames" }
self.redis.lpush('scroll_effect', 'ignition')
HSET scroll_effect_description indestructibility    {"name":"indestructibility",    "description":"prevents the user from being damaged" }
self.redis.lpush('scroll_effect', 'indestructibility')
HSET scroll_effect_description influence    {"name":"influence",    "description":"grants the ability to influence others" }
self.redis.lpush('scroll_effect', 'influence')
HSET scroll_effect_description insanity    {"name":"insanity",    "description":"causes irrational and uncontrollable behavior" }
self.redis.lpush('scroll_effect', 'insanity')
HSET scroll_effect_description intimidation    {"name":"intimidation",    "description":"causes the user to be far more intimidating" }
self.redis.lpush('scroll_effect', 'intimidation')
HSET scroll_effect_description invigorating    {"name":"invigorating",    "description":"removes fatigue and keeps user awake" }
self.redis.lpush('scroll_effect', 'invigorating')
HSET scroll_effect_description invisibility    {"name":"invisibility",    "description":"makes the user invisible" }
self.redis.lpush('scroll_effect', 'invisibility')
HSET scroll_effect_description jawbind    {"name":"jawbind",    "description":"induces lockjaw in the user" }
self.redis.lpush('scroll_effect', 'jawbind')
HSET scroll_effect_description jumping              {"name":"jumping",              "description":"allows user to jump to amazing heights and distances"    }
self.redis.lpush('scroll_effect', 'jumping')
HSET scroll_effect_description knowledge    {"name":"knowledge",    "description":"grants the user knowledge on a specific subject" }
self.redis.lpush('scroll_effect', 'knowledge')
HSET scroll_effect_description laughter    {"name":"laughter",    "description":"causes the user to laugh uncontrollably" }
self.redis.lpush('scroll_effect', 'laughter')
HSET scroll_effect_description laxative    {"name":"laxative",    "description":"causes uncontrollable bowel movements" }
self.redis.lpush('scroll_effect', 'laxative')
HSET scroll_effect_description lazarus    {"name":"lazarus",    "description":"can return the user from death or near-death" }
self.redis.lpush('scroll_effect', 'lazarus')
HSET scroll_effect_description lean    {"name":"lean",    "description":"causes the user to immediately decrease body fat by 75%" }
self.redis.lpush('scroll_effect', 'lean')
HSET scroll_effect_description levitation    {"name":"levitation",    "description":"allows the user to levitate" }
self.redis.lpush('scroll_effect', 'levitation')
HSET scroll_effect_description librarian    {"name":"librarian",    "description":"grants user the ability to locate any nearby book" }
self.redis.lpush('scroll_effect', 'librarian')
HSET scroll_effect_description lightfoot    {"name":"light foot",    "description":"grants the user the ability to move quietly" }
self.redis.lpush('scroll_effect', 'lightfoot')
HSET scroll_effect_description livingdeath    {"name":"living death",    "description":"puts user into a death-like sleep" }
self.redis.lpush('scroll_effect', 'livingdeath')
HSET scroll_effect_description lockjaw    {"name":"lockjaw",    "description":"induces lockjaw in the user" }
self.redis.lpush('scroll_effect', 'lockjaw')
HSET scroll_effect_description longevity    {"name":"longevity",    "description":"cuts aging range by half" }
self.redis.lpush('scroll_effect', 'longevity')
HSET scroll_effect_description love    {"name":"love",    "description":"makes the user fall in love with whoever held the substance previously" }
self.redis.lpush('scroll_effect', 'love')
HSET scroll_effect_description luck    {"name":"luck",    "description":"grants unnatural luck to the user" }
self.redis.lpush('scroll_effect', 'luck')
HSET scroll_effect_description magearmor    {"name":"mage armor",    "description":"grants magical protection to the user" }
self.redis.lpush('scroll_effect', 'magearmor')
HSET scroll_effect_description magebane    {"name":"magebane",    "description":"causes illness in anyone who manipulates magical energies" }
self.redis.lpush('scroll_effect', 'magebane')
HSET scroll_effect_description magicfang    {"name":"magic fang",    "description":"causes user to grow magical fangs" }
self.redis.lpush('scroll_effect', 'magicfang')
HSET scroll_effect_description magicstone    {"name":"magic stone",    "description":"summons a handful of small throwing stones" }
self.redis.lpush('scroll_effect', 'magicstone')
HSET scroll_effect_description magicvestment    {"name":"magic vestment",    "description":"grants magical protection to the user\'s clothing" }
self.redis.lpush('scroll_effect', 'magicvestment')
HSET scroll_effect_description magicweapon    {"name":"magic weapon",    "description":"summons a force weapon shaped by the user\'s mind" }
self.redis.lpush('scroll_effect', 'magicweapon')
HSET scroll_effect_description malevolence    {"name":"malevolence",    "description":"causes brooding anger towards a random target" }
self.redis.lpush('scroll_effect', 'malevolence')
HSET scroll_effect_description manegrow    {"name":"manegrow",    "description":"causes user\'s head to grow thick, luxurious hair rapidly" }
self.redis.lpush('scroll_effect', 'manegrow')
HSET scroll_effect_description melancholy    {"name":"melancholy",    "description":"impairs enjoyment and fun" }
self.redis.lpush('scroll_effect', 'melancholy')
HSET scroll_effect_description memory    {"name":"memory",    "description":"enhances the drinker\'s memory" }
self.redis.lpush('scroll_effect', 'memory')
HSET scroll_effect_description mentalresistance    {"name":"mental resistance",    "description":"protects the user from mental attacks and damage" }
self.redis.lpush('scroll_effect', 'mentalresistance')
HSET scroll_effect_description midastouch    {"name":"midas touch",    "description":"allows user to turn any small object to gold" }
self.redis.lpush('scroll_effect', 'midastouch')
HSET scroll_effect_description might    {"name":"might",    "description":"greatly increases user\'s strength" }
self.redis.lpush('scroll_effect', 'might')
HSET scroll_effect_description misdirection    {"name":"misdirection",    "description":"grants user the ability to misdirect others visually or verbally" }
self.redis.lpush('scroll_effect', 'misdirection')
HSET scroll_effect_description monster    {"name":"monster",    "description":"causes user to transform into a random creature" }
self.redis.lpush('scroll_effect', 'monster')
HSET scroll_effect_description mouthitching    {"name":"mouth itching",    "description":"causes insufferable itching of the inside of the mouth" }
self.redis.lpush('scroll_effect', 'mouthitching')
HSET scroll_effect_description muffling    {"name":"muffling",    "description":"wraps the user in a cocoon of silence" }
self.redis.lpush('scroll_effect', 'muffling')
HSET scroll_effect_description mummycurse    {"name":"mummy curse",    "description":"causes illness and a slow death unless curse is broken" }
self.redis.lpush('scroll_effect', 'mummycurse')
HSET scroll_effect_description neutralizepoison    {"name":"neutralize poison",    "description":"neutralizes any poisons in the user\'s system" }
self.redis.lpush('scroll_effect', 'neutralizepoison')
HSET scroll_effect_description neutralize_poison    {"name":"neutralize poison",    "description":"neutralizes various poisons"          }
self.redis.lpush('scroll_effect', 'neutralize_poison')
HSET scroll_effect_description neutralmutation    {"name":"neutral mutation",    "description":"provides some sort of neutral mutation" }
self.redis.lpush('scroll_effect', 'neutralmutation')
HSET scroll_effect_description nightmare    {"name":"nightmare",    "description":"invokes nightmares the next time the user sleeps" }
self.redis.lpush('scroll_effect', 'nightmare')
HSET scroll_effect_description nondetection    {"name":"nondetection",    "description":"makes the user undetectable through magical means" }
self.redis.lpush('scroll_effect', 'nondetection')
HSET scroll_effect_description noxiousfumes    {"name":"noxious fumes",    "description":"causes the user to emit noxious, suffocating fumes" }
self.redis.lpush('scroll_effect', 'noxiousfumes')
HSET scroll_effect_description obesity    {"name":"obesity",    "description":"causes an immediate increase in body fat by 100%" }
self.redis.lpush('scroll_effect', 'obesity')
HSET scroll_effect_description oculus    {"name":"oculus",    "description":"restores the user\'s sight" }
self.redis.lpush('scroll_effect', 'oculus')
HSET scroll_effect_description owlwisdom    {"name":"owl wisdom",    "description":"grants the user powerful insight" }
self.redis.lpush('scroll_effect', 'owlwisdom')
HSET scroll_effect_description paralysis    {"name":"paralysis",    "description":"paralyzes the user" }
self.redis.lpush('scroll_effect', 'paralysis')
HSET scroll_effect_description paralysisremoval    {"name":"paralysis removal",    "description":"removes paralysis from user" }
self.redis.lpush('scroll_effect', 'paralysisremoval')
HSET scroll_effect_description pacifism    {"name":"pacifism",    "description":"causes immediate aversion to confrontation" }
self.redis.lpush('scroll_effect', 'pacifism')
HSET scroll_effect_description passwithouttrace    {"name":"pass without trace",    "description":"grants the user the ability to move without leaving a trail" }
self.redis.lpush('scroll_effect', 'passwithouttrace')
HSET scroll_effect_description peace    {"name":"peace",    "description":"relieves anxiety" }
self.redis.lpush('scroll_effect', 'peace')
HSET scroll_effect_description perception    {"name":"perception",    "description":"increases the user\'s perception" }
self.redis.lpush('scroll_effect', 'perception')
HSET scroll_effect_description piercingwit    {"name":"piercing wit",    "description":"makes the user keenly aware of the missteps of others" }
self.redis.lpush('scroll_effect', 'piercingwit')
HSET scroll_effect_description pinkeye    {"name":"pinkeye",    "description":"causes drinker to suffer immediate conjunctivitis" }
self.redis.lpush('scroll_effect', 'pinkeye')
HSET scroll_effect_description poison    {"name":"poison",    "description":"user becomes immediately ill" }
self.redis.lpush('scroll_effect', 'poison')
HSET scroll_effect_description polymorph    {"name":"polymorph",    "description":"grants the user the ability to morph into another shape" }
self.redis.lpush('scroll_effect', 'polymorph')
HSET scroll_effect_description porridge    {"name":"porridge",    "description":"removes any immediate hunger" }
self.redis.lpush('scroll_effect', 'porridge')
HSET scroll_effect_description precision    {"name":"precision",    "description":"grants the user precision with ranged weaponry" }
self.redis.lpush('scroll_effect', 'precision')
HSET scroll_effect_description prowess    {"name":"prowess",    "description":"grants the user unmatched agility, strength or endurance" }
self.redis.lpush('scroll_effect', 'prowess')
HSET scroll_effect_description pumpkinhead    {"name":"pumpkinhead",    "description":"turns the user\'s head into an unlit jack-o-lantern" }
self.redis.lpush('scroll_effect', 'pumpkinhead')
HSET scroll_effect_description pureluck    {"name":"pure luck",    "description":"grants the user unnatural luck" }
self.redis.lpush('scroll_effect', 'pureluck')
HSET scroll_effect_description purification    {"name":"purification",    "description":"cleanses the user of any non-magical diseases and filth" }
self.redis.lpush('scroll_effect', 'purification')
HSET scroll_effect_description rage    {"name":"rage",    "description":"causes the user to develop uncontrolled, undirected rage" }
self.redis.lpush('scroll_effect', 'rage')
HSET scroll_effect_description rano    {"name":"rano",    "description":"causes user to develop large horns on their forehead" }
self.redis.lpush('scroll_effect', 'rano')
HSET scroll_effect_description rawchaos    {"name":"raw chaos",    "description":"inundates the user with raw chaos" }
self.redis.lpush('scroll_effect', 'rawchaos')
HSET scroll_effect_description reason    {"name":"reason",    "description":"protects the user from the effects of insanity" }
self.redis.lpush('scroll_effect', 'reason')
HSET scroll_effect_description reduceperson    {"name":"reduce person",    "description":"decreases the user\'s size by 50%" }
self.redis.lpush('scroll_effect', 'reduceperson')
HSET scroll_effect_description reflection    {"name":"reflection",    "description":"grants the user insight" }
self.redis.lpush('scroll_effect', 'reflection')
HSET scroll_effect_description regeneration    {"name":"regeneration",    "description":"allows the user to regrow lost limbs" }
self.redis.lpush('scroll_effect', 'regeneration')
HSET scroll_effect_description removeblindness    {"name":"remove blindness",    "description":"restores sight" }
self.redis.lpush('scroll_effect', 'removeblindness')
HSET scroll_effect_description removecurse    {"name":"remove curse",    "description":"removes minor curses" }
self.redis.lpush('scroll_effect', 'removecurse')
HSET scroll_effect_description removedeafness    {"name":"remove deafness",    "description":"restores hearing" }
self.redis.lpush('scroll_effect', 'removedeafness')
HSET scroll_effect_description removedisease    {"name":"remove disease",    "description":"removes most diseases" }
self.redis.lpush('scroll_effect', 'removedisease')
HSET scroll_effect_description removefear    {"name":"remove fear",    "description":"removes unnatural fear" }
self.redis.lpush('scroll_effect', 'removefear')
HSET scroll_effect_description remove_fear          {"name":"remove fear",          "description":"fortifies the user against the most terrifying foes"     }
self.redis.lpush('scroll_effect', 'remove_fear')
HSET scroll_effect_description removeparalysis    {"name":"remove paralysis",    "description":"grants the ability to move freely" }
self.redis.lpush('scroll_effect', 'removeparalysis')
HSET scroll_effect_description replenishing    {"name":"replenishing",    "description":"heals and revitalizes the user" }
self.redis.lpush('scroll_effect', 'replenishing')
HSET scroll_effect_description resistacid    {"name":"resist acid",    "description":"toughens the user and makes them resistant to corrosive substances" }
self.redis.lpush('scroll_effect', 'resistacid')
HSET scroll_effect_description resistcold    {"name":"resist cold",    "description":"provides resistance to the cold" }
self.redis.lpush('scroll_effect', 'resistcold')
HSET scroll_effect_description resistelectricity    {"name":"resist electricity",    "description":"provides resistance to electricity" }
self.redis.lpush('scroll_effect', 'resistelectricity')
HSET scroll_effect_description resistfire     {"name":"resist fire ",    "description":"provides resistance to fire" }
self.redis.lpush('scroll_effect', 'resistfire ')
HSET scroll_effect_description resistsonic     {"name":"resist sonic ",    "description":"provides resistance to sonic damage" }
self.redis.lpush('scroll_effect', 'resistsonic ')
HSET scroll_effect_description resourcefinder    {"name":"resource finder",    "description":"allows the user to sniff out needed resources" }
self.redis.lpush('scroll_effect', 'resourcefinder')
HSET scroll_effect_description respiration          {"name":"respiration",          "description":"allows the user to breathe in otherwise dangerous environments" }
self.redis.lpush('scroll_effect', 'respiration')
HSET scroll_effect_description restoration     {"name":"restoration ",    "description":"reverts effects of any other spells" }
self.redis.lpush('scroll_effect', 'restoration ')
HSET scroll_effect_description revive    {"name":"revive",    "description":"awakens an unconscious person" }
self.redis.lpush('scroll_effect', 'revive')
HSET scroll_effect_description rockskin    {"name":"rock skin",    "description":"hardens the skin of the user while allowing flexibility" }
self.redis.lpush('scroll_effect', 'rockskin')
HSET scroll_effect_description sanctuary    {"name":"sanctuary",    "description":"grants the user protection from combat" }
self.redis.lpush('scroll_effect', 'sanctuary')
HSET scroll_effect_description scouringsolution    {"name":"scouring solution",    "description":"is good for cleaning caked-on grime" }
self.redis.lpush('scroll_effect', 'scouringsolution')
HSET scroll_effect_description seduction    {"name":"seduction",    "description":"grants the user the ability to seduce anyone" }
self.redis.lpush('scroll_effect', 'seduction')
HSET scroll_effect_description seeinvisible    {"name":"see invisible",    "description":"grants the user the ability to see invisible things" }
self.redis.lpush('scroll_effect', 'seeinvisible')
HSET scroll_effect_description serpent    {"name":"serpent",    "description":"causes the user to grow poisonous fangs" }
self.redis.lpush('scroll_effect', 'serpent')
HSET scroll_effect_description shield    {"name":"shield",    "description":"grants the user a magical force shield for protection" }
self.redis.lpush('scroll_effect', 'shield')
HSET scroll_effect_description shieldoffaith     {"name":"shield of faith ",    "description":"grants the user a magical force shield from an unknown deity" }
self.redis.lpush('scroll_effect', 'shieldoffaith ')
HSET scroll_effect_description shrinking    {"name":"shrinking",    "description":"causes the drinker to shrink" }
self.redis.lpush('scroll_effect', 'shrinking')
HSET scroll_effect_description sickness    {"name":"sickness",    "description":"causes the user to display symptoms of severe illness" }
self.redis.lpush('scroll_effect', 'sickness')
HSET scroll_effect_description skelegro    {"name":"skelegro",    "description":"regrows any missing bones" }
self.redis.lpush('scroll_effect', 'skelegro')
HSET scroll_effect_description slashingfury    {"name":"slashing fury",    "description":"causes the user to fly into a frenzy when holding a blade" }
self.redis.lpush('scroll_effect', 'slashingfury')
HSET scroll_effect_description slaying    {"name":"slaying",    "description":"grants the user unnatural vigor when combating a specific enemy" }
self.redis.lpush('scroll_effect', 'slaying')
HSET scroll_effect_description sleep    {"name":"sleep",    "description":"causes the user to fall asleep for up to 24 hours" }
self.redis.lpush('scroll_effect', 'sleep')
HSET scroll_effect_description sleeping    {"name":"sleeping",    "description":"forces the user into a deep sleep" }
self.redis.lpush('scroll_effect', 'sleeping')
HSET scroll_effect_description slowness    {"name":"slowness",    "description":"causes the user to move with extreme slowness" }
self.redis.lpush('scroll_effect', 'slowness')
HSET scroll_effect_description snakehair    {"name":"snakehair",    "description":"causes user to sprout snakes from their head" }
self.redis.lpush('scroll_effect', 'snakehair')
HSET scroll_effect_description snuffling    {"name":"snuffling",    "description":"causes the user to continuously sniffle" }
self.redis.lpush('scroll_effect', 'snuffling')
HSET scroll_effect_description socialgrace    {"name":"social grace",    "description":"grants unnatural skill in social situations" }
self.redis.lpush('scroll_effect', 'socialgrace')
HSET scroll_effect_description spark    {"name":"spark",    "description":"causes the user to suffer from continual, uncontrollable electrical outbursts" }
self.redis.lpush('scroll_effect', 'spark')
HSET scroll_effect_description sparklingapplecider    {"name":"sparkling apple cider",    "description":"causes the user to desire apples" }
self.redis.lpush('scroll_effect', 'sparklingapplecider')
HSET scroll_effect_description speed    {"name":"speed",    "description":"allows the user to move quickly" }
self.redis.lpush('scroll_effect', 'speed')
HSET scroll_effect_description spellbreaker    {"name":"spell breaker",    "description":"breaks any existing spell effects on the user" }
self.redis.lpush('scroll_effect', 'spellbreaker')
HSET scroll_effect_description spicyfungalgumbo    {"name":"spicy fungal gumbo",    "description":"causes severe pain and hallucinations" }
self.redis.lpush('scroll_effect', 'spicyfungalgumbo')
HSET scroll_effect_description spiderclimb    {"name":"spider climb",    "description":"grants the user the ability to climb walls" }
self.redis.lpush('scroll_effect', 'spiderclimb')
HSET scroll_effect_description staticdischarge    {"name":"static discharge",    "description":"causes unnatural buildup of static discharge" }
self.redis.lpush('scroll_effect', 'staticdischarge')
HSET scroll_effect_description steeledcurtain    {"name":"steeled curtain",    "description":"increases the protection of existing armor" }
self.redis.lpush('scroll_effect', 'steeledcurtain')
HSET scroll_effect_description stomachgrowling    {"name":"stomach growling",    "description":"provokes stomach growling" }
self.redis.lpush('scroll_effect', 'stomachgrowling')
HSET scroll_effect_description stoneskin    {"name":"stoneskin",    "description":"grants the user hardened skin" }
self.redis.lpush('scroll_effect', 'stoneskin')
HSET scroll_effect_description stonetoflesh    {"name":"stone to flesh",    "description":"can be used to cure petrification" }
self.redis.lpush('scroll_effect', 'stonetoflesh')
HSET scroll_effect_description strength    {"name":"strength",    "description":"grants unusual strength to the drinker" }
self.redis.lpush('scroll_effect', 'strength')
HSET scroll_effect_description swelling    {"name":"swelling",    "description":"causes severe swelling of a random section of the body" }
self.redis.lpush('scroll_effect', 'swelling')
HSET scroll_effect_description swiftness    {"name":"swiftness",    "description":"grants the user the ability to move quickly" }
self.redis.lpush('scroll_effect', 'swiftness')
HSET scroll_effect_description tongues    {"name":"tongues",    "description":"allows the user to speak and understand any language" }
self.redis.lpush('scroll_effect', 'tongues')
HSET scroll_effect_description toughness    {"name":"toughness",    "description":"grants the user increased endurance" }
self.redis.lpush('scroll_effect', 'toughness')
HSET scroll_effect_description training    {"name":"training",    "description":"allows the user to increase effectiveness of a single skill" }
self.redis.lpush('scroll_effect', 'training')
HSET scroll_effect_description trollblood    {"name":"troll blood",    "description":"grants the user minor regenerative abilities" }
self.redis.lpush('scroll_effect', 'trollblood')
HSET scroll_effect_description truth    {"name":"truth",    "description":"makes the user tell the truth" }
self.redis.lpush('scroll_effect', 'truth')
HSET scroll_effect_description tumbling    {"name":"tumbling",    "description":"grants the user unnatural tumbling skills" }
self.redis.lpush('scroll_effect', 'tumbling')
HSET scroll_effect_description unfortunatemutation    {"name":"unfortunate mutation",    "description":"provides some sort of unfortunate mutation" }
self.redis.lpush('scroll_effect', 'unfortunatemutation')
HSET scroll_effect_description uselessness    {"name":"uselessness",    "description":"has no discernible effect" }
self.redis.lpush('scroll_effect', 'uselessness')
HSET scroll_effect_description vampirebite    {"name":"vampire bite",    "description":"infects user with vampirism" }
self.redis.lpush('scroll_effect', 'vampirebite')
HSET scroll_effect_description vampiricsunscreen    {"name":"vampiric sunscreen",    "description":"mitigates any penalties taken from sunlight" }
self.redis.lpush('scroll_effect', 'vampiricsunscreen')
HSET scroll_effect_description venomguard    {"name":"venomguard",    "description":"grants poison resistance" }
self.redis.lpush('scroll_effect', 'venomguard')
HSET scroll_effect_description visibility    {"name":"visibility",    "description":"grants visibility to the invisible" }
self.redis.lpush('scroll_effect', 'visibility')
HSET scroll_effect_description vision    {"name":"vision",    "description":"grants the user a mysterious and unclear vision" }
self.redis.lpush('scroll_effect', 'vision')
HSET scroll_effect_description vocality    {"name":"vocality",    "description":"alters the user\'s voice" }
self.redis.lpush('scroll_effect', 'vocality')
HSET scroll_effect_description waterbreathing    {"name":"water breathing",    "description":"allows the user to breathe underwater" }
self.redis.lpush('scroll_effect', 'waterbreathing')
HSET scroll_effect_description waterwalk    {"name":"water walk",    "description":"allows the user to walk on water" }
self.redis.lpush('scroll_effect', 'waterwalk')
HSET scroll_effect_description weakness    {"name":"weakness",    "description":"causes the user to feel weak" }
self.redis.lpush('scroll_effect', 'weakness')
HSET scroll_effect_description wide-eye    {"name":"wide-eye",    "description":"prevents the user from falling asleep" }
self.redis.lpush('scroll_effect', 'wide-eye')
HSET scroll_effect_description wolfsbane    {"name":"wolfsbane",    "description":"is poisonous to a lycanthrope but protects uninfected user from infection" }
self.redis.lpush('scroll_effect', 'wolfsbane')
HSET scroll_effect_description wound-cleaning    {"name":"wound-cleaning",    "description":"is an anti-septic that prevents infection from sinking in" }
self.redis.lpush('scroll_effect', 'wound-cleaning')
HSET scroll_effect_description zombification    {"name":"zombification",    "description":"causes the user to show immediate signs of zombification" }
self.redis.lpush('scroll_effect', 'zombification')



            
#<!-- may cause blindness, which -->

ZADD scroll_duration  10  {"name":"is temporary",           "score":10  }
ZADD scroll_duration  20  {"name":"lasts a few seconds",    "score":20  }
ZADD scroll_duration  30  {"name":"lasts a minute",         "score":30  }
ZADD scroll_duration  40  {"name":"lasts a few minutes",    "score":40  }
ZADD scroll_duration  50  {"name":"lasts several minutes",  "score":50  }
ZADD scroll_duration  60  {"name":"lasts an hour",          "score":60  }
ZADD scroll_duration  70  {"name":"lasts a few hours",      "score":70  }
ZADD scroll_duration  80  {"name":"lasts several hours",    "score":80  }
ZADD scroll_duration  85  {"name":"lasts a day",            "score":85  }
ZADD scroll_duration  90  {"name":"lasts a few days",       "score":90  }
ZADD scroll_duration  95  {"name":"lasts a week",           "score":95  }
ZADD scroll_duration  98  {"name":"lasts weeks",            "score":98  }
ZADD scroll_duration 100  {"name":"is permanent",           "score":100  }



            
SET   scroll_sideeffect_chance 50
self.redis.lpush('scroll_sideeffect', 'seizures')
self.redis.lpush('scroll_sideeffect', 'blindness')
self.redis.lpush('scroll_sideeffect', 'death')
self.redis.lpush('scroll_sideeffect', 'melting flesh')
self.redis.lpush('scroll_sideeffect', 'spontaneous combustion')
self.redis.lpush('scroll_sideeffect', 'muteness')
self.redis.lpush('scroll_sideeffect', 'mouth glued shut')
self.redis.lpush('scroll_sideeffect', 'skin to turn an unnatural color')
self.redis.lpush('scroll_sideeffect', 'vomiting')
self.redis.lpush('scroll_sideeffect', 'nausea ')
self.redis.lpush('scroll_sideeffect', 'irritability')
self.redis.lpush('scroll_sideeffect', 'dizziness')
self.redis.lpush('scroll_sideeffect', 'fatigue')
self.redis.lpush('scroll_sideeffect', 'allergic reactions')
self.redis.lpush('scroll_sideeffect', 'fever')
self.redis.lpush('scroll_sideeffect', 'apathy')
self.redis.lpush('scroll_sideeffect', 'lethargy')
self.redis.lpush('scroll_sideeffect', 'paranoia')
self.redis.lpush('scroll_sideeffect', 'irrational behavior')
self.redis.lpush('scroll_sideeffect', 'hallucinations')
self.redis.lpush('scroll_sideeffect', 'levitation')
self.redis.lpush('scroll_sideeffect', 'colour blindness')
self.redis.lpush('scroll_sideeffect', 'sprouting feathers')
self.redis.lpush('scroll_sideeffect', 'sprouting hairs')
self.redis.lpush('scroll_sideeffect', 'vertigo')
self.redis.lpush('scroll_sideeffect', 'uncontrolled bowel movements')
self.redis.lpush('scroll_sideeffect', 'uncontrolled urination')
self.redis.lpush('scroll_sideeffect', 'severe muscle cramps')
            
self.redis.lpush('scroll_material', 'papyrus')
self.redis.lpush('scroll_material', 'sheepskin')
self.redis.lpush('scroll_material', 'paper')
self.redis.lpush('scroll_material', 'parchment')
self.redis.lpush('scroll_material', 'vellum')
self.redis.lpush('scroll_material', 'leather')
            
# rarity- how rare is this scroll in this region
# rarity controls how likely they will know of it.

# scroll contains ______ symbols .
SET   scroll_writingtype_chance 10
self.redis.lpush('scroll_writingtype', 'cryptic')
self.redis.lpush('scroll_writingtype', 'indecipherable')
self.redis.lpush('scroll_writingtype', 'strange')
self.redis.lpush('scroll_writingtype', 'arcane')
self.redis.lpush('scroll_writingtype', 'divine')
self.redis.lpush('scroll_writingtype', 'ritualistic')

# scroll contains cryptic _______ .
self.redis.lpush('scroll_writingform', 'symbols')
self.redis.lpush('scroll_writingform', 'writing')
self.redis.lpush('scroll_writingform', 'pictograms')
self.redis.lpush('scroll_writingform', 'ideograms')
self.redis.lpush('scroll_writingform', 'glyphs')
self.redis.lpush('scroll_writingform', 'script')
self.redis.lpush('scroll_writingform', 'scrawlings')

# The container has a label, which is ____
SET   scroll_container_label_chance 30
self.redis.lpush('scroll_container_label', 'illegible')
self.redis.lpush('scroll_container_label', 'clearly written (and correct)')
self.redis.lpush('scroll_container_label', 'clearly written (and incorrect)')
self.redis.lpush('scroll_container_label', 'written in an uncommon language')
self.redis.lpush('scroll_container_label', 'covered in ideograms')
self.redis.lpush('scroll_container_label', 'signed by the creator')

# The scroll is housed in a ____
self.redis.lpush('scroll_container_type', 'scroll case')
self.redis.lpush('scroll_container_type', 'folder')
self.redis.lpush('scroll_container_type', 'book')
self.redis.lpush('scroll_container_type', 'clay canister')
self.redis.lpush('scroll_container_type', 'glass tube')
