# duration 
# combatduration
# target
# growth
# smallanimal
# largeanimal
# disposition
# suze
# distance
# direction
# damagetype
# smell
# taste
# radius
# color
# multiplier
# suffers
# spelleffect
# plants
# liquid
# soundvolume
# soundeffect
# location
# craving
# coating
# metal
# coinmetal
# minion
# minions
# flowers
# language
# coverage
# heavitem


self.redis.lpush('misfire_dexsave', 'There is no save.')
self.redis.lpush('misfire_dexsave', '(easy dexterity save)')
self.redis.lpush('misfire_dexsave', '(moderate dexterity save)')

self.redis.lpush('misfire_wissave', 'There is no save.')
self.redis.lpush('misfire_wissave', '(easy wisdom save)')
self.redis.lpush('misfire_wissave', '(moderate wisdom save)')


self.redis.lpush('misfire_heavyitem', 'safe')
self.redis.lpush('misfire_heavyitem', 'anvil')
self.redis.lpush('misfire_heavyitem', 'barrel')
self.redis.lpush('misfire_heavyitem', 'lead bar')
self.redis.lpush('misfire_heavyitem', 'orb of hot, molten lead')

self.redis.lpush('misfire_coverage', 'mud')
self.redis.lpush('misfire_coverage', 'ash')
self.redis.lpush('misfire_coverage', 'flower petals')
self.redis.lpush('misfire_coverage', 'marshmellow fluff')
self.redis.lpush('misfire_coverage', 'feces')


self.redis.lpush('misfire_language', 'common')
self.redis.lpush('misfire_language', 'elven')
self.redis.lpush('misfire_language', 'dwarven')
self.redis.lpush('misfire_language', 'giant')

self.redis.lpush('misfire_flowers', 'red roses')
self.redis.lpush('misfire_flowers', 'daffodils')
self.redis.lpush('misfire_flowers', 'carnations')
self.redis.lpush('misfire_flowers', 'dandelions')

# a[n] ________ is needed to remove lingering effects before the duration is over.
self.redis.lpush('misfire_cure', 'dispel magic')
self.redis.lpush('misfire_cure', 'remove curse')
self.redis.lpush('misfire_cure', 'lesser restoration')
self.redis.lpush('misfire_cure', 'greater restoration')
self.redis.lpush('misfire_cure', 'bath')
self.redis.lpush('misfire_cure', 'blood sacrifice')
self.redis.lpush('misfire_cure', 'apology to the gods')

self.redis.lpush('misfire_minion', 'zombie')
self.redis.lpush('misfire_minion', 'skeleton')
self.redis.lpush('misfire_minion', 'peasant')
self.redis.lpush('misfire_minion', 'goblin')
self.redis.lpush('misfire_minion', 'kobold')
self.redis.lpush('misfire_minion', 'fairy')

self.redis.lpush('misfire_minions', 'zombies')
self.redis.lpush('misfire_minions', 'skeletons')
self.redis.lpush('misfire_minions', 'townsfolk')
self.redis.lpush('misfire_minions', 'goblins')
self.redis.lpush('misfire_minions', 'orcs')
self.redis.lpush('misfire_minions', 'corgis')

self.redis.lpush('misfire_coating', 'chalkdust')
self.redis.lpush('misfire_coating', 'oil')
self.redis.lpush('misfire_coating', 'lard')
self.redis.lpush('misfire_coating', 'honey')
self.redis.lpush('misfire_coating', 'tar')
self.redis.lpush('misfire_coating', 'pollen')
self.redis.lpush('misfire_coating', 'blood')
self.redis.lpush('misfire_coating', 'taffy')
self.redis.lpush('misfire_coating', 'rancid milk')

self.redis.lpush('misfire_craving', 'moose dung')
self.redis.lpush('misfire_craving', 'chocolate')
self.redis.lpush('misfire_craving', 'grass')
self.redis.lpush('misfire_craving', 'dirt')
self.redis.lpush('misfire_craving', 'brussel sprouts')


# which will last ___

self.redis.lpush('misfire_duration', 'a few seconds')
self.redis.lpush('misfire_duration', 'a minute')
self.redis.lpush('misfire_duration', 'a few minutes')
self.redis.lpush('misfire_duration', 'an hour')
self.redis.lpush('misfire_duration', 'a few hours')
self.redis.lpush('misfire_duration', 'a day')
self.redis.lpush('misfire_duration', 'a few days')
self.redis.lpush('misfire_duration', 'a week')
self.redis.lpush('misfire_duration', 'a few weeks')
self.redis.lpush('misfire_duration', 'a month')
self.redis.lpush('misfire_duration', 'a few months')
self.redis.lpush('misfire_duration', 'a year')
self.redis.lpush('misfire_duration', 'a few years')
self.redis.lpush('misfire_duration', 'a decade')
self.redis.lpush('misfire_duration', 'a few decades')


self.redis.lpush('misfire_shortduration', 'a few minutes')
self.redis.lpush('misfire_shortduration', 'an hour')
self.redis.lpush('misfire_shortduration', 'a few hours')
self.redis.lpush('misfire_shortduration', 'a day')
self.redis.lpush('misfire_shortduration', 'a few days')
self.redis.lpush('misfire_shortduration', 'a week')

self.redis.lpush('misfire_combatduration', 'a round')
self.redis.lpush('misfire_combatduration', 'two rounds')
self.redis.lpush('misfire_combatduration', 'three rounds')
self.redis.lpush('misfire_combatduration', 'the length of combat')
self.redis.lpush('misfire_combatduration', 'ten minutes')
self.redis.lpush('misfire_combatduration', 'an hour')


# the area center on ___ is covered
# _______ are covered
# 

self.redis.lpush('misfire_target', 'you')
self.redis.lpush('misfire_target', 'a random creature')
self.redis.lpush('misfire_target', 'the original targets')
self.redis.lpush('misfire_target', 'any spectators')
self.redis.lpush('misfire_target', 'allies')
self.redis.lpush('misfire_target', 'enemies')
self.redis.lpush('misfire_target', 'you and your allies')
self.redis.lpush('misfire_target', 'you and your enemies')
self.redis.lpush('misfire_target', 'you, your enemies, and your allies')
        

self.redis.lpush('misfire_growth', 'head')
self.redis.lpush('misfire_growth', 'leg')
self.redis.lpush('misfire_growth', 'finger')
self.redis.lpush('misfire_growth', 'hand')
self.redis.lpush('misfire_growth', 'arm')
self.redis.lpush('misfire_growth', 'foot')
self.redis.lpush('misfire_growth', 'toe')

self.redis.lpush('misfire_instrument', 'flute')
self.redis.lpush('misfire_instrument', 'pan flute')
self.redis.lpush('misfire_instrument', 'bongo')
self.redis.lpush('misfire_instrument', 'bagpipe')
self.redis.lpush('misfire_instrument', 'trumpet')

        
self.redis.lpush('misfire_coinmetal', 'platinum')
self.redis.lpush('misfire_coinmetal', 'gold')
self.redis.lpush('misfire_coinmetal', 'electrum')
self.redis.lpush('misfire_coinmetal', 'silver')
self.redis.lpush('misfire_coinmetal', 'copper')

self.redis.lpush('misfire_metal', 'gold')
self.redis.lpush('misfire_metal', 'steel')
self.redis.lpush('misfire_metal', 'lead')
self.redis.lpush('misfire_metal', 'iron')
self.redis.lpush('misfire_metal', 'copper')
self.redis.lpush('misfire_metal', 'tin')
self.redis.lpush('misfire_metal', 'brass')
self.redis.lpush('misfire_metal', 'aluminum')

self.redis.lpush('misfire_smallanimal', 'piglet')
self.redis.lpush('misfire_smallanimal', 'hamster')
self.redis.lpush('misfire_smallanimal', 'mouse')
self.redis.lpush('misfire_smallanimal', 'kitten')
self.redis.lpush('misfire_smallanimal', 'ferret')
self.redis.lpush('misfire_smallanimal', 'sparrow')
self.redis.lpush('misfire_smallanimal', 'iguana')
self.redis.lpush('misfire_smallanimal', 'cat')
self.redis.lpush('misfire_smallanimal', 'snail')

self.redis.lpush('misfire_largeanimal', 'horse')
self.redis.lpush('misfire_largeanimal', 'elephant')
self.redis.lpush('misfire_largeanimal', 'camel')
self.redis.lpush('misfire_largeanimal', 'cow')
self.redis.lpush('misfire_largeanimal', 'peacock')
self.redis.lpush('misfire_largeanimal', 'large snake')
self.redis.lpush('misfire_largeanimal', 'skunk')
self.redis.lpush('misfire_largeanimal', 'large rabbit')
self.redis.lpush('misfire_largeanimal', 'eagle')
self.redis.lpush('misfire_largeanimal', 'panther')
self.redis.lpush('misfire_largeanimal', 'giant raven')
self.redis.lpush('misfire_largeanimal', 'dire wolf')
self.redis.lpush('misfire_largeanimal', 'giant snail')
self.redis.lpush('misfire_largeanimal', 'moose')
self.redis.lpush('misfire_largeanimal', 'alligator')
self.redis.lpush('misfire_largeanimal', 'hippopotamus')

        
# the dog is ___ towards you

self.redis.lpush('misfire_disposition', 'friendly')
self.redis.lpush('misfire_disposition', 'aggressive')
self.redis.lpush('misfire_disposition', 'suspicious')
self.redis.lpush('misfire_disposition', 'fearful')
self.redis.lpush('misfire_disposition', 'protective')
self.redis.lpush('misfire_disposition', 'vicious')
        

self.redis.lpush('misfire_size', 'tiny')
self.redis.lpush('misfire_size', 'small')
self.redis.lpush('misfire_size', 'normal')
self.redis.lpush('misfire_size', 'large')
self.redis.lpush('misfire_size', 'huge')
self.redis.lpush('misfire_size', 'gigantic')
self.redis.lpush('misfire_size', 'colossal')
        
#the monster appears ____ from you

self.redis.lpush('misfire_distance', 'several centimeters')
self.redis.lpush('misfire_distance', 'a meter')
self.redis.lpush('misfire_distance', 'several meters')
self.redis.lpush('misfire_distance', 'twenty meters')
self.redis.lpush('misfire_distance', 'a hundred meters')
self.redis.lpush('misfire_distance', 'two hundred meters')
self.redis.lpush('misfire_distance', 'a kilometer')
self.redis.lpush('misfire_distance', 'several kilometers')
self.redis.lpush('misfire_distance', 'many kilometers')
        
# the cloud appears ___ of you

self.redis.lpush('misfire_direction', 'north')
self.redis.lpush('misfire_direction', 'south')
self.redis.lpush('misfire_direction', 'east')
self.redis.lpush('misfire_direction', 'west')
self.redis.lpush('misfire_direction', 'underneath')
self.redis.lpush('misfire_direction', 'overhead')
self.redis.lpush('misfire_direction', 'atop')
self.redis.lpush('misfire_direction', 'in front')
self.redis.lpush('misfire_direction', 'to the right')
self.redis.lpush('misfire_direction', 'to the left')
        
#you are hit with a glow ball that does ____ damage

self.redis.lpush('misfire_damagetype', 'fire')
self.redis.lpush('misfire_damagetype', 'acidic')
self.redis.lpush('misfire_damagetype', 'sonic')
self.redis.lpush('misfire_damagetype', 'frost')
self.redis.lpush('misfire_damagetype', 'electrical')
self.redis.lpush('misfire_damagetype', 'elemental')
self.redis.lpush('misfire_damagetype', 'necrotic')
self.redis.lpush('misfire_damagetype', 'holy')
        
# your nose is filled with the scent of ______

self.redis.lpush('misfire_smell', 'smoke')
self.redis.lpush('misfire_smell', 'skunk')
self.redis.lpush('misfire_smell', 'mint')
self.redis.lpush('misfire_smell', 'decomposition')
self.redis.lpush('misfire_smell', 'decay')
self.redis.lpush('misfire_smell', 'citrus')
self.redis.lpush('misfire_smell', 'vomit')
self.redis.lpush('misfire_smell', 'wet dog')
self.redis.lpush('misfire_smell', 'blood')
self.redis.lpush('misfire_smell', 'urine')

self.redis.lpush('misfire_taste', 'acidic')
self.redis.lpush('misfire_taste', 'amazing')
self.redis.lpush('misfire_taste', 'bitter')
self.redis.lpush('misfire_taste', 'bland')
self.redis.lpush('misfire_taste', 'burned')
self.redis.lpush('misfire_taste', 'buttery')
self.redis.lpush('misfire_taste', 'cheesy')
self.redis.lpush('misfire_taste', 'chocolaty')
self.redis.lpush('misfire_taste', 'delicious')
self.redis.lpush('misfire_taste', 'delightful')
self.redis.lpush('misfire_taste', 'divine')
self.redis.lpush('misfire_taste', 'earthy')
self.redis.lpush('misfire_taste', 'excellent')
self.redis.lpush('misfire_taste', 'extraordinary')
self.redis.lpush('misfire_taste', 'fantastic')
self.redis.lpush('misfire_taste', 'fatty')
self.redis.lpush('misfire_taste', 'fiery')
self.redis.lpush('misfire_taste', 'fishy')
self.redis.lpush('misfire_taste', 'flavorful')
self.redis.lpush('misfire_taste', 'fresh')
self.redis.lpush('misfire_taste', 'fried')
self.redis.lpush('misfire_taste', 'fruity')
self.redis.lpush('misfire_taste', 'gamey')
self.redis.lpush('misfire_taste', 'garlicky')
self.redis.lpush('misfire_taste', 'gingery')
self.redis.lpush('misfire_taste', 'greasy')
self.redis.lpush('misfire_taste', 'heavenly')
self.redis.lpush('misfire_taste', 'lemony')
self.redis.lpush('misfire_taste', 'marvelous')
self.redis.lpush('misfire_taste', 'meaty')
self.redis.lpush('misfire_taste', 'mellow')
self.redis.lpush('misfire_taste', 'mild')
self.redis.lpush('misfire_taste', 'minty')
self.redis.lpush('misfire_taste', 'nutty')
self.redis.lpush('misfire_taste', 'oniony')
self.redis.lpush('misfire_taste', 'peppery')
self.redis.lpush('misfire_taste', 'pickled')
self.redis.lpush('misfire_taste', 'plain')
self.redis.lpush('misfire_taste', 'pleasant')
self.redis.lpush('misfire_taste', 'powdery')
self.redis.lpush('misfire_taste', 'rich')
self.redis.lpush('misfire_taste', 'robust')
self.redis.lpush('misfire_taste', 'salty')
self.redis.lpush('misfire_taste', 'satisfying')
self.redis.lpush('misfire_taste', 'savory')
self.redis.lpush('misfire_taste', 'scrumptious')
self.redis.lpush('misfire_taste', 'seasoned')
self.redis.lpush('misfire_taste', 'sharp')
self.redis.lpush('misfire_taste', 'smokey')
self.redis.lpush('misfire_taste', 'soupy')
self.redis.lpush('misfire_taste', 'sour')
self.redis.lpush('misfire_taste', 'spicy')
self.redis.lpush('misfire_taste', 'strong')
self.redis.lpush('misfire_taste', 'sugary')
self.redis.lpush('misfire_taste', 'superb')
self.redis.lpush('misfire_taste', 'sweet')
self.redis.lpush('misfire_taste', 'tangy')
self.redis.lpush('misfire_taste', 'tart')
self.redis.lpush('misfire_taste', 'terrific')
self.redis.lpush('misfire_taste', 'unflavored')
self.redis.lpush('misfire_taste', 'unseasoned')
self.redis.lpush('misfire_taste', 'vinegary')
self.redis.lpush('misfire_taste', 'wonderful')
self.redis.lpush('misfire_taste', 'woody')
self.redis.lpush('misfire_taste', 'yeasty')
self.redis.lpush('misfire_taste', 'zesty')
self.redis.lpush('misfire_taste', 'zingy')
self.redis.lpush('misfire_taste', 'onions')
self.redis.lpush('misfire_taste', 'beer')
self.redis.lpush('misfire_taste', 'horse manure')
self.redis.lpush('misfire_taste', 'garlic')
self.redis.lpush('misfire_taste', 'cabbage')
self.redis.lpush('misfire_taste', 'vanilla')

self.redis.lpush('misfire_radius', '1 meter')
self.redis.lpush('misfire_radius', '3 meter')
self.redis.lpush('misfire_radius', '10 meter')
self.redis.lpush('misfire_radius', '50 meter')
self.redis.lpush('misfire_radius', '100 meter')
self.redis.lpush('misfire_radius', '500 meter')
self.redis.lpush('misfire_radius', '1000 meter')

        
self.redis.lpush('misfire_color', 'red')
self.redis.lpush('misfire_color', 'purple')
self.redis.lpush('misfire_color', 'orange')
self.redis.lpush('misfire_color', 'blue')
self.redis.lpush('misfire_color', 'green')
self.redis.lpush('misfire_color', 'black')
self.redis.lpush('misfire_color', 'gold')

self.redis.lpush('misfire_multiplier', '0.01x')
self.redis.lpush('misfire_multiplier', '0.1x')
self.redis.lpush('misfire_multiplier', '0.5x')
self.redis.lpush('misfire_multiplier', '1.5x')
self.redis.lpush('misfire_multiplier', '2.0x')
self.redis.lpush('misfire_multiplier', '5x')

self.redis.lpush('misfire_suffers', 'irritable bowel syndrome')
self.redis.lpush('misfire_suffers', 'partial blindness')
self.redis.lpush('misfire_suffers', 'partial deafness')
self.redis.lpush('misfire_suffers', 'intermittent dementia')
self.redis.lpush('misfire_suffers', 'intermittent delusions')
self.redis.lpush('misfire_suffers', 'paralyzation')
self.redis.lpush('misfire_suffers', 'muteness')
self.redis.lpush('misfire_suffers', 'memory loss')
self.redis.lpush('misfire_suffers', 'color blindness')

