
self.redis.lpush('curse_kind', 'bezerker')
self.redis.lpush('curse_kind', 'narcolepsy')
self.redis.lpush('curse_kind', 'fanatic')
self.redis.lpush('curse_kind', 'greed')
self.redis.lpush('curse_kind', 'hubris')
self.redis.lpush('curse_kind', 'addiction')
self.redis.lpush('curse_kind', 'penalty')
self.redis.lpush('curse_kind', 'derp')
self.redis.lpush('curse_kind', 'yawning')
self.redis.lpush('curse_kind', 'submission')
self.redis.lpush('curse_kind', 'lethargy')
self.redis.lpush('curse_kind', 'bigspender')
self.redis.lpush('curse_kind', 'truthteller')
self.redis.lpush('curse_kind', 'precious')
self.redis.lpush('curse_kind', 'braddoro')
self.redis.lpush('curse_kind', 'karrius')
self.redis.lpush('curse_kind', 'quint')
self.redis.lpush('curse_kind', 'ibiwan')
self.redis.lpush('curse_kind', 'greenimposter')
self.redis.lpush('curse_kind', 'mabdelnour')
self.redis.lpush('curse_kind', 'trammelle')
self.redis.lpush('curse_kind', 'jamangai')
self.redis.lpush('curse_kind', 'phobic')
self.redis.lpush('curse_kind', 'babbler')
self.redis.lpush('curse_kind', 'kudla')
self.redis.lpush('curse_kind', 'toolio')
self.redis.lpush('curse_kind', 'sleepless')
self.redis.lpush('curse_kind', 'agro')
self.redis.lpush('curse_kind', 'blinding')
self.redis.lpush('curse_kind', 'butterfinger')
self.redis.lpush('curse_kind', 'cleese')
self.redis.lpush('curse_kind', 'deathscent')
self.redis.lpush('curse_kind', 'deathspite')
self.redis.lpush('curse_kind', 'decaying')
self.redis.lpush('curse_kind', 'doublevision')
self.redis.lpush('curse_kind', 'drowning')
self.redis.lpush('curse_kind', 'echo')
self.redis.lpush('curse_kind', 'fashionista')
self.redis.lpush('curse_kind', 'festering')
self.redis.lpush('curse_kind', 'forgetful')
self.redis.lpush('curse_kind', 'habitualliar')
self.redis.lpush('curse_kind', 'halfhearted')
self.redis.lpush('curse_kind', 'humming')
self.redis.lpush('curse_kind', 'itchy')
self.redis.lpush('curse_kind', 'leadenedleg')
self.redis.lpush('curse_kind', 'lostmojo')
self.redis.lpush('curse_kind', 'maximumpain')
self.redis.lpush('curse_kind', 'misfiring')
self.redis.lpush('curse_kind', 'misplacing')
self.redis.lpush('curse_kind', 'muted')
self.redis.lpush('curse_kind', 'pacifistic')
self.redis.lpush('curse_kind', 'princely')
self.redis.lpush('curse_kind', 'puedelathos')
self.redis.lpush('curse_kind', 'reflectedsins')
self.redis.lpush('curse_kind', 'respondent')
self.redis.lpush('curse_kind', 'seashell')
self.redis.lpush('curse_kind', 'sexybeast')
self.redis.lpush('curse_kind', 'shakyhands')
self.redis.lpush('curse_kind', 'singletasking')
self.redis.lpush('curse_kind', 'skippy')
self.redis.lpush('curse_kind', 'smoothness')
self.redis.lpush('curse_kind', 'spinny')
self.redis.lpush('curse_kind', 'startling')
self.redis.lpush('curse_kind', 'stutterer')
self.redis.lpush('curse_kind', 'tonguetied')
self.redis.lpush('curse_kind', 'trueself')
self.redis.lpush('curse_kind', 'truthteller')
self.redis.lpush('curse_kind', 'tunnelvision')

# The Bezerker Curse ____________
HSET curse_kind_description bezerker  {"name":"bezerker", "description":"causes intermittent, uncontrollable rage in the victim"  }
HSET curse_kind_description narcolepsy  {"name":"narcolepsy", "description":"causes the victim to fall asleep in stressful situations"   }
HSET curse_kind_description fanatic  {"name":"fanatic", "description":"causes overzealous feeling of love or hate towards a single random person, action or thing"   }
HSET curse_kind_description greed  {"name":"greed", "description":"causes the victim to take unnecessary risks for treasure"   }
HSET curse_kind_description hubris  {"name":"hubris", "description":"causes the victim to overvalue their ability"   }
HSET curse_kind_description addiction  {"name":"addiction", "description":"causes the victim to grow overly dependent on an action or thing"   }
HSET curse_kind_description penalty  {"name":"disadvantaged", "description":"causes victim to perform poorly at everything" }
HSET curse_kind_description derp  {"name":"derp", "description":"causes the victim to become noticeably stupider than everyone around"   }
HSET curse_kind_description yawning  {"name":"yawning", "description":"causes uncontrollable, loud yawning"   }
HSET curse_kind_description submission  {"name":"submission", "description":"will randomly submit to anyone disagreeing or displaying force"   }
HSET curse_kind_description lethargy  {"name":"lethargy", "description":"causes the victim to perform poorly at physical tasks"  }
HSET curse_kind_description bigspender  {"name":"big spender", "description":"causes victim to overcompensate when making purchases"   }
HSET curse_kind_description truthteller  {"name":"truth teller", "description":"prevents you from lying, bending or ommitting the truth"   }
HSET curse_kind_description precious  {"name":"precious", "description":"causes paranoia relating to theft of an item"   }
HSET curse_kind_description braddoro  {"name":"braddoro", "description":"causes a preoccupation with juvenile jokes, and uncontrollable giggles"   }
HSET curse_kind_description karrius  {"name":"carrius", "description":"causes an obnoxious preoccupation with random topics that no one cares about"   }
HSET curse_kind_description quint  {"name":"quint", "description":"causes the victim to randomly berate and threaten friends and colleagues"   }
HSET curse_kind_description ibiwan  {"name":"ibiwan", "description":"causes inability to comprehend being wrong, even if it leads to death"   }
HSET curse_kind_description greenimposter  {"name":"greenimposter", "description":"causes the victim to suddenly believe their are unqualified for whatever task is at hand"   }
HSET curse_kind_description mabdelnour  {"name":"mabdelnour", "description":"causes random shortness of breath and inability to run" }
HSET curse_kind_description trammelle  {"name":"trammelle", "description":"causes fits of rage when any filth is left on a glossy surface and a compulsion to clean it"   }
HSET curse_kind_description jamangai  {"name":"jamangai", "description":"causes the victim to feel compelled to one-up others"   }
HSET curse_kind_description phobic  {"name":"phobic", "description":"causes irrational fear of one or more things"   }
HSET curse_kind_description babbler  {"name":"babbler", "description":"causes incessant, uncontrollable talking that becomes worse with stressful situations"   }
HSET curse_kind_description kudla {"name":"kudla", "description":"causes the victim\'s skin to secrete a disgusting, oozing slime"   }
HSET curse_kind_description toolio {"name":"toolio", "description":"causes the victim extreme discomfort when being decisive or making decisions"   }
HSET curse_kind_description unlucky  {"name":"unlucky", "description":"causes the victim to become unlucky when they don\'t have their lucky charm"  }
HSET curse_kind_description sleepless  {"name":"sleepless", "description":"prevents the victim from resting through mundane or magical means"  }