self.redis.lpush('misfire_spelleffect', 'Plant Growth')
self.redis.lpush('misfire_spelleffect', 'Fireball')
self.redis.lpush('misfire_spelleffect', 'Vacuum')
self.redis.lpush('misfire_spelleffect', 'Stun Cloud')
self.redis.lpush('misfire_spelleffect', 'Gravitational Well')
self.redis.lpush('misfire_spelleffect', 'Stink Cloud')
self.redis.lpush('misfire_spelleffect', 'Fog')
self.redis.lpush('misfire_spelleffect', 'Invisibility')
self.redis.lpush('misfire_spelleffect', 'Silence')
self.redis.lpush('misfire_spelleffect', 'Darkness')
self.redis.lpush('misfire_spelleffect', 'Hold Person')
self.redis.lpush('misfire_spelleffect', 'Fireball Illusion')
self.redis.lpush('misfire_spelleffect', 'Chain Lightning')

self.redis.lpush('misfire_plants', 'palm trees')
self.redis.lpush('misfire_plants', 'oak trees')
self.redis.lpush('misfire_plants', 'cherry trees')
self.redis.lpush('misfire_plants', 'willow trees')

self.redis.lpush('misfire_liquid', 'water')
self.redis.lpush('misfire_liquid', 'urine')
self.redis.lpush('misfire_liquid', 'wine')
self.redis.lpush('misfire_liquid', 'beer')
self.redis.lpush('misfire_liquid', 'fresh milk')
self.redis.lpush('misfire_liquid', 'rancid milk')
self.redis.lpush('misfire_liquid', 'syrup')

self.redis.lpush('misfire_soundvolume', 'quiet')
self.redis.lpush('misfire_soundvolume', 'barely audible')
self.redis.lpush('misfire_soundvolume', 'deafening')
self.redis.lpush('misfire_soundvolume', 'loud')

self.redis.lpush('misfire_soundeffect', 'thunderclap')
self.redis.lpush('misfire_soundeffect', 'buzz')
self.redis.lpush('misfire_soundeffect', 'zap')
self.redis.lpush('misfire_soundeffect', 'bell')
self.redis.lpush('misfire_soundeffect', 'gong')
self.redis.lpush('misfire_soundeffect', 'crash')
self.redis.lpush('misfire_soundeffect', 'shriek')
self.redis.lpush('misfire_soundeffect', 'bang')
self.redis.lpush('misfire_soundeffect', 'poof')


self.redis.lpush('misfire_location', 'desert')
self.redis.lpush('misfire_location', 'desert oasis')
self.redis.lpush('misfire_location', 'jungle')
self.redis.lpush('misfire_location', 'deep lake')
self.redis.lpush('misfire_location', 'shallow pond')
# target = The Caster, The Target, Allies, All Enemies

self.redis.lpush('misfire_template', '{{params.target }}\'s skin is now {{params.color}}.')
self.redis.lpush('misfire_template', '{{params.target }} will grow an extra {{params.growth}} which hangs limply and occasionally mimics the movement of other {{params.growth}}s.')
self.redis.lpush('misfire_template', '{{params.target }} are covered with a glowing aura that protects from aggressive magics.')
self.redis.lpush('misfire_template', 'Surprise fireballs! {{params.target |capitalize}} get damage from several {{params.size}} fireballs exploding at once.')
self.redis.lpush('misfire_template', 'You summon forth a {{params.size}} {{params.color}} {{params.largeanimal}} that is {{params.disposition}} towards {{params.target}}.')
self.redis.lpush('misfire_template', '{{params.target }} contract uncontrollable, loud hiccups that prevent stealth or concentration.')
self.redis.lpush('misfire_template', 'The magic affects everyone within a {{params.radius}} radius except the intended target.')
self.redis.lpush('misfire_template', 'A horrible taste overcomes {{params.target}}. They have a 25% chance of throwing up.')
self.redis.lpush('misfire_template', 'An {{params.size}} {{params.largeanimal}} suddenly appears in front of you, explains that he\'s very sorry he didn\'t show up earlier and wanders off humming.')
self.redis.lpush('misfire_template', 'In a {{params.radius}} radius centered on {{params.target}}, snow begins to fall, and will follow {{params.target}} indoors and out.')
self.redis.lpush('misfire_template', 'The spell hits with reduced intensity.')
self.redis.lpush('misfire_template', 'The spell hits with enhanced intensity.')
self.redis.lpush('misfire_template', '{{params.target}} suddenly suffer from acute, powerful and unique body odor that smells of {{params.smell}}. While not putrid, it is not pleasant.')
self.redis.lpush('misfire_template', 'A {{params.size}} cloud of thick smoke appears {{params.distance}} {{params.direction}} of you.')
self.redis.lpush('misfire_template', '{{params.target}} start to froth at the mouth uncontrollably and prolifically.')
self.redis.lpush('misfire_template', '{{params.target}} suffer a {{params.size}} amount of {{params.damagetype}} damage.')

self.redis.lpush('misfire_template', 'A loud Gong sounds.')
self.redis.lpush('misfire_template', 'A strong {{params.taste}} taste affects {{params.target}}.')
self.redis.lpush('misfire_template', 'A swarm of vicious rats surround {{params.target}} and attack after a few moments of confusion.')
self.redis.lpush('misfire_template', 'Create food and water.')
self.redis.lpush('misfire_template', '{{params.target}} becomes hastened {{params.combatduration}}.')
self.redis.lpush('misfire_template', '{{params.target}} emits the scent of a dangerous predator for the next hour.  Domestic animals become hostile.')
self.redis.lpush('misfire_template', '{{params.target}} Enlarged.')
self.redis.lpush('misfire_template', '{{params.target}} grow a pair of small horns (2 in each) on the forehead, which contrasts with skin color.  A remove curse may remove them.')
self.redis.lpush('misfire_template', '{{params.target}} grows via an enlarged spell.')
self.redis.lpush('misfire_template', '{{params.target}} hastened.')
self.redis.lpush('misfire_template', '{{params.target}} thirst is quenched for {{params.duration}}.  No ill effects from dehydration.')
self.redis.lpush('misfire_template', '{{params.target}} turns to stone for {{params.duration}}')
self.redis.lpush('misfire_template', 'Spell fails')
self.redis.lpush('misfire_template', 'Spell is delayed for {{params.combatduration}} and has half the effect.')
self.redis.lpush('misfire_template', 'Spell simply fails')

self.redis.lpush('misfire_template', 'A faeries dance affects {{params.target}} for {{params.combatduration}}.')

self.redis.lpush('misfire_template', '{{params.target}} emit the scent of a dangerous predator for the next hour.  Domestic animals become hostile.')
self.redis.lpush('misfire_template', 'Absolutely nothing happens (time is stopped {{params.duration}}).')
self.redis.lpush('misfire_template', 'A swarm of viscious rats surround {{params.target}} and attack after a few moments of confusion.')
self.redis.lpush('misfire_template', '{{params.target}} thirst is quenched for {{params.duration}}.  No ill effects from dehydration.')
self.redis.lpush('misfire_template', 'Spell is delayed for {{params.duration}} and has half the effect.')
self.redis.lpush('misfire_template', 'Spell simply fails')
self.redis.lpush('misfire_template', '{{params.target}} grow via an enlarged spell.')
self.redis.lpush('misfire_template', '{{params.target}} become hastened {{params.duration}}.')
self.redis.lpush('misfire_template', '{{params.target}} turn to stone for {{params.duration}}')

self.redis.lpush('misfire_template', '{{params.target}} age 1d20 years.')
self.redis.lpush('misfire_template', '{{params.target}} uncontrollably strip.')
self.redis.lpush('misfire_template', '{{params.target}} suffer {{params.suffers}} for {{params.duration}}')
self.redis.lpush('misfire_template', '{{params.target}} grow an extra thumb.')
self.redis.lpush('misfire_template', '{{params.target}} spin 180 degrees')
self.redis.lpush('misfire_template', '{{params.target}} grow 1d10 years older')
self.redis.lpush('misfire_template', 'A light aria fills the air.')
self.redis.lpush('misfire_template', '{{params.target}} grow 1d10 years younger')
self.redis.lpush('misfire_template', '{{params.spelleffect}} centered on {{params.target}} with a {{params.radius}} radius.')
self.redis.lpush('misfire_template', 'Wall of Fire encircles {{params.target}}.')
self.redis.lpush('misfire_template', '{{params.target}} become extremely drunk.')
self.redis.lpush('misfire_template', '{{params.target}} find a dagger in a boot.')
self.redis.lpush('misfire_template', 'All gold on {{params.target}} turns to lead.')
self.redis.lpush('misfire_template', 'Death himself comes to claim {{params.target}}.')
self.redis.lpush('misfire_template', '{{params.target}} forget the last 24 hours.')
self.redis.lpush('misfire_template', '{{params.target}} glow as per a light spell for {{params.duration}}.')
self.redis.lpush('misfire_template', '{{params.target}} change sex for {{params.duration}}.')
self.redis.lpush('misfire_template', '{{params.target}} now possess {{params.smallanimal|article}}.')
self.redis.lpush('misfire_template', '{{params.target}} set the nearest forest ablaze.')
self.redis.lpush('misfire_template', '2d20 {{params.plants}} grow up around {{params.target}}.')
self.redis.lpush('misfire_template', 'Skin turns pale {{params.color}} for 2d6 months')
self.redis.lpush('misfire_template', 'Spell effectiveness {{params.multiplier}}')
self.redis.lpush('misfire_template', '{{params.target}} take 5d10 hit points of {{params.damagetype}} damage')
self.redis.lpush('misfire_template', '{{params.target}} turn ethereal for 2d4 rounds')
self.redis.lpush('misfire_template', 'Overwhelming fear strikes {{params.target}}. It lasts {{params.duration}}.')
self.redis.lpush('misfire_template', '{{params.target}} forget how to read for 3d4 days.')
self.redis.lpush('misfire_template', '{{params.target}} permanently grow a pointed chin.')
self.redis.lpush('misfire_template', '200 gallons of {{params.liquid}} soak {{params.target}}.')
self.redis.lpush('misfire_template', 'A {{params.largeanimal}} walks by ignoring {{params.target}}.')
self.redis.lpush('misfire_template', 'A {{params.soundvolume}} {{params.soundeffect}} is heard. No other effect.')
self.redis.lpush('misfire_template', '{{params.target}} are healed of 10 HP if wounded.')
self.redis.lpush('misfire_template', '{{params.target}} get a random disease.')
self.redis.lpush('misfire_template', '{{params.target}} metamorphosis into a {{params.largeanimal}} for {{params.combatduration}}.')
self.redis.lpush('misfire_template', 'Spell has only 1/4 effect and duration')
self.redis.lpush('misfire_template', 'Spell reversed if reverse is possible.')

self.redis.lpush('misfire_template', '{{params.target}} are charmed as per charm monster')
self.redis.lpush('misfire_template', '{{params.target}} are imprisoned on another plane.')
self.redis.lpush('misfire_template', 'A desert oasis grows around {{params.target}}.')
self.redis.lpush('misfire_template', 'Burst of fireworks explode from {{params.target}} (harmless but loud and visible).')

self.redis.lpush('misfire_template', '{{params.target}} are in great pain for {{params.combatduration}}.')
self.redis.lpush('misfire_template', '{{params.target}} need no sleep for {{params.coduration}}.')
self.redis.lpush('misfire_template', '{{params.largeanimal|article|capitalize}} appears and considers itself to be your pet.')

self.redis.lpush('misfire_template', '{{params.largeanimal|article|capitalize}} appears and is {{params.disposition}} towards {{params.target}}.')
self.redis.lpush('misfire_template', 'A skunk is conjured and sprays {{params.target}}.')

self.redis.lpush('misfire_template', 'A {{disposition}} prostitute turns up from nowhere and demands payment for services rendered.')
self.redis.lpush('misfire_template', 'A {{params.color}} Djinn materializes in front of you. It says nothing.')
self.redis.lpush('misfire_template', 'A stream of {{params.liquid}} shoots from the caster\'s fingertips countinuously for {{params.combatduration}}.')
self.redis.lpush('misfire_template', 'The surrounding area {{params.distance}}  is turned into {{params.location}}.')
self.redis.lpush('misfire_template', 'a 10 foot diamter circle of caltrops surround {{params.target}}.')
self.redis.lpush('misfire_template', 'A rift is opened revealing a Banshee, which appears by {{params.target}} and Wails before disappearing.')
self.redis.lpush('misfire_template', 'A desert oasis grows around the {{params.target}}.')
self.redis.lpush('misfire_template', 'All food and rations within 50 feet spoils and becomes poisonous. ')
self.redis.lpush('misfire_template', 'All nonmagical metal on the {{params.target}} turns into balsawood (including armor, weapons and equipment).')
self.redis.lpush('misfire_template', 'A minor air elemental offers you its help for {{params.target}}. (usefulness decreases with longer durations).')
self.redis.lpush('misfire_template', 'A passing butterfly tells {{params.target}} who the betrayer really is.')

self.redis.lpush('misfire_template', 'A raven decides to follow you and be helpful for {{params.duration}}.')
self.redis.lpush('misfire_template', 'A stinking cloud centers on the {{params.target}}.')
self.redis.lpush('misfire_template', 'An explosion of fireworks erupts above, and can be seen and heard for miles.')
self.redis.lpush('misfire_template', '{{params.target}} lose color vision in exchange for x-ray vision for {{params.duration}}.')
self.redis.lpush('misfire_template', 'Caster is in great incapacitating pain for {{params.combatduration}}.')
self.redis.lpush('misfire_template', '{{params.target}} is Mute for the next {{params.combatduration}}.')
self.redis.lpush('misfire_template', '{{params.target}} become color blind for {{params.duration}}.')
self.redis.lpush('misfire_template', '{{params.target}} forgets identity and motivation for {{params.combatduration}}.')
self.redis.lpush('misfire_template', '{{params.target}} glows bright {{params.color}} for {{params.duration}}.')
self.redis.lpush('misfire_template', '{{params.target}} grow a 2 foot long beard (that will continuously regrow if shaven) for {{params.duration}} . ')
self.redis.lpush('misfire_template', '{{params.target}} is safely displaced {{params.radius}} {{params.direction}} of it\'s current position.')

self.redis.lpush('misfire_template', '{{params.target}} is imprisoned on another plane for {{params.combatduration}}.')
self.redis.lpush('misfire_template', '{{params.target}} speak in reverse sentences for {{params.combatduration}}.')
self.redis.lpush('misfire_template', '{{params.target}} skin turns {{params.color}}.')
self.redis.lpush('misfire_template', 'Summon lesser demon (DM\'s discretion.)')
self.redis.lpush('misfire_template', 'The intended spell functions as intended.')
self.redis.lpush('misfire_template', 'Caster is affected by a Hold Person spell.')
self.redis.lpush('misfire_template', 'Caster is temporarily blinded for {{params.combatduration}}')
self.redis.lpush('misfire_template', 'Four goblins appear and begin beating the caster with socks full of copper coins (improvised weapon)')
self.redis.lpush('misfire_template', 'Silence, {{params.radius}} radius centered on {{params.target}} for {{params.combatduration}}')
self.redis.lpush('misfire_template', 'Spell goes off normally, no extra effects.')
self.redis.lpush('misfire_template', '{{params.target}} shot with 1d10 darts (1d4 dam each)')
self.redis.lpush('misfire_template', 'A giant sock appears in the mouth of {{params.target}}')
self.redis.lpush('misfire_template', 'A watermelon appears at the feet of {{params.target}}.')
self.redis.lpush('misfire_template', '{{params.target}} is affected by Invisibility, normal.')
self.redis.lpush('misfire_template', 'The caster learns the name of the profession of {{params.target}}.')
self.redis.lpush('misfire_template', 'The clothes on {{params.target}} itch unbearably, affecting initiative, concentration, and dexterity.')
self.redis.lpush('misfire_template', 'The caster suffers same spell effect as {{params.target}}.')
self.redis.lpush('misfire_template', 'The caster and {{params.target}} exchange current HP total for {{params.duration}}')
self.redis.lpush('misfire_template', 'Normal fire springs up at the feet of{{params.target}}.')
self.redis.lpush('misfire_template', '{{params.target}} has an insatiable craving for {{params.craving}}.')
self.redis.lpush('misfire_template', '{{params.target}} affected by True Sight for {{params.combatduration}}.')
self.redis.lpush('misfire_template', 'The caster is teleported directly behind {{params.target}}.')
self.redis.lpush('misfire_template', 'The caster amuses the gods and gets one casting of any desired spell.')
self.redis.lpush('misfire_template', 'Weight increased by {{params.multiplier}} for {{params.duration}}')
self.redis.lpush('misfire_template', 'Any nearby plants insist that {{params.target}} play a game of chess.')

self.redis.lpush('misfire_template', 'An empty log cabin pops up next to the {{params.target}}.')
self.redis.lpush('misfire_template', 'A Wall of Force appears in front of the {{params.target}}')
self.redis.lpush('misfire_template', '{{params.target}} is affected by Confusion, as the spell.')
self.redis.lpush('misfire_template', '{{params.target}}\'s face is blackened by small explosion.')
self.redis.lpush('misfire_template', '{{params.target}} smells like {{params.smell}} for spell duration.')
self.redis.lpush('misfire_template', '{{params.target}} speaks in a squeaky voice for {{params.duration}}.')
self.redis.lpush('misfire_template', '{{params.target}} summons {{params.disposition|article}} {{params.smallanimal}}.')
self.redis.lpush('misfire_template', '{{params.target}}\'s weapons disappear and are replaced with a scythe.')
self.redis.lpush('misfire_template', 'A phantom footman turns up and offers his help.')
self.redis.lpush('misfire_template', 'A sketch of {{params.target}} falls to the ground beside you.')
self.redis.lpush('misfire_template', '{{params.target}} automatically succeeds on the next roll.')
self.redis.lpush('misfire_template', '{{params.target}} instantly coated in unlit flammable oil.')
self.redis.lpush('misfire_template', '{{params.target}} is struck by an invisible fist (unarmed attack) in the back of the head.')
self.redis.lpush('misfire_template', 'a key falls to the ground in front of {{params.target}}.')
self.redis.lpush('misfire_template', '{{params.target}} hair is coated in {{params.coating}}.')
self.redis.lpush('misfire_template', 'A peach tree starts growing in one of your bags. Grows to full size in {{params.combatduration}}.')

self.redis.lpush('misfire_template', '{{params.target}} levitates 20 feet for {{params.combatduration}}, then falls slowly.')
self.redis.lpush('misfire_template', '{{params.target}} reduces (reversed enlarge) for {{params.combatduration}}.')
self.redis.lpush('misfire_template', 'The caster\'s next spell cast at 1st level in effect.')
self.redis.lpush('misfire_template', 'Spells are reflected from {{params.target}} for {{params.combatduration}}.')
self.redis.lpush('misfire_template', '{{params.target}}\'s clothing and armour fall to the ground, tied in knots.')
self.redis.lpush('misfire_template', 'Coloured streamers pour from the caster\'s fingertips.')
self.redis.lpush('misfire_template', '{{params.target}} turns {{params.color}}. (cancelled by dispel magic)')
self.redis.lpush('misfire_template', '{{params.target}} speaks like Hans and Frans for {{params.combatduration}}.')
self.redis.lpush('misfire_template', 'The eyes on {{params.target}} permanently turn wine red. (Iris only.)')
self.redis.lpush('misfire_template', 'All lead in the {{params.target}}\'s possession turns to gold.')

self.redis.lpush('misfire_template', '{{params.target}} is tied down with magically appearing hemp rope.')
self.redis.lpush('misfire_template', 'Cream puffs fly from the caster\'s hands toward {{params.target}}.')
self.redis.lpush('misfire_template', 'Height and mass is reduced by 1/2,  lasts {{params.duration}}')

self.redis.lpush('misfire_template', '{{params.target}} is Slowed (opposite of Haste) for {{params.combatduration}}.')
self.redis.lpush('misfire_template', '{{params.target}} catch a very, very bad cold.  Lasts {{params.duration}}.')
self.redis.lpush('misfire_template', '{{params.target}} drop all of your teeth in your upper left jaw.')
self.redis.lpush('misfire_template', 'A large green worm appears and jumps at the {{params.target}}.')
self.redis.lpush('misfire_template', 'A lightning bolt strikes the {{params.target}}.')
self.redis.lpush('misfire_template', 'All gold in the {{params.target}}\'s possession turns to water.')
self.redis.lpush('misfire_template', 'An Imp appears, insults the {{params.target}}, and disappears.')
self.redis.lpush('misfire_template', 'A pack of Orcs selects you to be their next victim, will attack in {{params.duration}}')
self.redis.lpush('misfire_template', 'Disco Inferno! Harmless colourful light beams radiate from {{params.target}}.')
self.redis.lpush('misfire_template', 'A Leprechaun (or other suitable Fae) is summoned. It is {{params.disposition}} towards the caster.')

self.redis.lpush('misfire_template', 'Streams of butterflies pour from the {{params.target}}\'s mouth.')
self.redis.lpush('misfire_template', '{{params.target}} is teleported {{params.distance}} away.')
self.redis.lpush('misfire_template', 'The {{params.target}} forgets the events of the last {{params.combatduration}}')
self.redis.lpush('misfire_template', '2d20 bottle of the finest wine appear at your feet.')
self.redis.lpush('misfire_template', '{{params.target}} speed is doubled for {{params.combatduration}}.')
self.redis.lpush('misfire_template', 'Random plant appears and takes root at the feet {{params.target}}.')
self.redis.lpush('misfire_template', 'The caster becomes a Wraith for {{params.combatduration}}')
self.redis.lpush('misfire_template', 'The area around {{params.target}} becomes uncomfortably hot.')
self.redis.lpush('misfire_template', '3d6 {{params.minions}} rise from the ground to do your bidding for {{params.combatduration}} before disappearing.')
self.redis.lpush('misfire_template', 'A colony of black ants explains its {{params.disposition}} disposition towards you.')
self.redis.lpush('misfire_template', 'All gold in the {{params.target}}\'s possession turns to platinum.')
self.redis.lpush('misfire_template', 'An eternal flame is instantly created where you stand.')

self.redis.lpush('misfire_template', '{{params.target}} falls prone.')
self.redis.lpush('misfire_template', 'All plants in a 20\'radius around {{params.target}} wither and die.')
self.redis.lpush('misfire_template', 'All weapons within {{params.radius}} of {{params.target}} glow for {{params.combatduration}}.')
self.redis.lpush('misfire_template', 'A raving specter starts terrorizing {{params.target}}.')
self.redis.lpush('misfire_template', '{{params.target}} grow webbed hands and feet for {{params.combatduration}}.')
self.redis.lpush('misfire_template', '{{params.target}} instantly triple your spells/day.  Lasts {{params.combatduration}}.')
self.redis.lpush('misfire_template', 'A simple black felt hat appears on {{params.target}}\'s head.')
self.redis.lpush('misfire_template', 'All fluid in containers on {{params.target}} turn to deadly poison.')
self.redis.lpush('misfire_template', 'A major earth elemental decides you are too dangerous to live.')
self.redis.lpush('misfire_template', '{{params.target}} becomes invulnerable to edged weapons for 1 hour.')
self.redis.lpush('misfire_template', 'The ground opens up and swallows the {{params.target}} to the neck.')
self.redis.lpush('misfire_template', 'The {{params.target}} gains Regeneration at the rate of 1 HP/round for {{params.combatduration}}.')
self.redis.lpush('misfire_template', '1d4 rotten tomatoes hit {{params.target}} (effect at DM discretion).')

self.redis.lpush('misfire_template', 'All creatures within 30 ft of the {{params.target}} begin to hiccup.')
self.redis.lpush('misfire_template', 'For the next 5 minutes, the {{params.target}} says everything twice.')
self.redis.lpush('misfire_template', 'Spell effectiveness (range, duration, etc,) decreases 50%')
self.redis.lpush('misfire_template', '{{params.target}} gains magic resistance for {{params.combatduration}}.')
self.redis.lpush('misfire_template', 'The ground beneath the {{params.target}} becomes slippery as if icy.')
self.redis.lpush('misfire_template', '{{params.target}} hair grows an inch per turn for the next {{params.combatduration}}.')
self.redis.lpush('misfire_template', 'A random person within {{params.radius}} of you becomes invisible.')

self.redis.lpush('misfire_template', '{{params.target}} turn ethereal for {{params.combatduration}}.')
self.redis.lpush('misfire_template', '{{params.target}} is cured of 5d10 hit points (up to normal maximum).')
self.redis.lpush('misfire_template', 'The {{params.target}} speaks with a lisp until the effects wear off. ')
self.redis.lpush('misfire_template', 'All magical items within {{params.radius}} of {{params.target}} glow for {{params.duration}}.')
self.redis.lpush('misfire_template', 'All normal fires within {{params.radius}} of the {{params.target}} are extinguished.')
self.redis.lpush('misfire_template', 'Cone of Cold directed at {{params.target}}. Brrrrr.')
self.redis.lpush('misfire_template', 'A rainbow appears over this location for {{params.duration}}.')
self.redis.lpush('misfire_template', '{{params.target}} is healed of all non-fatal damage incurred thus far.')
self.redis.lpush('misfire_template', 'Everything you touch not in currently in your possession for the next {{params.combatduration}} starts to burn.')

self.redis.lpush('misfire_template', 'For the next {{params.duration}}, all of {{params.target}}\'s rolls are at -5.')
self.redis.lpush('misfire_template', 'One member of the {{params.target}}\'s party is Blinded for {{params.duration}}.')
self.redis.lpush('misfire_template', 'One randomly chosen magic item has its enchantment changed.')
self.redis.lpush('misfire_template', 'Spell functions normally, but also shrieks like a shrieker.')
self.redis.lpush('misfire_template', '{{params.target}}\'s weapons jump off him and bounce away out of reach for {{params.combatduration}}')
self.redis.lpush('misfire_template', 'The intended spell backfires on the caster for good or ill.')
self.redis.lpush('misfire_template', 'The next 10 meals the {{params.target}} eats will taste like cow dung.')
self.redis.lpush('misfire_template', '{{params.target}} somehow become a {{params.largeanimal}} for {{params.shortduration}}.  But you can speak.')
self.redis.lpush('misfire_template', 'A Jinn appears and asks you to make a wish. It may be a cursed wish, a trick, or an outright lie.')

self.redis.lpush('misfire_template', 'All magical fires within 40\' of the {{params.target}} are extinguished.')
self.redis.lpush('misfire_template', 'Any darkvision possessed by {{params.target}} is nullified for {{params.shortduration}}.')
self.redis.lpush('misfire_template', '{{params.target}} are disarmed and weapons are flung 10 feet away.')
self.redis.lpush('misfire_template', 'A reversed tongues affects all within {{params.radius}} of the {{params.target}}.')
self.redis.lpush('misfire_template', 'A ring of mushrooms appears around {{params.target}} (no other effect).')
self.redis.lpush('misfire_template', 'The caster is paralyzed for {{params.combatduration}} but makes a full recovery.')
self.redis.lpush('misfire_template', 'a 10x10x10 cube of ground beneath {{params.target}} vanishes, causing them to fall.')
self.redis.lpush('misfire_template', '1d4 skeletons rise from their graves to tear {{params.target}} apart.')
self.redis.lpush('misfire_template', '1d6 raw eggs hit {{params.target}} from above (effect at DM discretion).')

self.redis.lpush('misfire_template', 'A 20 foot log wall of fire sweeps ahead of you for {{params.distance}}, passing through any solid barriers.')
self.redis.lpush('misfire_template', '{{params.target}} is teleported home. Normal teleport error rules apply.')
self.redis.lpush('misfire_template', 'Tip of {{params.target}}\'s nose glows red for a second. No other effect.')
self.redis.lpush('misfire_template', '{{params.target}}\'s {{params.growth}} grows to 10 times its normal size for {{params.combatduration}}.')
self.redis.lpush('misfire_template', 'A potion pops into existence in front of you (DM choice on contents)')
self.redis.lpush('misfire_template', '{{params.target}} and {{params.target}} exchange voices.')
self.redis.lpush('misfire_template', 'The caster breathes fire as a small dragon for one breath only.')
self.redis.lpush('misfire_template', 'No gravity in a {{params.radius}} radius around {{params.target}} for {{params.shortduration}}.')
self.redis.lpush('misfire_template', 'The {{params.target}} belches once with the same effect as a thunderstone.')

self.redis.lpush('misfire_template', 'All water within 60\' of {{params.target}} turns to fine Elvin wine. Cheers!')
self.redis.lpush('misfire_template', '{{params.target}}\'s next spell is cast as though it is a level higher.')
self.redis.lpush('misfire_template', 'The shield closest to the {{params.target}} is turned into a flower basket.')
self.redis.lpush('misfire_template', 'A levitation spell is mistakenly laid on {{params.target}}, lasting {{params.combatduration}}')
self.redis.lpush('misfire_template', '{{params.target}} are chained to ground; chains are near impossible to break.')
self.redis.lpush('misfire_template', '{{params.target}} is struck by a random curse. {{params.wissave}}')
self.redis.lpush('misfire_template', '{{params.target}}\'s next spell is cast at 1d4 levels lower in effectiveness if possible.')
self.redis.lpush('misfire_template', '{{params.target}} has a small, black rain cloud form 3 feet over their head. It follows them for {{params.duration}}')
self.redis.lpush('misfire_template', 'The next stranger you talk to will mistake you for an old friend.')

self.redis.lpush('misfire_template', '{{params.target}}\'s clothing and equipment turn invisible for {{params.combatduration}}. Very embarrassing.')
self.redis.lpush('misfire_template', 'Next successful attack on {{params.target}} heals instead of harms.')
self.redis.lpush('misfire_template', '{{params.target}} becomes dizzy for {{params.combatduration}}.')
self.redis.lpush('misfire_template', '2d6 chickens appear at the {{params.target}}\'s feet and run away at top speed.')
self.redis.lpush('misfire_template', 'A Lesser Air Elemental is summoned and promptly attacks the {{params.target}}.')
self.redis.lpush('misfire_template', 'All non-magical glass or crystal within 30 feet of {{params.target}} shatters.')
self.redis.lpush('misfire_template', 'A poisonous spider (DM choice) appears near the {{params.target}} and attacks.')
self.redis.lpush('misfire_template', '{{params.target}} Forgets all spells for {{params.combatduration}}. Items still function.')
self.redis.lpush('misfire_template', 'Everyone in {{params.target}}\'s view feels cold for {{params.shortduration}}. No other effect.')
self.redis.lpush('misfire_template', 'Smoke trickles from the ears of the {{params.target}} for {{params.duration}}.  Harmless.')
self.redis.lpush('misfire_template', '{{params.target}} go berserk for {{params.combatduration}}, lashing out at anyone within 13 ft.')

self.redis.lpush('misfire_template', '{{params.target}} falls madly in love with {{params.target}}.')
self.redis.lpush('misfire_template', '{{params.target}}\'s skin turns to steel, providing physical damage resistance for {{params.combatduration}}')
self.redis.lpush('misfire_template', 'Everything the {{params.target}} touches is stained {{params.color}} for {{params.shortduration}}.')
self.redis.lpush('misfire_template', '{{params.target}}\'s next action automatically fumbles as though he rolled a 1.')
self.redis.lpush('misfire_template', 'The {{params.target}} gains low-light vision for {{params.combatduration}}.')
self.redis.lpush('misfire_template', 'a Greater Heal, healing all but 1d4 points of damage, affects {{params.target}}.')
self.redis.lpush('misfire_template', 'All visible areas of cloudy skies clears, and clear skies cloud over.')
self.redis.lpush('misfire_template', 'Spell functions normally, any applicable saving throw fails.')
self.redis.lpush('misfire_template', 'Spell must run full duration; the caster cannot cancel the spell at will.')
self.redis.lpush('misfire_template', 'Stone to Flesh on 1d100 pounds of rock within 100 feet of {{params.target}}.')
self.redis.lpush('misfire_template', '{{params.flowers}} start growing from your {{params.growth}}.  They fall off after {{params.shortduration}}.')
self.redis.lpush('misfire_template', 'Spell Hold Person affects all creatures for {{params.combatduration}}. Creatures can still speak normally.')
self.redis.lpush('misfire_template', 'The {{params.target}}\'s weight decreases by 1/4th for {{params.duration}}.')
self.redis.lpush('misfire_template', 'A {{params.instrument}}-playing {{params.minion}} accompanies you for {{params.duration}}.')
self.redis.lpush('misfire_template', 'The caster opens a rift to another plane, which sucks in the enemies and closes.')

self.redis.lpush('misfire_template', 'Rope appears around {{params.target}} (completely restraining).')
self.redis.lpush('misfire_template', 'The {{params.target}} grows small wings on their temples and can fly. They will whither and fall off in {{params.shortduration}}.')
self.redis.lpush('misfire_template', 'a random mundane item appears.')
self.redis.lpush('misfire_template', '{{params.target}} forgets a language of their choice and learns {{params.language}}.')
self.redis.lpush('misfire_template', 'A portal opens unleashing a carriage at full speed, which tramples {{params.target}}. The driver is confused.')
self.redis.lpush('misfire_template', 'Beer suds flow from the mouth of {{params.target}} for {{params.combatduration}}, inhibiting speech.')
self.redis.lpush('misfire_template', '{{params.target}} is encased in lime gellatin one size larger than the target.')
self.redis.lpush('misfire_template', 'A portal betweeen you and your target, allowing melee attacks despite distance. Lasts {{params.combatduration}}.')
self.redis.lpush('misfire_template', 'Lightning strikes the tallest creature in your vicinity.')
self.redis.lpush('misfire_template', 'Lightning strikes the shortest creature in your vicinity.')

self.redis.lpush('misfire_template', 'An energy bolt explodes from one ear and hits the nearest object/person.')
self.redis.lpush('misfire_template', '{{params.target}} are suddenly fluent in {{params.language}} and craves the taste of {{params.craving}}.')
self.redis.lpush('misfire_template', 'Area within {{params.radius}} of {{params.target}} becomes a null magic zone.')
self.redis.lpush('misfire_template', '{{params.target}} develops a phobia.')
self.redis.lpush('misfire_template', 'A random creature in the area turns to wood and explodes into 30 parts. If not reassembled in {{params.shortduration}}, it will result in death.')
self.redis.lpush('misfire_template', '{{params.target}} finds their mouth filled with 30 {{params.coinmetal}} coins.')
self.redis.lpush('misfire_template', 'All copper pieces within 30 feet of {{params.target}} are changed into {{params.coinmetal}} pieces, and vice versa.')
self.redis.lpush('misfire_template', 'your head shrinks by 30% (otherwise harmless).')

self.redis.lpush('misfire_template', 'A small hamster on your head and tries to claw your eyes.')
self.redis.lpush('misfire_template', 'A mundane item possed by {{params.target}} becomes magical (DM discretion).')
self.redis.lpush('misfire_template', 'Fear engulfs {{params.target}} for {{params.combatduration}}')
self.redis.lpush('misfire_template', 'Your opponent dies instantly.')
self.redis.lpush('misfire_template', 'The intended spell functions with a flashy lightshow and sounds to boot.')
self.redis.lpush('misfire_template', 'A forest of appropriate plants sprout to life {{params.radius}} around you, creating difficult terrain.')
self.redis.lpush('misfire_template', 'A forest of inappropriate plants sprout to life {{params.radius}} around you, creating difficult terrain.')

self.redis.lpush('misfire_template', 'All creatures in a {{params.radius}} radius currently hostile to the caster are duplicated (including possessions).')
self.redis.lpush('misfire_template', 'a single possession on {{params.target}} becomes sentient with the personality of a random NPC. ')
self.redis.lpush('misfire_template', 'Caster drains the lifeforce from a single random enemy and distributes it to the team. any remaining lifeforce is kept by caster as temp HP.')
self.redis.lpush('misfire_template', 'The caster learns the history of a random item in their possession.')
self.redis.lpush('misfire_template', 'The caster gains an unimpressed personal narrator that can be heard by anyone in a 30 foot radius.')
self.redis.lpush('misfire_template', 'The caster and target are imprisoned in a 20x20 foot impenetrable box. The box will disappear when one of them is dead.')
self.redis.lpush('misfire_template', 'The caster sees a vision of the future which may or may not be true.')
self.redis.lpush('misfire_template', '{{params.target}} appear on a reward poster that appears in front of the caster with a substantial reward for capture.')