HSET curse_kind_description agro  {"name":"agro", "description":"causes enemies to always target the victim"  }
HSET curse_kind_description blinding  {"name":"blinding", "description":"causes decay of sight"  }
HSET curse_kind_description butterfinger  {"name":"butterfinger", "description":"prevents the victim from griping anything for more than 30 seconds"  }
HSET curse_kind_description cleese  {"name":"cleese", "description":"causes the victim to walk strangely, reducing movement and stealth"  }
HSET curse_kind_description deathscent  {"name":"death scent", "description":"causes the victim to reek of death, frightening nearby animals"  }
HSET curse_kind_description deathspite  {"name":"death spite", "description":"causes dying enemies within range to get one last attack against the victim before dying"  }
HSET curse_kind_description decaying  {"name":"decaying", "description":"causes physical rotting and losing a bit of health each day"  }
HSET curse_kind_description doublevision  {"name":"double vision", "description":"causes the victim to see double (disadvantage in combat and perception)"  }
HSET curse_kind_description drowning  {"name":"drowning", "description":"causes prevents the victim from remembering how to swim"  }
HSET curse_kind_description echo  {"name":"", "description":"causes the victim to randomly parrot phrases"  }
HSET curse_kind_description fashionista  {"name":"fashionista", "description":"causes the victim to become are uncomfortable in whatever clothing or armor they are wearing (at a disadvantage while wearing it)"  }
HSET curse_kind_description festering  {"name":"festering", "description":"causes the victim to become resistant to healing"  }
HSET curse_kind_description forgetful  {"name":"forgetful", "description":"become forgetful when trying to recall important things"  }
HSET curse_kind_description habitualliar  {"name":"habitual liar", "description":"causes the victim to be strongly compelled to needlessly lie"  }
HSET curse_kind_description halfhearted  {"name":"half-hearted", "description":"causes the victim to strike in a minimally damaging way"  }
HSET curse_kind_description humming  {"name":"humming", "description":"causes the victim to unconsciously hum or sing"  }
HSET curse_kind_description itchy  {"name":"itchy ", "description":"causes the victim to develop a full body, insufferable rash in the presence of a specific catalyst"  }
HSET curse_kind_description leadenedleg  {"name":"leadened leg", "description":"causes the victim\'s leg to permanently fall asleep, reducing movement"  }
HSET curse_kind_description lostmojo  {"name":"lost mojo", "description":"prevents the victim from attuning or using magical items"  }
HSET curse_kind_description maximumpain  {"name":"maximum pain", "description":"causes an enemies damage to always maximized against the victim"  }
HSET curse_kind_description misfiring  {"name":"misfiring", "description":"causes a 25% chance of failure to properly cast a spell or use a ranged weapon"  }
HSET curse_kind_description misplacing  {"name":"misplacing", "description":"causes the victim to have a 5% chance of realizing a possession is missing when trying to use it"  }
HSET curse_kind_description muted  {"name":"muted", "description":"causes an inability to vocalize"  }
HSET curse_kind_description pacifistic  {"name":"pacifistic", "description":"causes the victim\'s hands to burn and blister while holding a weapon"  }
HSET curse_kind_description princely  {"name":"princely", "description":"causes the victim to be polymorphed into a talking animal."  }
HSET curse_kind_description puedelathos  {"name":"puedelathos", "description":"causes a 50% chance to automatically fail any successful saving throw"  }
HSET curse_kind_description reflectedsins  {"name":"reflected sins", "description":"causes any damage inflicted on an opponent to be mirrored on the victim"  }
HSET curse_kind_description respondent  {"name":"respondent", "description":"causes the victim to repeat a phrase in response to a trigger"  }
HSET curse_kind_description seashell  {"name":"seashell", "description":"causes the victim\'s hearing to be replaced with the roar of the ocean"  }
HSET curse_kind_description sexybeast  {"name":"sexy beast", "description":"causes the victim to release mating hormones of random nearby creatures"  }
HSET curse_kind_description shakyhands  {"name":"shaky hands", "description":"causes a 25% chance to drop whatever the victim is holding in combat situations"  }
HSET curse_kind_description singletasking {"name":"single-tasking", "description":"prevents the victim from performing more than one action at a time."  }
HSET curse_kind_description skippy  {"name":"skippy", "description":"causes the victim to forget how to walk (but can still skip)"  }
HSET curse_kind_description smoothness  {"name":"smoothness", "description":"causes all hair, feathers, spines or scales fall off the victim"  }
HSET curse_kind_description spinny  {"name":"spinny", "description":"prevents walking or running in a straight line, reducing movement"  }
HSET curse_kind_description startling  {"name":"startling", "description":"causes the victim to always be surpised in new combat situations"  }
HSET curse_kind_description stutterer  {"name":"stutterer", "description":"causes the victim to develop an incomprehensible stutter "  }
HSET curse_kind_description tonguetied  {"name":"tonguetied", "description":"causes the victim to grow a fleshy webbing that holds their tongue down, impeding speech"  }
HSET curse_kind_description trueself  {"name":"true self", "description":"causes the victim to gradually morph cosmetically into another race"  }
HSET curse_kind_description truthteller  {"name":"truthteller", "description":"causes the victim to be strongly compelled to tell the complete truth"  }
HSET curse_kind_description tunnelvision  {"name":"tunnel vision", "description":"causes the victim to lose peripheral vision (disadvantage in combat and perception)"  }