self.redis.lpush('misfire_template', '{{params.target}} are knocked prone. Twice.')
self.redis.lpush('misfire_template', 'A random spell of the same level affects {{params.target}} instead.')
self.redis.lpush('misfire_template', '{{params.target}} loses all teeth.')
self.redis.lpush('misfire_template', '{{params.target}} bursts into flames, taking {{params.damagetype}} damage until the flames are extinguished.')
self.redis.lpush('misfire_template', '{{params.target}} begins to recite poetry for {{params.combatduration}}.')
self.redis.lpush('misfire_template', '{{params.target}} will rise as a fresh zombie when killed and attack their allies.')
self.redis.lpush('misfire_template', 'a demonic tax collector appears and demands 10% of their earnings for services rendered.')
self.redis.lpush('misfire_template', 'The caster disappears and reappears after {{params.combatduration}}.')
self.redis.lpush('misfire_template', 'The spell is delayed {{params.shortduration}}.')
self.redis.lpush('misfire_template', 'One magical item within {{params.radius}} is stripped of enchantment.')

self.redis.lpush('misfire_template', 'Disco Fever. Everyone dances in sight dances. {{params.wissave}}')
self.redis.lpush('misfire_template', 'A god\'s face appears before the caster and says "hushhhhh". Caster is mute for {{params.combatduration}}.')
self.redis.lpush('misfire_template', 'Small harmless rubber balls pelt {{params.target}}. They disappear after {{params.combatduration}}.')
self.redis.lpush('misfire_template', '{{params.target}} is sent forward in time {{params.combatduration}}. ')
self.redis.lpush('misfire_template', '{{params.target}} is pelted by a flurry of snowballs.')
self.redis.lpush('misfire_template', 'The caster finds themselves teleported to a fine dinner call for {{params.combatduration}} where a king is feasting.')
self.redis.lpush('misfire_template', '{{params.target}} grows a hairy tail 4d12 inches long.')
self.redis.lpush('misfire_template', 'A circle of protection is created around the caster.')
self.redis.lpush('misfire_template', 'The target is affected as per a Charm spell. {{params.wissave}}')
self.redis.lpush('misfire_template', '{{params.target}} is attacked by a random swarm.')

self.redis.lpush('misfire_template', 'A random enemy is transformed into a bat and flies away.')
self.redis.lpush('misfire_template', 'The caster thinks the spell has functioned as intended when it actually hasn\'t. This delusion lasts for {{params.combatduration}}.')

self.redis.lpush('misfire_template', 'A rope noose appears around {{params.target}}\'s neck with 10 feet of loose rope.')
self.redis.lpush('misfire_template', '{{params.target}}\'s ferrous items rust completely away in one round. {{params.wissave}}')
self.redis.lpush('misfire_template', 'All weapons within 60 feet of {{params.target}} sing one shrill note for {{params.combatduration}}.')
self.redis.lpush('misfire_template', '{{params.target}} are knocked prone and "stapled" to the ground by a large metal staple.')
self.redis.lpush('misfire_template', 'The world \'forgets\' you for {{params.shortduration}} and you are practically invisible during this period.')

self.redis.lpush('misfire_template', '{{params.target}} are deafened for {{params.shortduration}} by the sound of this spell.')
self.redis.lpush('misfire_template', '{{params.target}} spins rapidly for {{params.combatduration}} and is dizzy for {{params.combatduration}}.')
self.redis.lpush('misfire_template', 'Nearest creature friendly to the {{params.target}} is replaced by a doppelganger. The original creature is imprisoned in the doppelganger\'s lair (wherever that may be).')
self.redis.lpush('misfire_template', 'A {{params.radius}} radius centered around {{params.target}} is suddenly layered in 3 feet of {{params.coverage}}, making it difficult terrain.')

self.redis.lpush('misfire_template', 'Your head becomes an arrow magnet for {{params.shortduration}}- any arrows fired by anyone will veer to hit you.  Normal damage.')
self.redis.lpush('misfire_template', 'A light brown snake bites {{params.target}} on the left knee. It hurts.')

self.redis.lpush('misfire_template', '{{params.radius}} above your intended target appears {{params.largeanimal|article}}.  When the {{params.largeanimal}} falls, both it and the target take appropriate fall damage.')
self.redis.lpush('misfire_template', 'A spray of molten {{params.metal}} shoots from the caster\'s hands towards the target. it does 2d6 {{params.damagetype}} damage.')
self.redis.lpush('misfire_template', 'The person closest to {{params.target}} grows hair on their eyeballs. This is very painful and will cause blindness.')


self.redis.lpush('misfire_template', 'A large stream of urin falls from the sky to douse {{params.target}}. A booming jolly laugh is heard.')
self.redis.lpush('misfire_template', 'A {{params.heavyitem}} appears over {{params.target}} and falls for 2d20 points of damage. {{params.wissave}}')

self.redis.lpush('misfire_template', '{{params.target}} is covered with {{params.color}} mushrooms. each picked mushroom causes a point of damage. They whither and fall off harmlessly after {{params.shortduration}}.')
self.redis.lpush('misfire_template', 'An angry goblin child appears and attacks you from behind with a frying pan, and will flee if injured.')

self.redis.lpush('misfire_template', '{{params.target}} grow an extra set of teeth which last for {{params.duration}}.')
self.redis.lpush('misfire_template', '{{params.target}} is endowed with impressively large forearms.')