# The effects of the curse _____________.
ZADD curse_duration   5  {"name":"appear intermittently", "score":5  }
ZADD curse_duration  10  {"name":"are temporary",         "score":10  }
ZADD curse_duration  40  {"name":"last for a few minutes at a time",    "score":40  }
ZADD curse_duration  50  {"name":"last for several minutes at a time",  "score":50  }
ZADD curse_duration  60  {"name":"last for an hour at a time",          "score":60  }
ZADD curse_duration  70  {"name":"last for a few hours at a time",      "score":70  }
ZADD curse_duration  95  {"name":"last several hours at a time",    "score":95  }
ZADD curse_duration  96  {"name":"last a day",            "score":96  }
ZADD curse_duration  97  {"name":"last a few days",       "score":97  }
ZADD curse_duration  98  {"name":"last a week",           "score":98  }
ZADD curse_duration  99  {"name":"last weeks",            "score":99  }
ZADD curse_duration 100  {"name":"last a lifetime",       "score":100 }


# ...and can only be undone by ___________

self.redis.lpush('curse_removal', 'a remove curse spell')
self.redis.lpush('curse_removal', 'a restoration spell')
self.redis.lpush('curse_removal', 'performing an appropriate selfless act')
self.redis.lpush('curse_removal', 'performing a blood sacrifice')
self.redis.lpush('curse_removal', 'destroying a related artifact')
self.redis.lpush('curse_removal', 'undoing the action that lead to the curse')
self.redis.lpush('curse_removal', 'passing the curse on to another')
self.redis.lpush('curse_removal', 'killing the one who cursed you')
self.redis.lpush('curse_removal', 'undoing the original cause')
self.redis.lpush('curse_removal', 'performing an epic task')


self.redis.lpush('curse_template', 'The {{params.kind_description[\'name\']|title}} Curse {{params.kind_description[\'description\']}}. The effects of the curse {{params.duration[\'name\']}}.')
self.redis.lpush('curse_template', 'The {{params.kind_description[\'name\']|title}} Curse {{params.kind_description[\'description\']}}. Nothing else is known about it.')
self.redis.lpush('curse_template', 'The {{params.kind_description[\'name\']|title}} Curse {{params.kind_description[\'description\']}}.')
self.redis.lpush('curse_template', 'The {{params.kind_description[\'name\']|title}} Curse {{params.kind_description[\'description\']}}, and can only be undone by {{params.removal}}.')
self.redis.lpush('curse_template', 'The {{params.kind_description[\'name\']|title}} Curse {{params.kind_description[\'description\']}}, and can only be undone by {{params.removal}}. Untreated, the effects of the curse {{params.duration[\'name\']}}.')