#LPUSH misfire_template A star falls from the sky crashing into the nearest village. {{params.target}} know you\'re responsible.
#LPUSH misfire_template {{params.target}}\'s mouth is puckered for d10+10 rounds. No speech, spell casting, breath weapons, or other uses of the mouth are possible.
#LPUSH misfire_template An earthquake comes to visit the area surrounding you.  (300-yard radius, 4-5 on the Richter scale.)  Buildings shake and might crumble.
#LPUSH misfire_template One of the {{params.target}}\'s items pops over and draws the appropriate Circle to confine the {{params.target}}. {{params.target}}s susceptible to summoning must resist at –2 to avoid being encircled. The item drops at the circle.
#LPUSH misfire_template The {{params.target}}\'s deity is summoned. This does not oblige the deity to come, but is liable to attract attention. A reasonably smart deity will recognize the summoning as unintentional, but may still watch the {{params.target}} a little closer for a while.
#LPUSH misfire_template A white rabbit passes by.  When it gets in front of you, it stops, takes a kind of amulet out of a pocket in its vest, looks at it and mumbles, "oh-oh, I\'m too late for the tea-time."  After that, it will vanish down a hole.
#LPUSH misfire_template {{params.target}}\'s race randomly changes until cancelled by dispel magic.  Roll for a new race every day.  Stats remain the same.
#LPUSH misfire_template An enormous tornado picks up {{params.target}} and her associates and takes them to Kansas (or some other boring, flat, corn filled spot on the same plane.)
#LPUSH misfire_template A god (random, of course) "awards" you with a quest (the nature of the quest is up to the DM. {{params.target}} may decline....
#LPUSH misfire_template 10 normal 1st level Wizards show up and cast the same spell you just tried on your intended {{params.target}}.  They disappear when this is done.
#LPUSH misfire_template {{params.target}} learn a new spell (Random) that of course is unstable and this also makes one of your other spells unstable (random,) the problem is just that you don\'t know which one.
#LPUSH misfire_template For 1d4 weeks your body contracts a strange shape-shifting disease.  Roll 1d10 every morning.  1-3 you are male; 4-6 you are female; 7-9 you are both; 10 you are none.
#LPUSH misfire_template One of your permanent damages is mystically healed, if you don\'t have any permanent damage; now is a perfect time to roll for one!
#LPUSH misfire_template The {{params.target}}\'s mount is polymorphed into a goat if it fails a save vs. magic. If the {{params.target}} has no mount, it affects the nearest one.
#LPUSH misfire_template {{params.target}} is surrounded by a giant pliable (but impenetrable) bubble for 24 hours. (Giant hamster ball, anyone?)
#LPUSH misfire_template For 1 melee a strange oval black disc hangs in the air in front of you and then it disappears (a dimensional gateway to medieval Europe...)
#LPUSH misfire_template The {{params.target}} gains the ability to levitate for brief periods.  The ability to levitate lasts for 10 minutes, but the person can only hover 1 foot off the ground at most and can only hover for a number of rounds equal to their PE.
#LPUSH misfire_template {{params.target}} polymorphs into a bird appropriate to the area, or a random type if no birds are in the area. 40% chance for a monster type.
#LPUSH misfire_template {{params.target}} polymorphs into a reptile/amphibian appropriate to the area, or a random type if no reptiles or amphibians are in the area. 40% chance for a monster type.
#LPUSH misfire_template {{params.target}} polymorphs into a bird appropriate for the area, or a random type if no birds are around; 40% chance for a monster type.
#LPUSH misfire_template {{params.target}} polymorphs into a mammal appropriate for the area, or a random type if no mammals are around; 40% chance for a monster type.
#LPUSH misfire_template {{params.target}} polymorphs into a reptile/amphibian appropriate for the area, or a random type if no reptiles/amphibians are around; 40% chance for a monster type.
#LPUSH misfire_template A bunch (1d6) of naked Elvin maidens run in your direction.  They disappear 1 yard in front of you.  If you are male you lose initiative while they are there.
#LPUSH misfire_template One of {{params.target}}\'s items teleports into the {{params.target}}\'s hand. {{params.target}} drops anything previously held in the hand. If {{params.target}} has no hands or is not a creature, the item just lies there.
#LPUSH misfire_template A random attribute of your character becomes a wandering effect.  {{params.target}} get +1 every day until it reaches 30, then it restarts with 1 until it ends with the number it started with.  A remove curse will work, but if performed when it\'s higher then in the beginning the attribute will drop 1 point under the starting number.  This can be used to restore lost luck, although you must have it restored on a day between what you had and your original maximum, otherwise you will lose a point from your lower score.
#LPUSH misfire_template A concubine or eunuch (whichever suits you best) materializes in front of you and insists on giving you PLEASURE!
#LPUSH misfire_template Tiny sparks arc from the {{params.target}}.  The sparks do no damage to the {{params.target}} or to any other creature.
#LPUSH misfire_template The {{params.target}} becomes noticeably warm to the touch.  Although they feel severe warmth, the heat is not great enough to damage either the imbiber or any other creature.
#LPUSH misfire_template A random person within 5 feet of the {{params.target}} becomes noticeably cool to the touch.  Although they feel a sever chill, the cold is not great enough to damage either the {{params.target}} or any other creature.
#LPUSH misfire_template The {{params.target}}, if able to cast spells, casts them all with random {{params.target}}s and normal expenditure.
#LPUSH misfire_template Randomly roll a new race.  If it isn\'t the same as your current race, reroll all your stats.  Level and skills remain the same.  Remove curse or negate magic will work to restore you. (So save your stats, just in case ;)
#LPUSH misfire_template The back of your skull is from this day on made of crystal, permanently.  Mind the head, please...
#LPUSH misfire_template A lightning bolt shoots from the {{params.target}}\'s fingers.  When it strikes the {{params.target}} (no damage) it splashes and the {{params.target}} is covered in slick grease.
#LPUSH misfire_template A rock launches itself from the ground and strikes {{params.target}} on the head. This does no damage except to skew any helm he has on and make him think he\'s being attacked from someplace else.
#LPUSH misfire_template {{params.target}}\'s entire party teleported to the nearest artifact/relic (does not guarantee it is usable, and it is likely to be in the possession of someone else.)
#LPUSH misfire_template {{params.target}}\'ve got yourself so down you got a headache.  Migraine, permanent.  (-1/-5%, 30% chance of occurring when in a stressful situation.)  May be removed with a remove curse.
#LPUSH misfire_template {{params.target}}r ears turn permanently light blue.  May be removed by a remove curse.
#LPUSH misfire_template {{params.target}} grow the legs of a black goat permanently.  Increase SPD by 2d4 points.  May be removed by a remove curse.
#LPUSH misfire_template A random person in your vicinity permanently grows a skin coloured 1 ft long crooked horn on their forehead (ram attack does 1d6 dam, plus dam bonus.)  May be removed by a remove curse.
#LPUSH misfire_template {{params.target}} grow a 10 in long red nose, permanent.  May be removed by a remove curse.
#LPUSH misfire_template {{params.target}}r head shrinks to 1/2 of its normal size, permanently.  May be removed by a remove curse.
#LPUSH misfire_template {{params.target}}r ears grow three times larger, permanently.  May be removed by a remove curse.
#LPUSH misfire_template {{params.target}} grow another pair of arms, permanently.  May be removed by a remove curse.
#LPUSH misfire_template {{params.target}} grow a 5-inch high dark crest, permanently.  May be removed by a remove curse.
#LPUSH misfire_template From this day on you can\'t remember anything from certain full-moon nights since you suffer from Lycanthrophy.  May only be removed by a remove curse.
#LPUSH misfire_template The person on your right grows a pair of frog\'s legs, permanently, unless they make a save of 14 vs. curse.  Can be removed by a successful remove curse.
#LPUSH misfire_template "Just who do you think you are!!??  GET OFF MY HEAD!!!" Screams a stone from under your boot and gives you the evil eye. (Not the psionic or curse.)
#LPUSH misfire_template {{params.target}} become aware of the workings of the spell "Size of the Behemoth"  It\'s unstable of course.
#LPUSH misfire_template A group of wandering pilgrims (3d6) mistakes you for a saint and starts harassing you with prayers, offerings and submission.  They will be very hard to get rid of and may act violently when the truth is revealed, depending on their religion of course.
#LPUSH misfire_template {{params.target}} grow roots and cannot move for the next 1d4 hours, unless someone cuts off your feet of course.
#LPUSH misfire_template The {{params.target}} is imprisoned on another plane (DM choice.)  The captors may or may not be intelligent enough to care properly for their new inmate.
#LPUSH misfire_template {{params.target}} and {{params.target}} must re-roll their highest statistic that is not a Prime Requisite.
#LPUSH misfire_template All weapons within 60 feet of {{params.target}} receive a random lesser magical attribute.
#LPUSH misfire_template The {{params.target}}\'s hair changes colour temporarily.  Roll 1d6 for colour, 1=blonde, 2=red, 3=brown, 4=black, 5=grey, 6=blue
#LPUSH misfire_template All non-magical articles of clothing on {{params.target}}, crumble to dust.  Magic clothes receive a save.
#LPUSH misfire_template A random spell of the same level as the intended spell affects {{params.target}} if she fails a save.
#LPUSH misfire_template Drain {{params.target}}\'s magic items (except artefacts) of all enchantments; each item gets a save
#LPUSH misfire_template All the {{params.target}}\'s magic items are teleported to random locations within 100 feet. Items that don\'t wish to be separated from the {{params.target}} get a save.
#LPUSH misfire_template The {{params.target}} emits a cause fear on all within a 60-foot radius.  Standard save.
#LPUSH misfire_template {{params.target}}, everybody and everything in a 100 ft radius will be teleported 1d100 miles in a random direction (1d4 N, E, S, W).  Each person and object gets a separate save.
#LPUSH misfire_template One charge from a randomly chosen Wand, Rod, Staff, or other Charged item affects the {{params.target}} if she fails her save.
#LPUSH misfire_template A booming voice audible over the din of battle says “SURRENDER!” This acts as a Command Word and all who hear it must make a save at the {{params.target}}\'s level or surrender to anyone who makes their save.
#LPUSH misfire_template The {{params.target}}\'s familiar turns against him. The animal is no longer treated as a familiar (appropriate penalties for familiar loss) and will act as a normal creature of that type will. This may include attacking the {{params.target}} (usually just running away). If {{params.target}} doesn\'t have a familiar, he does now (GM choice. Be creative).
#LPUSH misfire_template In some strange way the spell makes you feel really good…{{params.target}} have an immediate orgasm and you lose your initiative.
#LPUSH misfire_template {{params.target}} notice a little pink hedgehog sitting on your head and at the same time you loose your initiative.
#LPUSH misfire_template {{params.target}} is bound in High Steel straps. These will take a skilled locksmith to remove.
#LPUSH misfire_template The {{params.target}} increases in weight by 20 pounds until the effects wear off.  This extra weight counts against what the {{params.target}} can carry until the effects wear off.
#LPUSH misfire_template A passing frog stops and says "{{params.target}}\'d better behave or I\'ll....." then hops off
#LPUSH misfire_template {{params.target}} is covered in liquid chocolate.  A random passerby offers to lick it off.
#LPUSH misfire_template {{params.target}}r appearance is changed to that of a dwarf.  No stat change.  If you are already a dwarf, you now look like an elf.
#LPUSH misfire_template {{params.target}} has an urgent call from nature and must immediately retreat to relieve himself.
#LPUSH misfire_template The magic you performed seems to have defied the laws of reality and bends all light that hits you for the next 1d6 hours; you are invisible even to yourself.
#LPUSH misfire_template {{params.target}} forget your name and profession for 1d4 weeks.  {{params.target}} retain your skills and may react but you are not aware of what you\'re capable of.
#LPUSH misfire_template The {{params.target}}\'s skin becomes sticky, like powerful glue.  The {{params.target}} must make a PP saving throw to drop an object that they are holding.
#LPUSH misfire_template The {{params.target}}\'s hands become slimy, and s/he has to make a PP roll each round to maintain their grip on any object s/he is holding.
#LPUSH misfire_template A stench of Hades (same as spell) is cast on you by a passing seagull that flies off laughing.
#LPUSH misfire_template {{params.target}} becomes immensely dirty- so much so that a dust cloud forms around her. Only natural bathing will remove the dirt. Interactions with others will suffer a penalty (unless they enjoy that kind of thing).
#LPUSH misfire_template A moose comes up to you and whispers in your right ear.  "{{params.target}} can\'t hear this with your left can you?" When he has said this he looks at you for a moment and wanders off mumbling.
#LPUSH misfire_template {{params.target}} is teleported to the top of the highest tree in sight and must make a PP check to avoid falling.
#LPUSH misfire_template {{params.target}}\'re mistaken for a wanted person in the next town you enter.  {{params.target}} will eventually be able to clear yourself, but it may take some doing.
#LPUSH misfire_template {{params.target}} sees a volley of arrows headed for him and will react appropriately. They\'re not really there, though, and his allies wonder what the heck he\'s doing.
#LPUSH misfire_template {{params.target}} find yourself dressed in the finest silk garments, but you\'ve no idea of where your armour is.  (Or whatever you were wearing.)
#LPUSH misfire_template The {{params.target}} gains 15th level singing ability and can\'t wait to try it out. Ever hear a troll sing?
#LPUSH misfire_template Everybody\'s last meal animates and seeks the easiest way out, which will be down if more than 3 hours have passed. No damage is incurred, but combat ceases for 2 rounds and the result may be embarrassing.
#LPUSH misfire_template A pygmy quire steps out from hiding, sings folksongs for 1d6 minutes, bows respectfully and departs chanting.
#LPUSH misfire_template All weapons and armour within a 50\' radius of {{params.target}} become rubbery and useless for 2d4 rounds. Weapons used during this time will be ruined, armour becomes form fitting.
#LPUSH misfire_template {{params.target}} becomes magnetically repulsive for d20 rounds. Metallic objects cannot be brought closer than 5 feet; any ferrous items on the {{params.target}} are repelled and go flying.
#LPUSH misfire_template {{params.target}}\'re transformed into a cute little Yorkshire terrier for god (DM) knows how long
#LPUSH misfire_template The {{params.target}} must succeed at a ME roll or be compelled to sing until her next action.  The singing prevents the person from casting spells, unless they are trained to cast by song. 
#LPUSH misfire_template Everyone you look at in the next 20 minutes must save vs Psionics or be hit by an Evil Eye (20 points of Damage each.)
#LPUSH misfire_template 1d4 silver bullets fly at {{params.target}}. Bullets contain 1 sp worth of metal each.
#LPUSH misfire_template {{params.target}} glows a primary colour for 2d12 days. This glow has the effective light of a normal torch.
#LPUSH misfire_template {{params.target}} is fascinated by what the {{params.target}} is doing and will stop whatever he is doing to watch.
#LPUSH misfire_template The {{params.target}}\'s hair spontaneously combusts into blue flame and continues to burn for 6d10 turns. The hair is not consumed, and no damage is taken. The flame is actually an Illusion and can be detected as such.
#LPUSH misfire_template Instead of a spell, a big green toad crawls out of your mouth and hops off.  Spell cost is still the same though.
#LPUSH misfire_template {{params.target}} opens a gate to another location (DM choice or random) and is pulled through.
#LPUSH misfire_template A river of lava stretches out from your feet in the direction you were looking when the spell was cast.  Effective level is 6th.
#LPUSH misfire_template {{params.target}} lapse into a coma for 1d8 days, and must roll a save vs. coma/death.
#LPUSH misfire_template A nearby bird starts singing the Star Spangled Banner in a rich baritone voice, and will follow the {{params.target}}, singing at 100 decibels, for 1 month.
#LPUSH misfire_template Caustic slime spews out of {{params.target}}\'s nose. {{params.target}} takes 1d10 points of damage and cannot smell for one month.
#LPUSH misfire_template {{params.target}} grow a permanent exoskeleton, like a beetle.  AR 15, HF 12.  May be removed by remove curse.  Roll vs random insanity every other month.
#LPUSH misfire_template In addition to your spell you conjure up a wasp\'s nest inside your {{params.target}}\'s mouth.
#LPUSH misfire_template {{params.target}} immediately stops what he is doing to sit down and perform some other non-combat related skill with whatever materials are at hand (e.g. making money bags out of his cloak).
#LPUSH misfire_template "Pleased to meet you.  Allow me to introduce myself..." {{params.target}} find yourself in a large damp dining hall at one end of a large oak-table facing a handsome dark-eyed young man.  He looks at you and has a sip of his wine, smiles and says: "I have a proposal to make, but first we eat hmmmm?"  The dinner you\'re served is the best you\'ve had in your entire life, the man makes small talk during the meal.  After you\'re finished he personally serves you a glass of vintage wine and asks you to do a favour for him.  "It is of course voluntary, since I wouldn\'t dream of forcing you to do anything against your will."  He will not tell you the nature of the favour until you agree.  If you refuse he will simply send you back....
#LPUSH misfire_template A spray of boiling oil strikes the {{params.target}} and he takes a point-blank fireball attack.
#LPUSH misfire_template Next missile weapon used by {{params.target}} multiplies by 6; one arrow becomes 6, each with its own attack.
#LPUSH misfire_template {{params.target}} shoots forth 8 non-poisonous snakes from their fingertips.  Snakes do not attack.
#LPUSH misfire_template All of {{params.target}}s flesh except her blood vessels and bones become transparent for 1d4 turns. Ick.
#LPUSH misfire_template A rat offers to be your pet, if you\'re prepared to feed it with one pound of cheese a week.
#LPUSH misfire_template The magic energies didn\'t quite leave when you were finished with them, instead they hung onto you and from now on your hair always stands straight up, your handshake jolts and static electricity sparks appear on your body now and then.  This also makes you only suffer half damage from electrical attacks.  {{params.target}} literally glow in the dark.
#LPUSH misfire_template From this day on, you will always walk on a track of solid cement.  The cement will remain even after you pass.  {{params.target}} won\'t have to worry about dense forests and such, but tracking you will be very, very easy.  Remove curse and negate magic will work.
#LPUSH misfire_template {{params.target}} sprayed by 2d20 pieces of confetti, edge on. They do 1 HP of damage each and {{params.target}} has annoying paper cuts that will itch maddeningly as they heal.
#LPUSH misfire_template All of {{params.target}}\'s weapons turn to Cursed Friend slaying weapons, which take effect the next time they are used and then return to normal.
#LPUSH misfire_template {{params.target}}\'re blessed by Colie and receive one random benefit, plus a random curse (most likely mixed together, as is his usual.)
#LPUSH misfire_template A strange pine tree appears in front of you.  It is highly decorated as if part of some strange ritual.  If you examine it closely you can see small dolls hanging from its branches featuring a bearded man in red clothes.  Burning candles also line the branches.  Under the tree there are some packages in multi-coloured paper, each one bearing a label...
#LPUSH misfire_template DM shouts “Wish!” and counts down from 10.  If the {{params.target}} makes a wish within the count it is granted.  Be creative, be cruel.
#LPUSH misfire_template {{params.target}}\'s hit points are raised (and healed) to their racial maximum.  (Racial PE maximum plus 8 points/character level)
#LPUSH misfire_template {{params.target}} is affected by Paralyze (as the spell). Duration is based on the {{params.target}}\'s level.
#LPUSH misfire_template {{params.target}} is wrapped in chains of force that will give him a jolt of Electricity (1d8 dam) if he struggles.  {{params.target}} is entitled to a RR at the {{params.target}}\'s level.
#LPUSH misfire_template Circle of Flame, as per the spell, surrounds {{params.target}} and moves with her, duration based on {{params.target}}\'s level.
#LPUSH misfire_template {{params.target}} can feel the rhythm, even before you can hear the wonderful music.  A fairies dance affects the entire party (same as your effect level.)
#LPUSH misfire_template {{params.target}} permanently forgets one spell chosen randomly. It may be re-learned at the next level.
#LPUSH misfire_template Dinner\'s served for all persons within 50 feet.  (A real banquet with servants and all…)
#LPUSH misfire_template All moving creatures within 60 feet of {{params.target}} must make a PP roll or trip and fall.
#LPUSH misfire_template {{params.target}} Levitates uncontrollably, always heading upward until the spell duration (at the {{params.target}}\'s level) is reached, then they fall.
#LPUSH misfire_template {{params.target}} steals {{params.target}}\'s reflection for 1d20 days. For that time, anytime {{params.target}} looks in a mirror she will see the {{params.target}} instead of herself.  ({{params.target}} will be ‘reflected\' doing whatever it is the {{params.target}} is actually doing.  If they are blocked from scrying, {{params.target}} has no reflection at all!)
#LPUSH misfire_template A forest grows up around {{params.target}} in 3d4 rounds, 1-mile radius per level of the intended spell.
#LPUSH misfire_template {{params.target}} is sucked into an extra-dimensional pocket for the duration of the intended spell.
#LPUSH misfire_template A plant within 10 feet of {{params.target}} swells alarmingly and then explodes in a cloud of pollen, obscuring everything in a 20-foot radius as per a Fog spell.
#LPUSH misfire_template The spell you just cast cost nothing; in fact, you just gained an additional spell.
#LPUSH misfire_template {{params.target}} smells of roses for one month. If killed, his body will not decompose and will resurrect as though given a Resurrection spell.
#LPUSH misfire_template {{params.target}} jerks uncontrollably for 1d4 rounds, then a hypnotic pattern appears, affecting all who see it as a Hold Person spell.
#LPUSH misfire_template {{params.target}} find yourself sitting on a transparent seesaw facing the {{params.target}} of your spell.
#LPUSH misfire_template The intended spell functions, but consumes one charge from a random nearby charged magic item instead of {{params.target}}\'s spell
#LPUSH misfire_template The {{params.target}} is picked up by an invisible hand and shaken like a rag doll for 1d6 rounds. Spellcasting under such conditions is impossible unless casting an instantaneous spell.
#LPUSH misfire_template Every spell the {{params.target}} has learned goes off, one per round, until {{params.target}} is exhausted. {{params.target}} may name the {{params.target}} with a successful ME roll.
#LPUSH misfire_template {{params.target}} turn yourself into a Sulfur-Crested Cockatoo for 1d4 days, but retain your self-control.
#LPUSH misfire_template A random snake is teleported in to within 10 feet of {{params.target}} and is under the {{params.target}}s control.
#LPUSH misfire_template A doppelganger of the {{params.target}} appears in the {{params.target}}\'s place, as she is teleported to appropriate cover. The simulacrum is under the {{params.target}}\'s control.
#LPUSH misfire_template {{params.target}} picks an object nearby for Animation. The object must be smaller than the {{params.target}} but is under the {{params.target}}\'s control.
#LPUSH misfire_template A geyser erupts midway between {{params.target}} and {{params.target}}. Anyone within 10 feet of it takes a 4d6 damage from the boiling steam.
#LPUSH misfire_template Trees around {{params.target}} fall down (if none, some grow first). {{params.target}} must make a PP check or be pinned beneath them.
#LPUSH misfire_template Fog, as per the spell, but only between the {{params.target}} and the {{params.target}}, and moves with them.
#LPUSH misfire_template {{params.target}} is surrounded by hot coals. All those attempting to walk on the coals must make a PE check to stay on them.
#LPUSH misfire_template The {{params.target}}\'s teeth turn into unbreakable white stone. She can chew through just about anything (including soft metals) and never gets a cavity again. If {{params.target}} already has stone teeth this surge removes them.
#LPUSH misfire_template {{params.target}}\'s eyes become vertically slit like a cat\'s. The {{params.target}} gains Nightvision, if the {{params.target}} already has night vision, it is extended by 10 feet.  If the {{params.target}} has slit eyes already, this surge removes them.
#LPUSH misfire_template {{params.target}} grow fangs (1d6 bite damage) and have a hard time learning to talk again (speak-15%).  A Remove Curse can remove the fangs. If the {{params.target}} has fangs already, this surge removes them.
#LPUSH misfire_template The {{params.target}} of your spell explodes, and dies instantly.  (PC\'s get a save vs. magic).  If you\'re lucky (roll) you may be able to assemble enough pieces to restore and resurrect them.
#LPUSH misfire_template {{params.target}} hallucinate for 1d12 months.  The hallucinations are completely up to the all-powerful GM.
#LPUSH misfire_template {{params.target}} decide to share the wealth.  Roll again on this table, once for each member of your party (including you.)  Everyone gets the effect you rolled for him.
#LPUSH misfire_template All scrolls anyone within a 30 foot radius of you possess (even when these scrolls are not in the radius) change their heading at random. 
#LPUSH misfire_template {{params.target}} find yourself in a splendid golden chain-mail teleported from the nearest king\'s ransom.
#LPUSH misfire_template {{params.target}} sprouts leaves (no damage cause, and they can be pruned without harm)
#LPUSH misfire_template The {{params.target}} turns into a painting of herself, until Dispelled (any Dispel will do). Any changes painted on the canvas will become part of the {{params.target}} if and when she is returned to her normal form.
#LPUSH misfire_template The next living creature the {{params.target}} touches gains 1d10 HP and the {{params.target}} loses the same amount permanently.  This can raise the creature\'s HP above the maximum.
#LPUSH misfire_template Hostile creatures within 60\' of {{params.target}} have their hit points restored to maximum.
#LPUSH misfire_template All your spells are now stable.  But for how long?  (DM, this is up to you to decide, I suggest 1d4 weeks maximum.)
#LPUSH misfire_template A stone Golem rises from the ground and is ready to fulfill your wishes the best it can.
#LPUSH misfire_template A 30-inch Colour TV appears from another time and dimension appears in front of the {{params.target}}. All who view it must make a ME check or be totally unable to do anything except watch the screen.
#LPUSH misfire_template Jail cell bars of the appropriate size surround the {{params.target}} and her party (and anyone else in between).
#LPUSH misfire_template {{params.target}} encased in a block of lime Jello 10 feet on a side. {{params.target}} must make a PP check every round to escape. Keep rolling until she gets out or passes out from lack of oxygen.
#LPUSH misfire_template All normal doors, secret doors, portcullises, etc. (including those locked or barred) within 60 feet of the {{params.target}} swing open.
#LPUSH misfire_template {{params.target}} is struck by a sudden bit of insight about a random skill and will succeed the next time she uses that skill as if she rolled a 01. The spell however is forgotten.
#LPUSH misfire_template A randomly chosen charged item has its spell changed. The appearance, command word, and number of charges do not change. Just the spell. Owner won\'t know this until the item is used again.
#LPUSH misfire_template {{params.target}}\'s clothing changes colour to match the surrounding environment as per the Camouflage spell. If the environment changes the {{params.target}}\'s clothes will not change again.
#LPUSH misfire_template {{params.target}} turns Invisible as per the spell, but can be hit once before turning visible again.
#LPUSH misfire_template {{params.target}}r hands and lower arms are turned into an oozing yellow liquid for 1d3 minutes.  If more than a quarter ounce of it gets out of place, you will need a restoration for them to be functional again.
#LPUSH misfire_template {{params.target}}\'s weapon or other possession becomes a teddy bear (25%), leg of mutton (25%), or red herring (50%).  If {{params.target}} has no possessions roll again.
#LPUSH misfire_template All spells cast during the previous round are re-cast again this round (no cost), affecting the same {{params.target}}s again.
#LPUSH misfire_template {{params.target}} gains a stutter. Remove curse will cure it.  75% chance that spells cast while stuttering will misfire, resulting in needing to roll on this chart again.
#LPUSH misfire_template {{params.target}}\'s hair turns florescent green (some other obnoxious colour if already green). This is permanent until new hair grows in.
#LPUSH misfire_template The {{params.target}}, and everyone within 10 feet of them have their fingernails stretch and curl.  Although they do not affect weapon use or unarmed attacks, they look strange.  The growth is permanent, but may be trimmed in the usual fashion.
#LPUSH misfire_template {{params.target}} accidentally summon a lesser deevil, that isn\'t very happy ‘bout being dragged from his own dimension.
#LPUSH misfire_template {{params.target}} are cured of any insanities you may have, if you have none, roll up an obsession.
#LPUSH misfire_template This was not quite what you thought should happen, but you conjure the one thing that you and your party needs most at this very moment, be it a piece of parchment with the layout of the dungeon you are trapped in or anything/anyone else.  {{params.target}}r DM will know what you need most, and will give it to you.  (DM note: The item disappears at the end of this session.)
#LPUSH misfire_template {{params.target}} notice a necklace around your neck that wasn\'t there before.  Anyway you can\'t take it off and as another bonus it gives you a +2 vs possession.
#LPUSH misfire_template All your friends, even distant ones, are mystically teleported to your location.
#LPUSH misfire_template All your magic items and weapons change their special abilities, and you don\'t know which is which.  (For example, you have a ring of save vs magic +1, 1 pair of gloves with healing touch and a sword with 1d6 extra damage.  {{params.target}} now have a ring with 1d6 extra damage, a pair of gloves with +1 save vs magic and a sword with healing touch.  Or any other combination.)
#LPUSH misfire_template The {{params.target}} is turned into a puddle of water for d8 rounds. Evaporation or splashing will do 1d20 hp dam. The {{params.target}} returns to normal form at the end of the duration.
#LPUSH misfire_template {{params.target}}\'s PS bonus is doubled for rounds equal to the level of the intended spell.  If they have no PS bonus, they gain a +2 for the duration.
#LPUSH misfire_template {{params.target}} and {{params.target}} become locked in a heated debate over the nature and use of Arcane Magic and will do nothing else for 1d6 rounds. If the two do not have a language in common, an imp appears to act as translator.  Inanimate objects animate for the duration.
#LPUSH misfire_template For a moment you seemed to be getting away with it, but your spell backfires and goes off in a random direction.
#LPUSH misfire_template {{params.target}} is cleaned. All dirt and bad smells are removed. This can actually cause damage to creatures composed of earth, DM discretion.
#LPUSH misfire_template {{params.target}} inherit a large estate from a senile Baron.  This is told to you by a messenger who also asks you to attend the funeral, which will be held soon.
#LPUSH misfire_template A magical artefact of great power is transported into the {{params.target}}\'s hands. The {{params.target}} is affected normally by handling it if it has detrimental effects. The previous owner will probably be missing it and be coming after it very soon.
#LPUSH misfire_template Enchantments and bonuses on all weapons and armours/shields within a 50\' radius of {{params.target}} have their bonuses inverted for 2d10 rounds (i.e. a +10 weapon becomes a –10 weapon)
#LPUSH misfire_template One of {{params.target}}\'s weapons flies through the air and attacks {{params.target}} as per a Dancing Weapon.
#LPUSH misfire_template If you are male, a beautiful maiden of your race comes to you with an apple in her hand.  "Be my Adam, I\'m your Eve."  She gives you the apple and disappears.  If you are female a nasty little snake bites you for 1 point of damage, but luckily no poison.
#LPUSH misfire_template A deep lake forms in a 100\' radius of {{params.target}}. Everyone in that area gets a quick swimming lesson.
#LPUSH misfire_template Everything indestructible, everlasting, permanent (Magic items, rune weapons, eternal flames, etc.) in a 1-mile radius of you will crumble to dust, vanish, and fade out.  On the other hand, every object that is not indestructible will get this attribute and be considered magical from now on.
#LPUSH misfire_template All magical weapons within 30 feet of the {{params.target}} are increased by +2 for 1 turn.
#LPUSH misfire_template Smoke trickles from the ears of all creatures within 60 feet of the {{params.target}} for 1 turn.
#LPUSH misfire_template Colourful bubbles come out of the {{params.target}}\'s mouth instead of words.  Words are released when bubbles pop.  Spells that are not stilled cannot be cast for 1 turn.
#LPUSH misfire_template The next phrase spoken by the {{params.target}} becomes true, literally for 1 turn.
#LPUSH misfire_template Spell has a minimum duration of 1 turn (i.e. a fireball creates a ball of flame that remains for 1 turn, a lightning bolt bounces and continues, possibly rebounding, for 1 turn, on the other hand, a healing spell activates every melee for one turn.)
#LPUSH misfire_template Hero or other famous figure friendly to {{params.target}} is summoned and remains for one turn.
#LPUSH misfire_template All blunt weapons within the {{params.target}}\'s sight emit loud kissing noises whenever they hit anything for the next turn.
#LPUSH misfire_template The earth around you is turned into mud, same effect level as your own.
#LPUSH misfire_template The {{params.target}} is teleported to the highest mountaintop in sight.  If there is no mountain visible the highest location within sight will do.
#LPUSH misfire_template {{params.target}} is turned into a cartoon rendition of himself and will not be able to take any action without making a short (less than 1 round, no more than 60% action) speech telling everyone exactly what he\'s going to do.
#LPUSH misfire_template {{params.target}} turns into a block of raspberry flavored Jello; all his possessions are suspended in the Jello.
#LPUSH misfire_template Molten lava comes out of the ground near {{params.target}}, who takes 5d10 points of damage.  Roll d100 for duration: 01-50, 1d4+4 rounds; 51-70, 1d4 hours; 71-85, 1d100 days, 86-100, becomes a real, non-magical volcano.
#LPUSH misfire_template All people, including you, within 40 feet are turned completely blue for 1d3 days. (Possessions too.)
#LPUSH misfire_template All people, including you, within 40 feet are turned completely yellow for 1d3 days. (Possessions too.)
#LPUSH misfire_template The {{params.target}} becomes drowsy, and falls asleep for 1d3 hours.  They can be woken normally, as if they were simply taking a nap.
#LPUSH misfire_template {{params.target}} begins singing as though she had 15th level singing. This lasts for 3 days and she hums in her sleep.
#LPUSH misfire_template 3d10 gems shoot from the {{params.target}}\'s fingertips.  Each gem is worth 1d6x10 GP
#LPUSH misfire_template the next noble you encounter presents a warhorse of the finest breed without any markings to you as a token of eternal friendship.
#LPUSH misfire_template {{params.target}}r SPD is raised to 55 due to the horse-body you grew.  {{params.target}} are now a centaur.  Duration: permanent, Remove curse or negate magic will help.
#LPUSH misfire_template {{params.target}} scorch yourself on the cold blue magical flames that suddenly engulf you as you burn all of your spells for the day  (1d6 damage for each spell)  If you have more than 2 dice of damage, the scars left on you by this horrible experience will reduce your PB by 1d6 permanently.  (A healer will be able to help.)
#LPUSH misfire_template {{params.target}} attempts to commit suicide for 3 rounds. Must roll normal attacks on himself.  If he inflicts a serious wound or stuns himself he stops, as it really is just a cry for help.
#LPUSH misfire_template {{params.target}} emits a bad odor; only the strongest perfume/cologne will cover it up.
#LPUSH misfire_template Gate opens to a randomly chosen outer plane; 50% chance for an extra-planar creature to appear.
#LPUSH misfire_template Roll twice on this table, but any outcome will either be permanent or TEN times the indicated damage/strength/number.
#LPUSH misfire_template Or are they?  {{params.target}} grows an argumentative, annoying second head on her shoulder.
#LPUSH misfire_template 1000 healing potions appear 100 yards above your {{params.target}} and fall down on it.  They will make damage and heal it in the same moment, so nothing really happens, besides the mountain of shards your {{params.target}} is buried under
#LPUSH misfire_template Everyone within a 150-yard radius, except you of course, is affected by the spell Faeries dance (effective level 4) and you find yourself lacking your entire spell reserve.  The affected people get a save vs magic of 14 or higher. 
#LPUSH misfire_template Some people to the left of you (1d8 randomly selected,) will be affected by the spell Words of Truth for one full day. (Save 15 or higher.) 
#LPUSH misfire_template One of your present, random companions turns into a black goat for 1d4 days unless s/he makes a save vs. spell magic of 15 or higher.
#LPUSH misfire_template {{params.target}} are affected by the spell Shadow meld for 3d6 melees (save at 15 or higher)
#LPUSH misfire_template The {{params.target}} of your spell is instantly and permanently turned into a turtle.  A negate magic may restore him/her.
#LPUSH misfire_template {{params.target}}\'s clothing changes to the outfit of a full patch Hell\'s Angel biker.
#LPUSH misfire_template Rabbit comes out of the nearest helm/hat. It runs for its life, but not before soiling the head of the wearer.
#LPUSH misfire_template {{params.target}} changes into a 4-foot diameter jellyfish unless a save vs. magic is made at –2.  If on land, the {{params.target}} takes 4d10 points of damage each round unless continually doused by water.
#LPUSH misfire_template A respected noble claims that you owe him 56000 gold pieces and sets a reward of 5000 gold pieces to anyone who can bring you before him alive.  {{params.target}} become aware of this when you see your own picture posted in the next town you enter.
#LPUSH misfire_template {{params.target}}s\' clothing is transformed into a soft, skin-tight, glossy black leather outfit studded with silver.
#LPUSH misfire_template A scribe appears and wants to do the story of your life.  He\'s very hard to get rid of and won\'t take no for an answer.
#LPUSH misfire_template All of your belongings, except holy and rune weapons are lost.  The items just disappear into thin air.
#LPUSH misfire_template The fingers of a nearby randomly chosen creature shrink to 1/12th their normal size for 1 hour.
#LPUSH misfire_template A large bulls eye {{params.target}} appears on {{params.target}}, giving anyone aiming at her with any kind of ranged attack a +10 to hit.  This lasts for 1 hour.
#LPUSH misfire_template A 10\' radius area chosen by the {{params.target}} becomes intensely cold (for the surrounding environment) for one hour.
#LPUSH misfire_template The {{params.target}}\'s voice becomes high pitched like a pixie for the next hour.
#LPUSH misfire_template The {{params.target}}\'s ears grow to the size of dinner plates.  S/he gets a +2 Per for the next hour.
#LPUSH misfire_template The {{params.target}} is unable to speak in a whisper, and his speaking voice becomes louder than normal.  Both effects last for the next hour.
#LPUSH misfire_template The {{params.target}}\'s eyes turn completely black, including pupils, whites, and irises.  The change in eye colour does not affect their vision, but the DM may impose small circumstance penalties in social situations.  (10th level negate magic or a remove curse at ½ will return your eyes to their normal colour.)
#LPUSH misfire_template {{params.target}} is covered in spider webs, complete with thousands of tiny spiders that will crawl into every crevice and space in his armour.
#LPUSH misfire_template {{params.target}} learns a randomly chosen spell. Can be from any realm (wizard, clerical, elemental, etc.) and need not fit any of her existing OCC\'s.
#LPUSH misfire_template A shrubbery a few yards away warns you of a nearby band of Orcs.  Actually true, but far too late.  10 Orcs step up to your party and explain that they\'re going to eat you for supper. (Low-level mercs.)
#LPUSH misfire_template {{params.target}} Phases into and out of the ethereal plane for the next 1d10+10 rounds.
#LPUSH misfire_template {{params.target}} can only be hit by a +5 weapon or greater for the next 1d10+10 rounds.
#LPUSH misfire_template {{params.target}} turned into an infant of the same race. She reverts to her original age after 1d10 rounds.
#LPUSH misfire_template {{params.target}} turned into an infant of the same race. He reverts to his original age after 1d10 rounds.
#LPUSH misfire_template All non-magical clothing, weapons, armour, and similar equipment must make a save vs. magic or Enlarge to twice their normal size for 4d10 rounds.
#LPUSH misfire_template The area fills with countless butterflies, blinding everyone for 2 rounds.
#LPUSH misfire_template An enormous glitter covered ball appears in mid-air between {{params.target}} and {{params.target}}. The words and music to “Staying Alive” play loudly, and {{params.target}} and {{params.target}} disco dance for the next 2 rounds.
#LPUSH misfire_template Deafening bang affects everyone within 60 ft.  All those who can hear must save vs spell or be stunned for 1d3 rounds.
#LPUSH misfire_template {{params.target}} falls down and is pinned there as though under a great weight for 3 rounds.
#LPUSH misfire_template Cream pie flies at {{params.target}}; {{params.target}} must waste a round wiping it off his face or fight at –2 for the next 3 rounds.
#LPUSH misfire_template {{params.target}} is able to drain Life Essence (1d8 points) at a touch for 1d4 rounds.
#LPUSH misfire_template {{params.target}} finds her lungs filled with water; she must make a PE check or die.  If it is made she can do nothing but cough and sputter for 1d4 rounds.
#LPUSH misfire_template {{params.target}} finds his lungs filled with water; he must make a PE check or die.  If they make it, they can do nothing but cough and sputter for 1d4 rounds
#LPUSH misfire_template {{params.target}} begins whistling “Whistle While {{params.target}} Work.” Lasts for 1d4 rounds.
#LPUSH misfire_template Technicolour hailstorm. 1d4 icy stones of various colours, doing 1d6 HP of damage each, hit all those within 50\' of {{params.target}}.  The storm lasts for 1d4 rounds.
#LPUSH misfire_template {{params.target}} is turned Invisible, as per Invisibility, and Paralyzed at the same moment. This lasts for 1d4 rounds.
#LPUSH misfire_template One randomly chosen creature within 50\' of {{params.target}} will automatically score a critical for the next 2d4 rounds.
#LPUSH misfire_template {{params.target}}\'s hands turn into +5 magical melee weapons appropriate for her primary weapon. {{params.target}} may attack as per their WP.  The hands return to normal after 5 rounds.
#LPUSH misfire_template A giant (6\' tall) rubber ducky falls out of the sky to land between {{params.target}} and {{params.target}} with a loud “SQWEEKEE.”  It vanishes after 1d6 rounds.
#LPUSH misfire_template {{params.target}} thinks her favorite weapon/wand/other long skinny object has turned into a poisonous snake. This lasts for 1d6 rounds.
#LPUSH misfire_template {{params.target}} begins sneezing.  No spells can be cast until fit passes. (1d6 rounds)
#LPUSH misfire_template Everyone within 200 feet of the {{params.target}} becomes completely invulnerable for 2d6 rounds.
#LPUSH misfire_template {{params.target}} jumps in a random direction d3x20 feet. {{params.target}} cannot jump more than 20 feet backwards.
#LPUSH misfire_template A New Orleans Brass Band materialized from thin air plays a funeral march and dissipates into thin air again.  Every action stops during the music.  Everybody has to reroll initiative afterwards.
#LPUSH misfire_template {{params.target}} notice a small chest full of gold and jewelry standing a few feet from you.  The gold is real and it is worth about 25,000 gold pieces.
#LPUSH misfire_template Each gold piece in the {{params.target}}\'s possession turns into the equivalent value in copper pieces.
#LPUSH misfire_template A well dressed violinist steps out from a shadow and plays a song for you, when he\'s finished he bows, turns around and implodes.
#LPUSH misfire_template As you cast the spell you burst into flames (same as the spell) for 1d4 melees.
#LPUSH misfire_template {{params.target}} loose control of yourself and your brilliant DM can do as he pleases with your character for 1d4 melees.
#LPUSH misfire_template For 1d4 melees you become completely weightless.  According to the universal laws of physics, if you make any movement, you will leave the ground and fly, but after the weightlessness wears off your body weight is increased by 100 pounds per level of your experience.  If you were flying, you now will fall back to the ground.  The increased weight lasts 4d4 melees.
#LPUSH misfire_template 20 naked male dwarves surround you.  {{params.target}} have to make a Horror Factor of 18.  They disappear after 1d6 melees.
#LPUSH misfire_template The magic energies are warped and directed at you instead and your body starts to burn taking 5d6 points of damage every melee for 1d6 melees.
#LPUSH misfire_template {{params.target}}\'re attack by a whole nest of wild bees.  The attack lasts for 1d6 melees.
#LPUSH misfire_template Every stone within a 50 ft radius starts jumping in all directions; if there are boulders present they might even hurt someone unless a dodge vs 14 is made each melee.  (Damage 2d6)  The stones stop jumping after 3d6 melees.
#LPUSH misfire_template Somehow you cast the spell Metamorphosis: Insect, on yourself and see the world from a snail\'s point of view for 1d8 melees.
#LPUSH misfire_template A nearby wand/rod/staff doubles in size (retaining its magical properties). If cut in half, both pieces become Wands of Random Spells and each has half the original number of charges.
#LPUSH misfire_template A nearby tree becomes sentient and is under the control of the {{params.target}}. It may attack immediately if the {{params.target}} chooses. This lasts for 1 turn. However, if the tree dies, the {{params.target}} also dies.
#LPUSH misfire_template The {{params.target}} becomes slightly translucent.  There is no physical effect (they are still completely corporeal,) and the {{params.target}} gains no ghost-like abilities.
#LPUSH misfire_template {{params.target}} realize that you\'re blasted on dwarven moonshine. (-4/-40%) {{params.target}}\'re drunk for 1d12 hours and have terrible a hangover for 1d8 hours with half of the penalties.
#LPUSH misfire_template Small licks of flame shoot from {{params.target}}\'s fingertips. These do no damage but can ignite flammables.
#LPUSH misfire_template A rain of fish starts with you in the center.  1d6 fish fall from the sky per square yard/melee.  Each does only 1 point of damage.  The duration of the rain is 1 melee/level, but the fish stay until eaten or rotten.  The \'storm\' has a radius of 2 miles.
#LPUSH misfire_template All of the {{params.target}}\'s stats are randomly redistributed, except their prime requisites.
#LPUSH misfire_template The {{params.target}} becomes incapable of standing still for the next 10 minutes.
#LPUSH misfire_template Something smells peaceful here.  {{params.target}} summon a cloud of marijuana smoke, covering 100 ft radius.  Duration: 1 hour per level.  Victims will loose their thrill to fight and become very peacefully loving and dreaming.  Only a save vs poison will help, but it must be repeated every 10 minutes.
#LPUSH misfire_template {{params.target}} polymorphs into a fish appropriate to the area, or a random type if no fish are in the area. 40% chance for a monster type.  If {{params.target}} is not near water they will suffocate in 3 minutes.
#LPUSH misfire_template All of your belongings, real estate included, are turned yellow for 1d4 minutes.
#LPUSH misfire_template {{params.target}} collapses and appears to be dead. He is not, however, but you have no desire to discover this. He\'ll wake up and be fine in 1d6 minutes.
#LPUSH misfire_template Suddenly you find yourself surrounded by a pack of frenzied hungry northern timber wolves.
#LPUSH misfire_template The {{params.target}}\'s eyes change colour temporarily.  Roll 1d6 for colour.  1=brown, 2=grey, 3=blue, 4=green, 5=yellow, 6=combination. (Roll twice, ignore any sixes.)
#LPUSH misfire_template A small apple tree materializes in front of you. It is about 6 ft high and planted in a large pot. The tree has a glittery aura and if examined closer by a magic user it will radiate powerful magic, in fact the whole tree is extremely magic. The tree monthly grows 1d6 red glass-like apples each containing 50 ISP The tree has to be kept in a suitable environment or it\'ll die. This plant is of a magic, practiced by the Titans and some Elves and Dragons during the elf-dwarf wars, long forgotten called; "Th\'aghf Zathciuwa\'gh Ghathyur\'eigh" or " The way of the trees". If not treated properly the tree will die. Once the apples are picked they will last for centuries. There are no cores in the apples, once each century the tree will grow one green apple (containing 2000 ISP!!!) that can be planted to yield another 1d8 trees.  There is a 1% chance that the tree has a green apple when it materializes.
#LPUSH misfire_template As the spell loses its effect you feel something pulling your very genes and in a moment\'s notice you find yourself transformed into a cute little piglet. (1d3 months.)
#LPUSH misfire_template All spells cast during the next round will last 10 times longer than normal. Do not inform {{params.target}} of this.
#LPUSH misfire_template Suddenly you know how to create the mysterious Cyclops lightning shafts!!! Why not try it out…(I hope all GM\'s are familiar with what happens if anyone does this…)
#LPUSH misfire_template All non-living items in a 10-foot radius of {{params.target}} are sliced into 1-inch cubes by radiant force fields (except ethereal creatures). Magic Items get a save at +2.  Appropriate effects should a magic item be destroyed by this.
#LPUSH misfire_template {{params.target}} hear a whistling sound above your head.  A shell from a WWII howitzer is dimensionally teleported to this world and explodes 50 yards above your heads.  Spreading shrapnel over a 200-yard radius.  60% chance of taking 8d6 points of damage, 30% chance of starting a fire.  {{params.target}} are deafened for 1d6 minutes, if you survive that is.
#LPUSH misfire_template {{params.target}} grow claws, horrible black, non-retractable claws. (Dam 2d6+2)  They may be removed by a remove curse, if you find a priest that can be convinced you\'re a good guy that is.
#LPUSH misfire_template {{params.target}} change your eye-colour randomly through the common colours for your race.  (Lasts 1d10 weeks)
#LPUSH misfire_template {{params.target}} find yourself equipped with bat-like wings making it possible for you to glide up to 1 mile under good conditions.  The wings fall off after 1d3 weeks.
#LPUSH misfire_template Until now it wasn\'t all that hard, but since you cast that spell...{{params.target}} have constipation for 1d3 weeks.
#LPUSH misfire_template {{params.target}} are now a beautiful (PB 29) female elf with long blond (IQ 5) hair (if you were male.)  If you were female, you are now a brute (PS 29, alignment: miscreant) male ogre also with IQ 5.  And I offer you 1000 extra XP for playing in character.  Duration 1d4 weeks.
#LPUSH misfire_template Well sort of, your pockets always seem to be filled with golden coins.  Same as fool\'s gold lasts for 1d4 weeks.
#LPUSH misfire_template {{params.target}} develop blisters.  First on your hands and a few days later your arms.  After a week your entire body is covered and the blisters begin to turn into sores.  {{params.target}} realize only too late that you\'ve caught the disease leprosy.  Unless magically treated you will die in 1d6 weeks.
#LPUSH misfire_template {{params.target}}r head is turned backwards for the first time in your life, and pleased as you are to see your own behind, after a while it becomes quite uncomfortable.  Lasts 1d6 weeks.
#LPUSH misfire_template {{params.target}} are instantly turned into a thorny shrubbery with small blue flowers and red berries.  {{params.target}} may think and speak.  Lasts 1d6 weeks.
#LPUSH misfire_template The {{params.target}} blends into his surroundings almost perfectly.  While the effect is in place they gain the benefit of a 98% hide/camouflage ability while motionless.  Lasts 1d6 weeks.
#LPUSH misfire_template {{params.target}}r body becomes infested with all kinds of parasites that can literally be seen crawling all over you.  Roll save vs. insanity every week, minimum 2x.  Lasts 1d6 weeks.
#LPUSH misfire_template The {{params.target}} is surrounded by a continual, soft glow of bluish white light; makes sneaking in the dark impossible and is frightening to children and superstitious individuals.
#LPUSH misfire_template A magic picture box comes into your possession.  See Terry Pratchett\'s The Colour of Magic for details.
#LPUSH misfire_template {{params.target}} is forced to speak in rhyme for 1d12 rounds.  Cannot cast spells.
#LPUSH misfire_template All creatures slain by the {{params.target}} in the last 24 hours rise up as Revenants and attempt to destroy him/her. All undead have their original abilities and skills.
#LPUSH misfire_template The {{params.target}} is overcome by severe stomach cramping.  They suffer a -2 to attack rolls and -5 to skills.
#LPUSH misfire_template {{params.target}}r mind gets twisted.  {{params.target}} lose 1d6 skills but you gain 1d6 other skills.
#LPUSH misfire_template {{params.target}} forget 2 random skills.  But hey they are not lost for nothing.  {{params.target}} can distribute their percentage numbers on the rest of your skills.
#LPUSH misfire_template The {{params.target}}\'s upper lip curls into a sneer.  They are incapable of making any other facial expression for the next hour.  While the effect lasts they are at a -4 to Charm/Impress/Trust rolls.
#LPUSH misfire_template {{params.target}} gains the ability to see magic for a month. The sensitivity is so great that if she looks at a +5 or greater item she is flash-blinded for d4 rounds. She should probably invest in Ray-Bans.
#LPUSH misfire_template {{params.target}} become a toad for 3d6 melees.  Only your body changes, not your clothes nor other possessions.
#LPUSH misfire_template The {{params.target}}\'s teeth become elongated, sharp, and pointed.  (Think Ferengi.)  The strange teeth do not affect most in-game situations, but a DM might rule that they provide some circumstance penalties in social situations.
#LPUSH misfire_template The {{params.target}} emits steam and mist for the next hour.  The steam is harmless and easily dispersed by movement or even a light breeze, but a DM might rule that the steam provides some circumstance penalties to skill checks in social situations.
#LPUSH misfire_template 2D100 pieces of gold rain down in a 30\' radius of {{params.target}}. Anyone caught in the radius takes 1d20 points of damage from the falling coins until they are outside the radius.  Coins vanish after 1d10 turns.
#LPUSH misfire_template 1d10 small stones shoot from the {{params.target}}\'s fingertips and orbit the {{params.target}}\'s head. They are under the {{params.target}}\'s control, as to speed and direction.  They orbit for 1d10 turns.
#LPUSH misfire_template {{params.target}}\'s associates all turn green whenever they come within 5 feet of her for the next 2d10 turns.
#LPUSH misfire_template {{params.target}}\'s skin turns hard as a diamond and will be immune to slash and puncture attacks. This does not affect his AR or HP, but only lasts 2 turns.
#LPUSH misfire_template {{params.target}}\'s feet enlarge, reducing movement to 1/2 normal and -4 to all initiative rolls for 1d3 turns.
#LPUSH misfire_template {{params.target}}\'s feet enlarge, reducing movement to 1/2 normal and adding -4 to initiative rolls for 1d3 turns.
#LPUSH misfire_template Sudden change in weather (temperature raise/fall, snow, rain, etc) lasting 1d6 turns.
#LPUSH misfire_template All those within 50 feet of {{params.target}} who have any special vision (night, infra, dark, etc.) lose it, and all who don\'t, gain Nightvision for 1d6 turns.
#LPUSH misfire_template {{params.target}} develops allergy to his magical items.  Character cannot control sneezing until all magical items are removed.  Allergy lasts 1d6 turns.
#LPUSH misfire_template The {{params.target}}\'s toes enlarge to 3x their normal size, ruining footwear and inflicting 1d10 points of damage and reduce the {{params.target}}\'s SPD to 50% of normal. If the {{params.target}} is wearing metal footwear (or something else which wouldn\'t normally be destroyed) 1d10 toes are broken. Toes return to normal size after 1d8 turns.
#LPUSH misfire_template A war hammer flies at the {{params.target}}, strikes at +10 and does critical damage. It then disappears.
#LPUSH misfire_template The {{params.target}} is buried to the chest in offal that oozes from a gate that spontaneously appears.
#LPUSH misfire_template A unicorn offers to be your steed, if you are of a good alignment.  An evil character on the other hand finds themselves covered with 2d8 hungry tinder spiders.
#LPUSH misfire_template {{params.target}} becomes hysterically religious for one month, believing herself to be an Avatar of some previously unknown god(dess) and will try to convert followers.
#LPUSH misfire_template An earthquake comes to visit the area surrounding you (300-yard radius, 6+ on the Richter scale.)  Buildings shake and will crumble.  I hope you are not indoors.
#LPUSH misfire_template A devil/angel duo appears on the {{params.target}}\'s shoulder, and advises them appropriately as to what to do for the next 1d10 hours.
#LPUSH misfire_template 13 common pixies make your and your friends life miserable for 2d20 hours.
#LPUSH misfire_template {{params.target}}\'s hair thickens and grows 4 yards long in 4 rounds. {{params.target}} must part the hair to see. The hair is impossible to damage for d3 hours.
#LPUSH misfire_template All spells are exchanged between the minds of the {{params.target}} and the {{params.target}} if they are both spell {{params.target}}s. If not, the {{params.target}} Forgets all her spells for the next 24 hours.
#LPUSH misfire_template The {{params.target}} is struck by the effect of drinking 10 mugs of ale.  They become intoxicated and suffer the appropriate penalties for 1d4 hours.
#LPUSH misfire_template {{params.target}} appear to have been awarded with Armour of Ithan, but you don\'t know for how long.  (1d6 hours.)
#LPUSH misfire_template The {{params.target}}\'s tongue grows to 3 feet in length.  They cannot speak properly and must make an ME check to cast spells.  Lasts 1d6 hours
#LPUSH misfire_template The {{params.target}} begins to sweat profusely.  They suffer no in-game effect, but my have a small circumstance penalty to social situations.  Lasts 1d6 hours.
#LPUSH misfire_template Amnesia hits you like a hammer and you can\'t even remember who you are for 4d6 hours.
#LPUSH misfire_template Hits you like a lightning strike from a clear sky.  Lasts for 1d8 hours.
#LPUSH misfire_template The {{params.target}} emits the effects of a fear spell on creatures within 30 feet for the next 1d8 hours.
#LPUSH misfire_template The true name of the person next to you is revealed, but s/he also gets to know yours.
#LPUSH misfire_template A yellow mushroom grows out of the {{params.target}}\'s right ear over the course of two rounds. It is edible but tastes like wax. {{params.target}} must make a ME roll or be distracted during the process.
#LPUSH misfire_template {{params.target}} can do nothing but laugh uncontrollably for d8 rounds, but they are also healed of 1d8 HP in the process.
#LPUSH misfire_template {{params.target}} is cooled to absolute zero and may shatter if hit. {{params.target}} must make a successful PE check at –10 to survive the thawing process.
#LPUSH misfire_template The {{params.target}} grows a 3-foot long beard.  If the {{params.target}} already has a beard, it falls out instead.  The beard falls out after an hour regardless.
#LPUSH misfire_template All claws and nails within 30 feet of {{params.target}} are filed short and blunt, making them harmless.
#LPUSH misfire_template {{params.target}} repeat the spell 1d4 times in the same melee. (Subtract spells/day for all the spells...although even if you don\'t have enough, the spell still repeats.)
#LPUSH misfire_template Sweet music fills the air, produced by a nearby flower (if there aren\'t any one grows first). The flower will never die, even if picked, continuing to sing forever and the tune never repeats.
#LPUSH misfire_template The spell has a minor healing effect.  It restores an additional 1d4 HP in addition to its normal effects.
#LPUSH misfire_template Spell functions, but cannot be controlled by {{params.target}} (DM determines effects).
#LPUSH misfire_template {{params.target}} is sprayed with mostly harmless insecticide. Does 5d10 hits of damage to large insect/insect-like creatures, kills small insects.
#LPUSH misfire_template The next living creature the {{params.target}} touches loses 3 points of PE, which is added to {{params.target}}\'s.
#LPUSH misfire_template {{params.target}} gains power of speech in the {{params.target}}\'s native language (98%) and High Intelligence (racial maximum.) This also applies to inanimate objects (IQ on an inanimate object is same as {{params.target}}\'s.)
#LPUSH misfire_template All of {{params.target}}\'s actions for 2d4 turns are accompanied by theme music and pop-up balloons containing his thoughts.
#LPUSH misfire_template All plants within 30 feet try to kill you for 1d6 minutes. (Same as Animate Plants.)
#LPUSH misfire_template The {{params.target}}\'s clothing becomes sentient for 2 weeks, refusing to leave the {{params.target}}\'s warm, comfortable body and complaining loudly if treated roughly or exposed to uncomfortable elements.
#LPUSH misfire_template All {{params.target}}\'s coins are transformed into pearls (100 GP base value). They will remain pearls until 2 hours after they are sold or traded to someone else, then return to normal. They cannot be used as spell components.
#LPUSH misfire_template {{params.target}} find that your nose has turned into 24 carat gold.  May be removed by a remove curse, or sold.  Lower PB by 1d3 points.
#LPUSH misfire_template {{params.target}} grow gills and cannot breath air anymore.  {{params.target}} must find a large body of water within 3 minutes or die from suffocation.  Luckily for you the gills work in both salt and fresh water.  Lower PB by 1d6 points.
#LPUSH misfire_template If you have lost any SDC or hit-points, you are totally healed, if you have lost any limbs, they are restored, if you have any diseases, they are gone, if you are poisoned, you are healthy again. But if you were completely healthy, well, you\'ll lose half your SDC and hit-points
#LPUSH misfire_template {{params.target}} vomit uncontrollably for 1d6 melees producing a strange green foul smelling thick liquid taking 2d4 points of damage directly to your hit points.
#LPUSH misfire_template All grass in a 160 square foot area around {{params.target}} grows uncontrollably. If there was no grass previously, a well-manicured lawn sprouts.
#LPUSH misfire_template The earth rumbles for 1d4 minutes (1-2 on the Richter scale) 100 yd radius.
#LPUSH misfire_template Incapacitating green gas comes out of the {{params.target}}\'s ears and floats in the {{params.target}}\'s general direction. All those between {{params.target}} and {{params.target}} must make a save vs spell at {{params.target}}\'s level vs. Poison or fall unconscious.
#LPUSH misfire_template A 10-foot diameter boulder rises from the ground directly under the {{params.target}}. Footing is precarious.
#LPUSH misfire_template The {{params.target}} is easily distracted and influenced.  For the next 10 minutes they suffer a -1 penalty to all ME saving throws.
#LPUSH misfire_template The next sword that hits your body will simply slide through and you will not suffer any damage.  This particular sword will not be able to hit you for the next 1d10 days.
#LPUSH misfire_template {{params.target}} instantly double the number of spells/day you can cast.  Lasts 1d3 days.
#LPUSH misfire_template The intended spell functions but consumes 1d6 of the {{params.target}}\'s spells for the day. If this exceeds the {{params.target}}\'s available spells, they cannot cast spells for the next 1d3 days.
#LPUSH misfire_template {{params.target}} really look twisted now.  {{params.target}}r arms and legs change their position for 1d4 days.
#LPUSH misfire_template {{params.target}} summon forth a beautiful Angel (Female Seraph if you are male; Male Ariel if you are female) which says \'I\'m here to do everything you want me to do."  It stays with you for 1d4 days.
#LPUSH misfire_template {{params.target}} summon forth a beautiful Succubus (Female Succubus if you are male; Male Incubus if you are female) which says \'I\'m here to do everything you want me to do."  It stays with you for 1d4 days.
#LPUSH misfire_template {{params.target}} receive a natural AR of 15 since your skin is turned into bronze scales for 1d6 days.
#LPUSH misfire_template All magic items within 60 feet of {{params.target}} wiggle when touched for the next 1d6 days.
#LPUSH misfire_template {{params.target}}r skin is turned transparent, (horror factor 10) lasts for 1d8 days.
#LPUSH misfire_template A large mirror appears in front of the {{params.target}}. If the {{params.target}} tries to get around it his mirror image emerges from the mirror and engages him in combat.
#LPUSH misfire_template The {{params.target}}\'s footwear animates and grows teeth for 3d4 rounds. These teeth will attack everything within range, causing the {{params.target}} to kick the nearest person. Treat as combat.
#LPUSH misfire_template The {{params.target}}\'s pack/robes whatever ignites for 1d4 rounds. {{params.target}} takes fire damage every round unless she removes the source of the flame or renders herself immune to natural flame/heat.
#LPUSH misfire_template {{params.target}}\'s stomach is emptied; she becomes ravenously hungry and must stop to eat.
#LPUSH misfire_template {{params.target}} inflates like a balloon for d4 rounds and deflates for another d4 rounds. This only affects living material up to 1000 pounds and will not float.
#LPUSH misfire_template The {{params.target}} drains the {{params.target}} of as many hit points as are required to put the {{params.target}} at maximum. The {{params.target}} will regain these lost hit points if the {{params.target}} is killed, and is aware of this fact.
#LPUSH misfire_template In some strange way you automatically loose the initiative for 1d8 melees.  But the spell works and has double effect.
#LPUSH misfire_template Spell takes physical form of free-willed elemental and cannot be controlled by {{params.target}}.  Elemental remains for duration of spell.  Touch of the elemental causes spell effect.
#LPUSH misfire_template {{params.target}} gains 5000 experience points and generates another random effect.
#LPUSH misfire_template {{params.target}} has foreknowledge of the next 3 unstable effects, but the information is only 75% correct.
#LPUSH misfire_template The {{params.target}} and all of her party are transported to another site of conflict.
#LPUSH misfire_template 1d10 small fireballs (1d6 dam each) erupt from your face and fly in random directions.  30% chance of hitting anyone within 30 feet.
#LPUSH misfire_template 1d6 of your friends get to save vs. magic if they fail they\'ll fall into a mindless frenzy and go berserk for 1d4 melees slashing out at anyone within 5 feet.
#LPUSH misfire_template Marbles appear on the floor next to the {{params.target}}. {{params.target}} will have to make PP rolls at -3 every round to stay on his feet.
#LPUSH misfire_template Either {{params.target}} or {{params.target}} must reduce all their statistics to the lowest one; 90% {{params.target}}, 10% {{params.target}}.
#LPUSH misfire_template The next time {{params.target}} says the word “Blind,” “Kill,” or “Stun,” it acts as though a Power Word has been spoken with. Let the {{params.target}} name the {{params.target}}.
#LPUSH misfire_template Some random body part of the {{params.target}} becomes invisible. This is permanent unless dispelled at the level of the {{params.target}}.
#LPUSH misfire_template A 10x10 pit appears immediately in front of {{params.target}}.  5\' deep per level of the {{params.target}}.
#LPUSH misfire_template All bonuses (regardless of type i.e. + to strike, save, etc.) are negated for 2d10 rounds for all creatures within 100 feet of the {{params.target}}.
#LPUSH misfire_template All creatures within 120 feet of the {{params.target}} teleport to random other positions within 120 feet of the {{params.target}}.
#LPUSH misfire_template A golem is created from the nearest appropriate substance. 50/50 chance it will obey or attack the {{params.target}}.
#LPUSH misfire_template {{params.target}}\'s form turns gaseous for 1d4 rounds. A good gust of wind will disperse the cloud and kill the {{params.target}}.
#LPUSH misfire_template A random something cold to drink is immediately provided to everyone in a 100-foot radius from the {{params.target}}. 
#LPUSH misfire_template A random something warm to drink is immediately provided to everyone in a 100-foot radius from the {{params.target}}. 
#LPUSH misfire_template There is an immediate random encounter with a monster hostile to the {{params.target}}.
#LPUSH misfire_template A bucket of green slime appears over {{params.target}}\'s head and dumps the slime all over the {{params.target}}.
#Illusion: " All creatures hostile to the {{params.target}} in a 60\' radius are Glamoured to see each other as the {{params.target}}.
#LPUSH misfire_template Nearest dead body within 60 yards of the {{params.target}} becomes a Zombie and attacks the {{params.target}}.
#LPUSH misfire_template 4d10 (10 minimum) 1 gp base value uncut gems shoot from the {{params.target}}\'s fingertips at the {{params.target}}.
#LPUSH misfire_template {{params.target}} is covered with tar and feathers. 50% chance {{params.target}} will stop what he\'s doing and taunt and laugh hysterically at the {{params.target}}.
#LPUSH misfire_template {{params.target}} is teleported 30 feet directly above {{params.target}} and will fall the next round. +30 Fall/Crush, and {{params.target}} may be hit if she fails to notice the falling {{params.target}}!
#LPUSH misfire_template {{params.target}}s circulatory system jumps out and runs away. Oddly, this has no ill effect on {{params.target}}.
#LPUSH misfire_template {{params.target}} names anything desired (not more than 10th level in effect), and GM rolls a 50/50 chance it will happen to {{params.target}} or {{params.target}}.
#LPUSH misfire_template Re-roll, but the effect doesn\'t happen right now. Instead, one of {{params.target}}\'s fingernails falls off. The re-roll takes affect when the nail is discarded or destroyed and always affects {{params.target}}, even if the surge says ‘{{params.target}}.\'
#LPUSH misfire_template The spell fails but the {{params.target}} believes it affected the {{params.target}} to the maximum possible effect (if the max possible is death, the {{params.target}} must choose a new {{params.target}}.)
#LPUSH misfire_template {{params.target}}r magic has upset the very forces of nature.  1d8 minor elementals turn up to give you and your party a lesson you may not be able to forget.
#LPUSH misfire_template {{params.target}} sweats buckets for a month, and must drink at least 3 liters of water per day or lose one point of Temporary PE for each day the water requirement is not met.
#LPUSH misfire_template The whole party is suddenly in a desert.  {{params.target}} can hear the sound of a distant battle raging through the air.  If you look closer you can see a battle going on in a valley.  There are only humans that are part of this battle.  (DM: The characters have been teleported to 900 AD during the Middle Eastern Crusades.)  The group will remain in this dimension for 1d4 days and will then be teleported back to the same place and time as they left.
#LPUSH misfire_template {{params.target}} instantly know the answer to the next 1d10 questions anybody will ask you, and the answers are all right.
#LPUSH misfire_template {{params.target}} chooses one object within 100\' to heat up to 200 degrees Fahrenheit.
#LPUSH misfire_template {{params.target}} reverse your alignment for 1d6 days...Maybe, just maybe, you\'ll like it.
#LPUSH misfire_template Desired spell at twice your effective level.  (If you are multi-classed, add all your levels together and double it.)
#LPUSH misfire_template {{params.target}} are permanently blinded in one eye. (High=Right, Low=Left.  If character is already blind in that eye, this will cure it.)
#LPUSH misfire_template One of your legs turns out to be made of pine.  Permanent, although a remove curse or a saw can remove it.
#LPUSH misfire_template A mad count has you contracted for assassination without apparent reason, but the good thing is that you\'re aware of it.
#LPUSH misfire_template A Joton makes you his enemy and comes looking for you.  In some strange way you\'re aware of it.
#LPUSH misfire_template the laws of reality forget the spell\'s cost and you don\'t have to spend any of your spells/day casting it.
#LPUSH misfire_template The ground between the {{params.target}} and the {{params.target}} turns to molten lava. All creatures touching the 5\' by 10\' strip of lava will take damage as per River of Lava at the {{params.target}}\'s full level, every round they are in contact with it. 
#LPUSH misfire_template A flash, a puff of smoke and a little pink frog.  That is all that remains of your spell. (Remove it from the list, you\'ve forgotten it.)
#LPUSH misfire_template The spell Mute is mistakenly laid on the nearest person to you, subtract cost for it.
#LPUSH misfire_template A creature of light/dark appears and will agree to become the {{params.target}}\'s familiar if they request it.
#LPUSH misfire_template The next person you tell your name to will instantly attack you, but you know it.
#LPUSH misfire_template A well is created beside you.  This may be a wishing well, so lets try it!
#LPUSH misfire_template The {{params.target}} grows scales all over their body.  Roll 1d6 to determine the colour of the scales 1=blue, 2=black, 3=green, 4=red, 5=yellow, 6=brown.  Scales last 1d10 weeks and then the {{params.target}} is overcome with an unbearable itchiness and is compelled to scratch at them, unless they make a successful PE roll.  PB is temporarily reduced by 1d6 during the molt.
#LPUSH misfire_template All rock within a 20\' radius of {{params.target}} turns to a random metal (whatever ore is most prevalent).
#LPUSH misfire_template A magic ring turns up on your index finger (+1 vs spell magic, perm: anent.)
#LPUSH misfire_template {{params.target}} are drained of all your spells, but this creates a ley-line nexus at the place you are standing, with ley-lines stretching out 500 miles north, east, south and west.  Duration: 1d8 years or permanent (?)
#LPUSH misfire_template {{params.target}} becomes immortal.  When he dies he loses 5 points of PE and rises from the dead at the next midnight.  This continues until his PE becomes 0, at which time he becomes a Revenant, which will hunt down the {{params.target}}.  Remove Curse at 1/3 normal will cure the {{params.target}}, however the PE loss is permanent.
#LPUSH misfire_template A five-mile long 200-yard wide 500-yard deep hole in the ground opens up a short distance away.  Permanent.
#LPUSH misfire_template A bard in a nearby town writes a hit-song about your groups\' heroic deeds, which results that in a year or two each existing group members\' renown will be increased by 1 point.
#LPUSH misfire_template {{params.target}} shoots a web at the {{params.target}}, becoming entangled.  The {{params.target}} is one (possibly the only) anchor point.
#LPUSH misfire_template Everybody within 50 feet of {{params.target}} and {{params.target}} starts singing bawdy drinking songs for 1d10 rounds. Everyone affected must make a save vs. magic or become friends. Those who make their save may Ambush those who don\'t.
#LPUSH misfire_template A barrel of syrup appears in the air above the {{params.target}}\'s party and empties itself on the first person to notice it.  (Person who made their PER by the most amount.)
#LPUSH misfire_template Sometimes a spell goes wrong, very wrong and this is one of those times.  If you are a male then you are from this day on impotent, but if you are a woman, you are pregnant, whether you want it or not.
#LPUSH misfire_template Graffiti reading “<{{params.target}}\'s name> was here!” appears on {{params.target}} written in ink. Ink is visible even if {{params.target}} is not.
#LPUSH misfire_template Two humans in strange dark-blue uniforms appear in front of you.  They say: "We are here to arrest you.  {{params.target}} have certain rights: {{params.target}} have the right to call an attorney; you have the right to say nothing.  If you say anything, this might and will be used against you in the court."  They walk towards you and in the very moment they touch you they disappear.  Who knows, maybe one day they\'ll be back to fulfill their attempt.
#LPUSH misfire_template {{params.target}} is teleported home/to lair/etc. There is a possibility of error as per Teleport.
#LPUSH misfire_template a messenger delivers a full size portrait of you shortly after the spell has been cast.
#LPUSH misfire_template From this day and for 1d10 weeks, all of your spells cost only 1/2 of what they should to cast.
#LPUSH misfire_template The intended spell appears to fail when cast, but will go off the next time {{params.target}} uses a spell in addition to the spell they are attempting to cast.
#LPUSH misfire_template Heavy storms appear from nowhere and last for 1d3 days, affecting a 1d4 mile radius from where you stood when the spell was cast.
#LPUSH misfire_template {{params.target}} leaves monster shaped footprints instead of his own until a dispel magic is cast.
#LPUSH misfire_template Fireball, conditional as per the spell, {{params.target}} can name the condition that triggers the blast.
#LPUSH misfire_template A petrification is mistakenly laid on one of your companions.  Subtract the appropriate cost.
#LPUSH misfire_template Since you weren\'t concentrating hard enough the spell fails and you loose half a spell cost.
#LPUSH misfire_template {{params.target}} may cast a spell of her choice of 14th level or less, instantaneously. Give the player 10 timed seconds to choose.  No spell cost.
#LPUSH misfire_template A fireball is also directed at your {{params.target}}.  Same level as you.  Subtract spell cost.
#LPUSH misfire_template {{params.target}} is the subject of a Rust spell; all non-magical metal on the {{params.target}} must save or be reduced to dust.
#LPUSH misfire_template The {{params.target}}\'s hair grows a foot in length.  The growth is permanent, unless cut.
#LPUSH misfire_template A net falls on the {{params.target}} and they becomes so entangled they will have to be cut out.
#LPUSH misfire_template A wall of flame, effective level 7 is instantly created 10 feet behind you.
#LPUSH misfire_template The earth beneath your feet opens up and you fall 30 yards down a hole taking 9d6 points of damage.  After two minutes the hole closes and if you\'re still there, only the gods can save you.
#LPUSH misfire_template The next person of your opposite sex that you encounter will insist on mating with you.
#LPUSH misfire_template A loud bang with the strength of thunder booms from above you and a new roll for initiative has to be made by any person standing within 150 yards from you.
#LPUSH misfire_template the next priest of darkness you encounter casts a random curse upon you.
#LPUSH misfire_template {{params.target}} find yourself in a black small room.  {{params.target}} can see light peeking in from a crack in what might be a door.  If you open the door you realize that a cupboard must have materialized around you.  The cupboard is of good quality and has several sets of fine tailored clothes in it.  Everything fits as if made for you.
#LPUSH misfire_template Luck sees you as a promising piece in the game and awards you an automatic successful dodge/save against the next supernatural attack directed at you.
#LPUSH misfire_template An Iron golem steps up to you and explains that he\'s ready to serve you now.
#LPUSH misfire_template The {{params.target}} of your spell will be turned to solid gold for 1d4 days.  No saving throw.
#LPUSH misfire_template An order of outcast magicians in the Wolfen Empire sends you their greetings and an invitation to their annual celebration of the equinox.
#LPUSH misfire_template {{params.target}} gains infravision (or some other unusual vision if he already has infravision) but loses all normal vision.  This lasts for 1 day.
#LPUSH misfire_template {{params.target}} has a vision of the players around a table, rolling dice, playing a game. This lasts for one round.  They are affected by a sense of ennui for the rest of the day.
#LPUSH misfire_template As you feel the ripple of the magic energies swirling through your conscious mind, something goes wrong.  {{params.target}} forget the incantation for 1d4 weeks.  The desired spell works as it should\'ve, it has 5x the effect and burns off 3 of your spells for the day.
#LPUSH misfire_template Wild surge triggers the casting of another randomly chosen spell.  Uses up it\'s own \'spell/day\'
#LPUSH misfire_template {{params.target}} cannot sleep or rest properly for 1d3 weeks and in that time you cannot recover any ISP, or spells/day.
#LPUSH misfire_template The spell you cast will repeat itself at the same time of the day for 3d6 days.  Spell cost will of course have to be subtracted.  If you\'re out of spells the spell won\'t repeat that day.
#LPUSH misfire_template A solar eclipse occurs (or lunar if nighttime). This lasts the rest of the night/day.
#LPUSH misfire_template The next time the PC\'s enter a town the inhabitants will try to chase them away.
#LPUSH misfire_template A spriggan disguised as a gnome comes up to you and asks what\'s wrong with that stone circle a few hundred yards away.
#LPUSH misfire_template A randomly chosen item on the {{params.target}}\'s person sprouts wings and flies away.
#LPUSH misfire_template {{params.target}}\'s arm stretches out and slaps the {{params.target}} across the face. This could be quite entertaining in a crowded bar when the {{params.target}} is 50 feet away.
#LPUSH misfire_template {{params.target}} is covered in earwigs. These do no damage but are likely to greatly annoy the {{params.target}} and gross everyone else out as they drop off his body and scurry away.
#LPUSH misfire_template A random person within 100 feet is made ethereal. Unless they are familiar with the ethereal plane they may not realize what has happened and will not be able to return unless shown the way.
#LPUSH misfire_template A nearby cemetery is accidentally affected by a powerful raise the dead spell producing 10d8 skeletons that set off to terrorize the countryside.  The creatures will kill all living beings that get in their way.
#LPUSH misfire_template {{params.target}}\'s tongue grows long enough to touch the tip of her nose. If her tongue is already that long, the surge affects some other part of her body.
#LPUSH misfire_template The {{params.target}} is covered with plate armour (AR 18). Any other armour worn falls off.  This lasts for 1d4 rounds then the armour disappears (but the original armour does not reappear on the {{params.target}}\'s body!) 
#LPUSH misfire_template A meteorite streaks out of the sky and hits {{params.target}} for 5d10+50 hit points. (If underground, waits until exposed to sky.)
#LPUSH misfire_template Thick dust covers {{params.target}}, 50% chance {{params.target}} is allergic to it and starts sneezing uncontrollably.
#LPUSH misfire_template {{params.target}} gains the use of Turn Undead (at 100%) for one time only. It need not be used immediately.
#LPUSH misfire_template {{params.target}} gains a random harmful (for him) miscellaneous magic time, which takes effect immediately.
#LPUSH misfire_template A juvenile dragon of a random type flies onto the scene and acts appropriately.
#LPUSH misfire_template {{params.target}} emits a powerful fart which does 1d10 damage to the {{params.target}}, propels her 10 feet forward, and remains where the {{params.target}} was and acts like a Stun Cloud for 1d4 rounds. Any non-magical trousers are ruined completely.
#LPUSH misfire_template A maddened tribe of trolls set out in order to make dinner of you, but in some strange way you\'re aware of their plans and can act accordingly.
#LPUSH misfire_template {{params.target}} grow a 3rd eye on your forehead.  As a result of this mutation you can see the aura of other people automatically.
#LPUSH misfire_template {{params.target}} screams (wasting a round, though voice or breath weapon attacks take effect automatically).
#LPUSH misfire_template A call lightning at twice your level also hits your {{params.target}}, in addition to the spell working normally.
#LPUSH misfire_template {{params.target}} may gamble up to 5 points of her luck stat on a future saving throw. If the save succeeds, the points are not lost. If it fails, she loses the points and must regain them normally.
#LPUSH misfire_template {{params.target}}r eyes are turned into a neon pink liquid for 2d4 hours.  They still function normally.
#LPUSH misfire_template No one (except the {{params.target}}) can hear the {{params.target}} for 1d6 rounds. {{params.target}} can still hear normally.
#LPUSH misfire_template {{params.target}} loses all hair/fur/feathers/scales etc. Reaction is determined by {{params.target}}\'s race/outlook. Other effects determined by DM (flying will be tough without feathers). Whatever is lost grows back naturally.
#LPUSH misfire_template All magical weapons within 30\' of {{params.target}} lose their magical powers for 2 rounds only.
#LPUSH misfire_template Water sprays from the {{params.target}}\'s tear ducts like a water pistol, Water type: 1=normal, 2=holy, or 3=unholy.
#LPUSH misfire_template A doppelganger of yourself is instantly created 5 feet away from you.  The creature pays its humble respects and wanders off to see the world.  (Lasts 1d3 years, Cannot be dispelled, no control is granted the {{params.target}}, usual restrictions apply)
#LPUSH misfire_template {{params.target}} develops an irritating rash for 1d4 rounds and has to scratch incessantly.
#LPUSH misfire_template All spells cast by the {{params.target}} in the next 24 hours will become unstable, permanently.
#LPUSH misfire_template The next time the PC\'s enter a town the inhabitants will try any method available, short of imprisonment, to try to get the PC\'s to live there permanently.
#LPUSH misfire_template {{params.target}} grow pointed ears like an elf, if you are an elf, your ears grow to double size, permanently.
#LPUSH misfire_template {{params.target}} Shrinks, as per the spell, but to 1/12th her original size, permanently.
#LPUSH misfire_template {{params.target}} find yourself to be the next victim of a secret death cult located near your home.  {{params.target}} are aware of this but you do not have the faintest idea of how you became aware.  Today is the perfect day for writing your testimony.
#LPUSH misfire_template A vorpal guillotine blade flies from the {{params.target}}\'s hands and strikes the {{params.target}} with a +5.  If a critical is obtained, the creature is decapitated and the head falls into a magically appearing basket. The creature gets its normal Dodge/Parry.
#LPUSH misfire_template {{params.target}} seem to have caught a rather common deadly disease; PLAGUE! (Bubonic that is.)  Unless properly treated you\'ll die within 3 weeks.  Sorry.
#LPUSH misfire_template 1d10 skeletons under the {{params.target}}\'s control rise up out of the ground and attack the {{params.target}} (this may anger the {{params.target}}\'s deity!).
#LPUSH misfire_template The {{params.target}} suffers from a distracting cough.  For the next 10 minutes they must make a ME roll to cast a spell.  While the cough lasts, they suffer a -15% to their prowl ability.
#LPUSH misfire_template The only thing you remember is that you were about to cast a spell and that a shimmering turquoise light engulfed you.  {{params.target}}r friends on the other hand have a completely different tale to tell: Suddenly you disappeared and were gone until now. (1d12 days have passed.) No one knows what really happened to you during this time, but you have a strange feeling that someone else can see, hear, smell and feel all that you experience.  It seems as though you have been abducted by something or someone...Roll save vs random insanity.
#LPUSH misfire_template One of your insanities is magically cured; if you have none then it\'s time to roll for one now.  ({{params.target}} get a save vs. insanity.)
#LPUSH misfire_template Somehow, from now on you are the most notorious spell-{{params.target}} in the whole universe.  Everybody everywhere will know your name and picture.  The reaction of the people, whenever you enter a community will either be respectful or hateful, depending on the view of magic they have in this community.
#LPUSH misfire_template Handedness of {{params.target}} is reversed. {{params.target}} must take time to switch hands or suffer the appropriate penalty.
#LPUSH misfire_template {{params.target}} and all others within 30 feet are instantly teleported to a location totally alien for the party.
#LPUSH misfire_template An angry minor earth elemental rises from the ground to kill your party.