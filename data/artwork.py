

# How do we lay out artwork?


self.redis.lpush('artwork_metal', 'copper')
self.redis.lpush('artwork_metal', 'silver')
self.redis.lpush('artwork_metal', 'electrum')
self.redis.lpush('artwork_metal', 'gold')
self.redis.lpush('artwork_metal', 'brass')
self.redis.lpush('artwork_metal', 'steel')
self.redis.lpush('artwork_metal', 'aluminum')

#gems pulled from Gem.py

#color pulled from elsewhere

self.redis.lpush('artwork_weapon', 'dagger')
self.redis.lpush('artwork_weapon', 'sword')
self.redis.lpush('artwork_weapon', 'axe')
self.redis.lpush('artwork_weapon', 'spear')
#do we really want more ceremonial weapons?


self.redis.lpush('artwork_item', 'mug')
self.redis.lpush('artwork_item', 'statuette')
self.redis.lpush('artwork_item', 'cup')
self.redis.lpush('artwork_item', 'harp')
self.redis.lpush('artwork_item', 'music box')
self.redis.lpush('artwork_item', 'comb')
self.redis.lpush('artwork_item', 'bottle')
self.redis.lpush('artwork_item', 'chalice')
self.redis.lpush('artwork_item', 'ewer')

self.redis.lpush('artwork_item_material', 'ivory')
self.redis.lpush('artwork_item_material', 'onyx')
self.redis.lpush('artwork_item_material', 'gold')
self.redis.lpush('artwork_item_material', 'bone')
self.redis.lpush('artwork_item_material', 'exotic wood')

self.redis.lpush('artwork_item_decoration', 'phoenix')
self.redis.lpush('artwork_item_decoration', 'dragon')
self.redis.lpush('artwork_item_decoration', 'tiger')
self.redis.lpush('artwork_item_decoration', 'bear')

self.redis.lpush('artwork_jewelry', 'ring')
self.redis.lpush('artwork_jewelry', 'circlet')
self.redis.lpush('artwork_jewelry', 'crown')
self.redis.lpush('artwork_jewelry', 'tiara')
self.redis.lpush('artwork_jewelry', 'pendant')
self.redis.lpush('artwork_jewelry', 'bracelet')
self.redis.lpush('artwork_jewelry', 'anklet')
self.redis.lpush('artwork_jewelry', 'chain')

self.redis.lpush('artwork_cloth_item', 'glove')
self.redis.lpush('artwork_cloth_item', 'vestments')
self.redis.lpush('artwork_cloth_item', 'tapestry')
self.redis.lpush('artwork_cloth_item', 'mantle')
self.redis.lpush('artwork_cloth_item', 'rug')

self.redis.lpush('artwork_cloth_material', 'velvet')
self.redis.lpush('artwork_cloth_material', 'silk')
self.redis.lpush('artwork_cloth_material', 'wool')
self.redis.lpush('artwork_cloth_material', 'leather')

self.redis.lpush('artwork_template', 'a necklace of {{params.gem.size}} {{params.gem.kind_description[\'name\']|pluralize(2)}}')
self.redis.lpush('artwork_template', '{{params.color}} {{params.item_material}} mask with several {{params.gem.kind_description[\'name\']|pluralize(2)}}')
self.redis.lpush('artwork_template', '{{params.metal}} {{params.item}} with {{params.gem.kind_description[\'name\']}} inlays')
self.redis.lpush('artwork_template', '{{params.item_material}} {{params.item}}')
self.redis.lpush('artwork_template', 'Carved harp of {{params.item_material}} with {{params.gem.kind_description[\'name\']}} gems')
self.redis.lpush('artwork_template', 'ceremonial {{params.metal}} {{params.weapon}} with a {{params.gem.kind_description[\'name\']}} in the pommel')
self.redis.lpush('artwork_template', '{{params.metal}}-embroidered {{params.cloth_item}}')
self.redis.lpush('artwork_template', 'embroidered and bejeweled {{params.cloth_item}}')
self.redis.lpush('artwork_template', 'embroidered {{params.clothmaterial}} {{params.cloth_item}} with numerous {{params.gem.kind_description[\'name\']|pluralize(2)}}')
self.redis.lpush('artwork_template', 'eye patch with mock eye of {{params.gem.kind_description[\'name\']}} and {{params.gem.kind_description[\'name\']}}')
self.redis.lpush('artwork_template', 'finely wrought small {{params.metal}} bracelet')
self.redis.lpush('artwork_template', '{{params.gem.kind_description[\'name\']}} {{params.jewelry}} on a fine {{params.metal}} chain')
self.redis.lpush('artwork_template', '{{params.metal}} and {{params.gem.kind_description[\'name\']}} {{params.jewelry}}')
self.redis.lpush('artwork_template', '{{params.metal}} {{params.item}} with {{params.gem.kind_description[\'name\']}}')
self.redis.lpush('artwork_template', '{{params.metal}} {{params.item_decoration}} {{params.item}} with {{params.gem.kind_description[\'name\']}} eye')
self.redis.lpush('artwork_template', '{{params.metal}} {{params.jewelry}} with four {{params.gem.kind_description[\'name\']|pluralize(2)}}')
self.redis.lpush('artwork_template', '{{params.metal}} {{params.item}}')
self.redis.lpush('artwork_template', 'jeweled {{params.jewelry}}')
self.redis.lpush('artwork_template', 'jeweled {{params.metal}} {{params.jewelry}}')

#large well-done wool tapestry
#old masterpiece painting
#{{params.gem.kind_description[\'name\']}} pendant on {{params.metal}} chain
#{{params.metal}} chalice with {{params.gem.kind_description[\'name\']}} gems
#{{params.metal}} comb with {{params.gem.kind_description[\'name\']}}
#{{params.metal}} {{item}}
#{{params.metal}}-plated steel longsword with jet jewel in hilt
#solid {{params.metal}} idol (10 lb.)




#amber amphora
#amber coffer
#amber miniature (of a female halfling) inlaid with fine steel
#amber miniature (of a ship) inlaid with fine steel
#amber miniature (of a unicorn) inlaid with copper
#amber statue (of a goddess of fate) wreathed in silver continual flame
#amethyst idol (of a goddess of chaos) inlaid with mithral
#amethyst miniature (of an angel)
#amethyst ring
#amethyst rod set with red-brown spinel
#a perfect rose in temporal stasis
#azurite box
#banded agate ewer inlaid with electrum
#banded agate ewer inlaid with platinum
#banded agate miniature (of a horse) set with hematite
#banded agate miniature (of a tree) set with freshwater pearl
#banded agate totem (of a totem charge)
#bloodstone box
#bloodstone dice (pair)
#bloodstone mask
#blue quartz bowl
#blue quartz medallion
#blue quartz stele inlaid with gold
#bolt of brass cloth
#bolt of bronze cloth
#bolt of copper cloth
#bolt of electrum cloth
#bolt of electrum cloth set with alexandrite
#bolt of electrum cloth set with amber
#bolt of electrum cloth set with amethyst
#bolt of electrum cloth set with chrysoberyl
#bolt of electrum cloth set with golden pearl
#bolt of electrum cloth set with golden yellow topaz
#bolt of electrum cloth set with jet
#bolt of electrum cloth set with pink pearl
#bolt of electrum cloth set with silver pearl
#bolt of electrum cloth set with tourmaline
#bolt of electrum cloth set with violet garnet
#bolt of electrum cloth set with white pearl
#bolt of fine cloth
#bolt of fine cloth threaded with brass
#bolt of fine cloth threaded with bronze
#bolt of fine cloth threaded with copper
#bolt of fine cloth threaded with fine steel
#bolt of fine cloth threaded with silver
#bolt of fine steel cloth
#bolt of gold cloth
#bolt of gold cloth set with alexandrite
#bolt of gold cloth set with aquamarine
#bolt of gold cloth set with black pearl
#bolt of gold cloth set with chrysoberyl
#bolt of gold cloth set with coral
#bolt of gold cloth set with deep green spinel
#bolt of gold cloth set with golden pearl
#bolt of gold cloth set with pink pearl
#bolt of gold cloth set with silver pearl
#bolt of platinum cloth
#bolt of platinum cloth set with alexandrite
#bolt of platinum cloth set with amethyst
#bolt of platinum cloth set with brown-green garnet
#bolt of platinum cloth set with deep green spinel
#bolt of platinum cloth set with golden yellow topaz
#bolt of platinum cloth set with jade
#bolt of platinum cloth set with jet
#bolt of platinum cloth set with pink pearl
#bolt of platinum cloth set with tourmaline
#bolt of platinum cloth set with white pearl
#bolt of silk
#bolt of silk threaded with brass
#bolt of silk threaded with bronze
#bolt of silk threaded with copper
#bolt of silk threaded with silver
#bolt of silver cloth
#bolt of silver cloth set with alexandrite
#bolt of silver cloth set with amber
#bolt of silver cloth set with black pearl
#bolt of silver cloth set with brown-green garnet
#bolt of silver cloth set with chrysoberyl
#bolt of silver cloth set with deep blue spinel
#bolt of silver cloth set with golden yellow topaz
#bolt of silver cloth set with jet
#bolt of silver cloth set with pink pearl
#bolt of silver cloth set with red-brown spinel
#bottle of exotic wine
#bottle of fine wine
#box of perfumed candles
#brass amulet
#brass armlet
#brass armlet set with sardonyx
#brass belt
#brass box
#brass bracelet
#brass brooch set with lapis lazuli
#brass buckle set with eye agate
#brass buckle set with lapis lazuli
#brass buckle set with rhodochrosite
#brass chainmail inlaid with gold
#brass chain set with freshwater pearl
#brass chain set with lapis lazuli
#brass chalice
#brass chest
#brass choker
#brass cloth cloak
#brass cloth coat
#brass cloth gloves
#brass cloth gown
#brass cloth hunter\'s cap
#brass cloth pennant
#brass cloth tabard
#brass cloth vest
#brass diadem set with moss agate
#brass diadem set with obsidian
#brass earrings set with malachite
#brass earrings set with turquoise
#brass figurine (of a halfling queen)
#brass flask inlaid with brass
#brass framed painting
#brass gauntlets inlaid with silver
#brass greatsword
#brass hairpin set with obsidian
#brass medallion set with chalcedony
#brass miniature (of a male dwarf wizard) set with obsidian
#brass music box
#brass orrery wreathed in continual flame
#brass pin set with eye agate
#brass plate armor
#brass plate armor inlaid with gold
#brass rapier
#brass ring set with lapis lazuli
#brass rod
#brass rod inlaid with fine steel
#brass shield wreathed in continual flame
#brass shuriken set with rhodochrosite
#brass sickle
#brass signet ring set with smoky quartz
#brass staff inlaid with silver
#brass statue (of a hart)
#brass statue (of a serpent)
#brass sundial inlaid with gold
#brass totem (of a totem charge)
#bronze armlet
#bronze bound book (blank)
#bronze bracers
#bronze bracers inlaid with platinum
#bronze brazier
#bronze brooch set with malachite
#bronze chain set with eye agate
#bronze chalice
#bronze chest
#bronze chime set with malachite
#bronze chime set with moss agate
#bronze cloth choker
#bronze cloth coat
#bronze cloth gloves
#bronze cloth gown
#bronze cloth pennant
#bronze cloth robe
#bronze cloth sash
#bronze cloth tabard
#bronze cloth vest
#bronze comb set with zircon
#bronze dagger inlaid with silver
#bronze decanter
#bronze decanter inlaid with copper
#bronze diadem set with blue quartz
#bronze dice (pair) set with banded agate
#bronze earrings set with azurite
#bronze earrings set with hematite
#bronze earrings set with rhodochrosite
#bronze earrings set with turquoise
#bronze ewer
#bronze flask inlaid with fine steel
#bronze font inlaid with gold
#bronze font wreathed in continual flame
#bronze framed painting
#bronze goblet set with chalcedony
#bronze hairpin set with moss agate
#bronze hairpin set with turquoise
#bronze longsword
#bronze longsword set with jade
#bronze mask set with citrine
#bronze medallion
#bronze miniature (of a tree) set with azurite
#bronze orrery
#bronze pendant set with malachite
#bronze ring set with obsidian
#bronze rod set with jasper
#bronze scepter inlaid with silver
#bronze scepter set with amethyst
#bronze scroll case
#bronze shield
#bronze shield set with deep blue spinel
#bronze skull
#bronze statue (of a boar) inlaid with electrum
#bronze statue (of a god of good) inlaid with silver
#bronze statue (of a halfling sorcerer) wreathed in continual flame
#bronze stele
#bronze stele set with aquamarine
#bronze sundial
#bronze tiara
#bronze tiara inlaid with platinum
#bronze torc inlaid with fine steel
#bronze totem (of a totem charge)
#bronze urn
#brown-green garnet holy symbol (of a god of beauty)
#brown-green garnet ring
#carnelian ring
#carnelian scroll case
#carved ivory drinking horn
#carved ivory drinking horn inlaid with adamantine
#carved ivory drinking horn inlaid with bronze
#carved ivory drinking horn inlaid with copper
#carved ivory drinking horn inlaid with electrum
#carved ivory drinking horn inlaid with fine steel
#carved ivory drinking horn inlaid with gold
#carved ivory drinking horn inlaid with hepatizon
#carved ivory drinking horn inlaid with mithral
#carved ivory drinking horn inlaid with platinum
#carved ivory drinking horn inlaid with silver
#carved ivory drinking horn set with alexandrite
#carved ivory drinking horn set with aquamarine
#carved ivory drinking horn set with bloodstone
#carved ivory drinking horn set with chrysoprase
#carved ivory drinking horn set with coral
#carved ivory drinking horn set with deep blue spinel
#carved ivory drinking horn set with deep green spinel
#carved ivory drinking horn set with golden pearl
#carved ivory drinking horn set with golden yellow topaz
#carved ivory drinking horn set with jade
#carved ivory drinking horn set with jasper
#carved ivory drinking horn set with moonstone
#carved ivory drinking horn set with peridot
#carved ivory drinking horn set with red garnet
#carved ivory drinking horn set with rose quartz
#carved ivory drinking horn set with white pearl
#carved ivory drinking horn wreathed in continual flame
#carved ivory drinking horn wreathed in white continual flame
#carved wooden bowl
#carved wooden coffer
#carved wooden dice (pair)
#carved wooden ewer
#carved wooden figurine (of a cock)
#carved wooden figurine (of a male halfling warrior)
#carved wooden goblet
#carved wooden holy symbol (of a god of war)
#carved wooden idol (of a god of plants)
#carved wooden idol (of an air god)
#carved wooden jar
#carved wooden medallion
#carved wooden miniature (of a demonic goddess)
#carved wooden miniature (of a god of travel)
#carved wooden miniature (of a hydra)
#carved wooden miniature (of a phoenix)
#carved wooden necklace
#carved wooden orb
#carved wooden puzzle box
#carved wooden ring
#carved wooden staff
#carved wooden staff studded with brass
#carved wooden staff studded with bronze
#carved wooden staff studded with copper
#carved wooden staff studded with electrum
#carved wooden staff studded with fine steel
#carved wooden staff studded with gold
#carved wooden staff studded with platinum
#carved wooden staff studded with silver
#carved wooden statuette (of a god of magic)
#carved wooden sundial
#carved wooden urn
#ceramic bowl
#ceramic box
#ceramic coffer
#ceramic comb
#ceramic dice (pair)
#ceramic ewer
#ceramic figurine (of a demonic god)
#ceramic figurine (of a female human)
#ceramic holy symbol (of a god of chaos)
#ceramic holy symbol (of an undead god)
#ceramic idol (of a goddess of shadows)
#ceramic jar
#ceramic mask
#ceramic medallion
#ceramic miniature (of a god of plants)
#ceramic miniature (of a god of shadows)
#ceramic miniature (of a ship)
#ceramic orb
#ceramic ring
#ceramic rod
#ceramic scroll case
#ceramic statuette (of a god of strength)
#ceramic sundial
#ceramic vase
#chalcedony bowl inlaid with gold
#chalcedony coffer set with aquamarine
#chalcedony dice (pair)
#chalcedony holy symbol (of a goddess of light)
#chrysoberyl dice (pair)
#chrysoprase dice (pair)
#chrysoprase puzzle box
#citrine amphora
#citrine holy symbol (of a goddess of law) set with red-brown spinel
#citrine miniature (of a lion)
#citrine miniature (of a shark)
#citrine orb wreathed in red continual flame
#citrine stele
#copper amphora
#copper amphora inlaid with gold
#copper amphora set with aquamarine
#copper armlet
#copper bell set with bloodstone
#copper belt
#copper box
#copper bracelet
#copper bracers inlaid with gold
#copper brazier inlaid with platinum
#copper brazier inlaid with silver
#copper brooch set with turquoise
#copper censer
#copper chain set with azurite
#copper chalice
#copper chalice set with peridot
#copper chime set with hematite
#copper chime set with obsidian
#copper choker set with peridot
#copper circlet
#copper cloth choker
#copper cloth hunter\'s cap
#copper cloth tabard
#copper cloth vest
#copper coffer set with amber
#copper comb inlaid with copper
#copper comb set with jasper
#copper crown inlaid with electrum
#copper earrings set with eye agate
#copper flask
#copper framed painting
#copper gauntlets
#copper goblet
#copper greatsword
#copper helmet
#copper longsword scabbard
#copper longsword scabbard inlaid with gold
#copper mace
#copper medallion
#copper pin set with hematite
#copper plate armor inlaid with electrum
#copper rapier inlaid with silver
#copper rapier set with bloodstone
#copper ring set with banded agate
#copper ring set with eye agate
#copper ring set with freshwater pearl
#copper scepter
#copper scroll case
#copper shuriken set with lapis lazuli
#copper skull
#copper stele
#copper sundial
#coral box
#coral dice (pair) set with citrine
#coral jar
#coral urn
#crystal amphora inlaid with silver
#crystal ball
#crystal comb set with chalcedony
#crystal comb set with chrysoprase
#crystal comb set with jasper
#crystal dice (pair) set with blue quartz
#crystal dice (pair) set with hematite
#crystal dice (pair) set with rhodochrosite
#crystal ewer
#crystal figurine (of a female human jester)
#crystal figurine (of a goddess of fate)
#crystal goblet
#crystal holy symbol (of a goddess of luck)
#crystal holy symbol (of an air god) set with star rose quartz
#crystal idol (of a god of evil)
#crystal idol (of an air god) set with amber
#crystal medallion
#crystal medallion set with carnelian
#crystal miniature (of a tower) set with turquoise
#crystal necklace
#crystal pedestal inlaid with silver
#crystal puzzle box
#crystal puzzle box inlaid with electrum
#crystal statue (of a kraken) inlaid with gold
#crystal statuette (of a phoenix)
#crystal stele
#crystal totem (of a totem charge)
#crystal totem (of a totem charge) wreathed in continual flame
#crystal vase
#crystal vase set with red garnet
#deck of ivory tarot cards inlaid with electrum
#deck of ivory tarot cards inlaid with gold
#deck of ivory tarot cards inlaid with silver
#deep green spinel dice (pair)
#deep green spinel medallion
#deep green spinel scroll case
#deep green spinel statuette (of a lion) set with aquamarine
#dragonscale belt
#dragonscale belt set with aquamarine
#dragonscale belt set with deep blue spinel
#dragonscale boots
#dragonscale boots inlaid with gold
#dragonscale boots set with red-brown spinel
#dragonscale bound book (blank)
#dragonscale bound book (blank) set with aquamarine
#dragonscale bracers
#dragonscale bracers inlaid with mithral
#dragonscale choker
#dragonscale coat
#dragonscale coat inlaid with hepatizon
#dragonscale coinpurse
#dragonscale coinpurse inlaid with silver
#dragonscale coinpurse set with chrysoberyl
#dragonscale coinpurse set with coral
#dragonscale corset
#dragonscale corset inlaid with orichalcum
#dragonscale gloves
#dragonscale hunter\'s cap inlaid with gold
#dragonscale longsword scabbard
#dragonscale longsword scabbard wreathed in violet continual flame
#dragonscale pouch inlaid with electrum
#dragonscale pouch set with amber
#dragonscale ribbon
#dragonscale ribbon inlaid with bronze
#dragonscale ribbon inlaid with copper
#dragonscale ribbon inlaid with silver
#dragonscale ribbon set with bloodstone
#dragonscale ribbon set with chrysoprase
#dragonscale ribbon set with jasper
#dragonscale sash
#dragonscale sash inlaid with adamantine
#dragonscale sash wreathed in continual flame
#dragonscale shoes
#dragonscale shortsword scabbard
#dragonscale shortsword scabbard set with aquamarine
#dragonscale tabard
#dragonscale talisman
#dragonscale talisman inlaid with brass
#dragonscale talisman inlaid with bronze
#dragonscale talisman inlaid with copper
#dragonscale talisman set with bloodstone
#dragonscale talisman set with onyx
#dragonscale talisman set with peridot
#dragonscale talisman set with rock crystal
#dragonscale talisman set with zircon
#dragonscale vest inlaid with hepatizon
#dragonscale vest inlaid with silver
#ebony amphora
#ebony amphora inlaid with orichalcum
#ebony bowl
#ebony bowl inlaid with silver
#ebony comb
#ebony dice (pair)
#ebony dice (pair) set with citrine
#ebony ewer inlaid with gold
#ebony ewer inlaid with orichalcum
#ebony goblet
#ebony holy symbol (of an earth god)
#ebony mask
#ebony mask inlaid with gold
#ebony mask inlaid with silver
#ebony medallion
#ebony miniature (of a female dwarf)
#ebony miniature (of a fox)
#ebony miniature (of a halfling priestess)
#ebony miniature (of a male elf jester)
#ebony miniature (of a male human) inlaid with silver
#ebony miniature (of a phoenix) set with rose quartz
#ebony miniature (of a sphinx)
#ebony necklace inlaid with platinum
#ebony orb inlaid with electrum
#ebony orb inlaid with mithral
#ebony pedestal
#ebony puzzle box set with golden yellow topaz
#ebony ring
#ebony ring inlaid with brass
#ebony ring set with chalcedony
#ebony ring set with onyx
#ebony rod inlaid with gold
#ebony rod set with golden pearl
#ebony scroll case
#ebony statue (of a gnome sorceror) inlaid with mithral
#ebony stele
#ebony totem (of a totem charge) inlaid with orichalcum
#ebony urn wreathed in continual flame
#ebony vase set with black pearl
#electrum belt inlaid with hepatizon
#electrum brazier inlaid with silver
#electrum brooch
#electrum buckle set with peridot
#electrum chain
#electrum chain inlaid with brass
#electrum chainmail
#electrum chain set with onyx
#electrum choker inlaid with electrum
#electrum circlet
#electrum cloth choker
#electrum cloth cloak
#electrum cloth cloak set with brown-green garnet
#electrum cloth cloak set with pink pearl
#electrum cloth coat set with tourmaline
#electrum cloth gloves
#electrum cloth gown
#electrum cloth gown set with pink pearl
#electrum cloth hunter\'s cap
#electrum cloth pennant
#electrum cloth ribbon
#electrum cloth robe set with alexandrite
#electrum cloth robe set with amethyst
#electrum cloth robe set with black pearl
#electrum cloth robe set with deep green spinel
#electrum cloth tabard
#electrum cloth tabard set with jet
#electrum cloth talisman
#electrum cloth vest
#electrum dagger
#electrum dagger inlaid with gold
#electrum dice (pair)
#electrum dice (pair) inlaid with copper
#electrum dice (pair) set with bloodstone
#electrum figurine (of a god of illusions) set with tourmaline
#electrum flute
#electrum flute wreathed in violet continual flame
#electrum font
#electrum framed masterpiece painting
#electrum framed painting
#electrum hairpin set with peridot
#electrum hairpin set with zircon
#electrum helmet
#electrum longsword set with black pearl
#electrum medallion inlaid with silver
#electrum miniature (of a dwarf priest)
#electrum miniature (of a dwarf wench)
#electrum miniature (of a female gnome)
#electrum miniature (of a temple) inlaid with bronze
#electrum music box
#electrum necklace
#electrum pendant
#electrum pin
#electrum pin inlaid with silver
#electrum plate armor inlaid with adamantine
#electrum rapier
#electrum ring inlaid with fine steel
#electrum scepter wreathed in continual flame
#electrum scroll case inlaid with electrum
#electrum scroll case inlaid with silver
#electrum scroll case set with red-brown spinel
#electrum shield inlaid with orichalcum
#electrum shuriken
#electrum shuriken inlaid with copper
#electrum shuriken set with onyx
#electrum signet ring
#electrum staff
#electrum staff set with deep blue spinel
#electrum staff wreathed in continual flame
#electrum stele
#electrum stele inlaid with hepatizon
#electrum torc
#electrum urn inlaid with gold
#electrum warhammer
#ermine belt
#ermine belt inlaid with hepatizon
#ermine belt wreathed in continual flame
#ermine boots set with jet
#ermine boots set with pink pearl
#ermine bound book (blank)
#ermine bound book (blank) inlaid with silver
#ermine bracers
#ermine choker
#ermine choker inlaid with gold
#ermine cloak
#ermine cloak wreathed in violet continual flame
#ermine coat
#ermine coinpurse set with pink pearl
#ermine gloves inlaid with gold
#ermine gloves inlaid with platinum
#ermine mask
#ermine ribbon
#ermine ribbon inlaid with copper
#ermine ribbon inlaid with silver
#ermine ribbon set with iolite
#ermine ribbon set with moonstone
#ermine ribbon set with smoky quartz
#ermine sash
#ermine sash wreathed in continual flame
#ermine sash wreathed in white continual flame
#ermine shoes
#ermine shoes set with red spinel
#ermine shortsword scabbard
#ermine shortsword scabbard inlaid with gold
#ermine tabard inlaid with orichalcum
#ermine talisman
#ermine talisman inlaid with bronze
#ermine talisman inlaid with copper
#ermine vest
#ermine vest inlaid with electrum
#ermine vest inlaid with silver
#ermine vest set with deep blue spinel
#eye agate comb set with iolite
#eye agate miniature (of a ship) set with lapis lazuli
#feathered boots
#feathered bound book (blank)
#feathered bracers
#feathered choker
#feathered coinpurse
#feathered gloves
#feathered hunter\'s cap
#feathered mask
#feathered ribbon
#feathered sash
#feathered shoes
#feathered shortsword scabbard
#feathered talisman
#feathered vest
#fine cloth choker trimmed with ermine
#fine cloth cloak
#fine cloth cloak threaded with bronze
#fine cloth cloak threaded with fine steel
#fine cloth cloak threaded with platinum
#fine cloth cloak trimmed with sable
#fine cloth coat
#fine cloth coat threaded with brass
#fine cloth coat threaded with bronze
#fine cloth coat trimmed with ermine
#fine cloth gloves threaded with gold
#fine cloth gloves threaded with platinum
#fine cloth gloves trimmed with ermine
#fine cloth gloves trimmed with sable
#fine cloth gown
#fine cloth gown threaded with bronze
#fine cloth gown threaded with gold
#fine cloth gown threaded with silver
#fine cloth gown trimmed with ermine
#fine cloth gown trimmed with fox fur
#fine cloth gown trimmed with sable
#fine cloth hunter\'s cap threaded with electrum
#fine cloth hunter\'s cap threaded with gold
#fine cloth hunter\'s cap threaded with platinum
#fine cloth hunter\'s cap trimmed with sable
#fine cloth pennant threaded with copper
#fine cloth pennant threaded with fine steel
#fine cloth pennant threaded with platinum
#fine cloth pennant threaded with silver
#fine cloth pennant trimmed with ermine
#fine cloth pennant trimmed with sable
#fine cloth robe
#fine cloth robe threaded with electrum
#fine cloth robe threaded with silver
#fine cloth robe trimmed with fox fur
#fine cloth robe trimmed with sable
#fine cloth sash threaded with brass
#fine cloth sash threaded with copper
#fine cloth sash threaded with electrum
#fine cloth sash threaded with fine steel
#fine cloth sash threaded with gold
#fine cloth sash threaded with silver
#fine cloth sash trimmed with ermine
#fine cloth sash trimmed with fox fur
#fine cloth sash trimmed with sable
#fine cloth tabard
#fine cloth tabard threaded with fine steel
#fine cloth tabard threaded with gold
#fine cloth tabard threaded with platinum
#fine cloth tabard threaded with silver
#fine cloth tabard trimmed with fox fur
#fine cloth tabard trimmed with leopard fur
#fine cloth tabard trimmed with sable
#fine cloth vest threaded with bronze
#fine cloth vest threaded with gold
#fine cloth vest threaded with platinum
#fine cloth vest threaded with silver
#fine cloth vest trimmed with fox fur
#fine cloth vest trimmed with leopard fur
#fine cloth vest trimmed with sable
#fine leather belt
#fine leather boots
#fine leather bound book (blank)
#fine leather bound book (blank) set with golden pearl
#fine leather bracers
#fine leather cloak
#fine leather cloak set with alexandrite
#fine leather coat
#fine leather coat wreathed in continual flame
#fine leather coinpurse
#fine leather corset
#fine leather gloves
#fine leather gloves inlaid with fine steel
#fine leather hunter\'s cap
#fine leather longsword scabbard
#fine leather longsword scabbard wreathed in continual flame
#fine leather mask
#fine leather mask inlaid with brass
#fine leather pouch
#fine leather pouch inlaid with fine steel
#fine leather ribbon set with malachite
#fine leather ribbon set with moss agate
#fine leather ribbon set with obsidian
#fine leather ribbon set with rhodochrosite
#fine leather ribbon set with turquoise
#fine leather sash
#fine leather sash set with amber
#fine leather sash set with golden pearl
#fine leather sash set with red garnet
#fine leather shoes
#fine leather shortsword scabbard
#fine leather shortsword scabbard inlaid with electrum
#fine leather shortsword scabbard inlaid with silver
#fine leather tabard set with aquamarine
#fine leather tabard wreathed in continual flame
#fine leather talisman set with azurite
#fine leather talisman set with banded agate
#fine leather talisman set with eye agate
#fine leather talisman set with lapis lazuli
#fine leather vest
#fine steel amulet
#fine steel armband
#fine steel armlet
#fine steel bell
#fine steel bound book (blank)
#fine steel bracelet
#fine steel bracers inlaid with gold
#fine steel buckle set with azurite
#fine steel chain set with azurite
#fine steel chalice
#fine steel choker
#fine steel circlet
#fine steel cloth choker
#fine steel cloth coat
#fine steel cloth gown
#fine steel cloth hunter\'s cap
#fine steel cloth pennant
#fine steel cloth robe
#fine steel cloth sash
#fine steel cloth tabard
#fine steel cloth vest
#fine steel coffer
#fine steel dagger
#fine steel dagger inlaid with copper
#fine steel diadem set with obsidian
#fine steel earrings set with hematite
#fine steel earrings set with moss agate
#fine steel ewer set with pink pearl
#fine steel figurine (of a god of trickery)
#fine steel figurine (of a male gnome merchant) inlaid with copper
#fine steel flask set with sardonyx
#fine steel flask set with star rose quartz
#fine steel flute
#fine steel font
#fine steel font wreathed in continual flame
#fine steel greatsword
#fine steel mace
#fine steel mask
#fine steel medallion set with carnelian
#fine steel miniature (of a male human) set with blue quartz
#fine steel music box
#fine steel necklace
#fine steel necklace inlaid with brass
#fine steel pendant set with banded agate
#fine steel pin set with turquoise
#fine steel rapier
#fine steel ring set with freshwater pearl
#fine steel ring set with malachite
#fine steel scroll case
#fine steel shield
#fine steel shield wreathed in continual flame
#fine steel sickle
#fine steel signet ring
#fine steel staff
#fine steel statue (of a female halfling wizard) inlaid with silver
#fine steel statue (of a god of strength) set with violet garnet
#fine steel totem (of a totem charge) set with violet garnet
#fine steel warhammer inlaid with platinum
#fox fur boots
#fox fur boots set with bloodstone
#fox fur boots set with star rose quartz
#fox fur bound book (blank)
#fox fur bound book (blank) inlaid with electrum
#fox fur bound book (blank) set with chrysoberyl
#fox fur bracers
#fox fur choker
#fox fur cloak
#fox fur coinpurse
#fox fur corset
#fox fur corset inlaid with electrum
#fox fur corset inlaid with gold
#fox fur corset set with black pearl
#fox fur gloves
#fox fur gloves inlaid with bronze
#fox fur gloves inlaid with fine steel
#fox fur hunter\'s cap
#fox fur hunter\'s cap inlaid with fine steel
#fox fur hunter\'s cap set with sardonyx
#fox fur longsword scabbard
#fox fur mask
#fox fur pouch
#fox fur pouch set with star rose quartz
#fox fur ribbon set with blue quartz
#fox fur ribbon set with eye agate
#fox fur sash
#fox fur shoes
#fox fur shortsword scabbard
#fox fur shortsword scabbard inlaid with electrum
#fox fur tabard
#fox fur tabard inlaid with platinum
#fox fur tabard inlaid with silver
#fox fur tabard wreathed in continual flame
#fox fur talisman set with azurite
#fox fur talisman set with banded agate
#fox fur talisman set with hematite
#fox fur talisman set with lapis lazuli
#fox fur talisman set with moss agate
#fox fur talisman set with rhodochrosite
#fox fur talisman set with turquoise
#freshwater pearl amphora wreathed in continual flame
#freshwater pearl mask
#freshwater pearl miniature (of a god of darkness) set with lapis lazuli
#freshwater pearl vase
#gilded wooden amphora
#gilded wooden amphora inlaid with adamantine
#gilded wooden bowl
#gilded wooden comb inlaid with electrum
#gilded wooden comb set with coral
#gilded wooden dice (pair)
#gilded wooden dice (pair) inlaid with copper
#gilded wooden dice (pair) inlaid with fine steel
#gilded wooden dice (pair) set with chrysoprase
#gilded wooden dice (pair) set with onyx
#gilded wooden ewer
#gilded wooden ewer set with black pearl
#gilded wooden ewer wreathed in continual flame
#gilded wooden idol (of an undead goddess) wreathed in continual flame
#gilded wooden jar inlaid with hepatizon
#gilded wooden jar inlaid with platinum
#gilded wooden jar set with black pearl
#gilded wooden jar wreathed in white continual flame
#gilded wooden mask
#gilded wooden miniature (of a female elf)
#gilded wooden miniature (of a goddess of good)
#gilded wooden miniature (of a monstrous god)
#gilded wooden miniature (of a phoenix) set with chrysoprase
#gilded wooden miniature (of a unicorn) set with smoky quartz
#gilded wooden necklace inlaid with silver
#gilded wooden pedestal wreathed in silver continual flame
#gilded wooden puzzle box wreathed in continual flame
#gilded wooden ring
#gilded wooden ring inlaid with fine steel
#gilded wooden ring inlaid with silver
#gilded wooden ring set with bloodstone
#gilded wooden ring set with jasper
#gilded wooden scroll case set with white pearl
#gilded wooden statuette (of a god of ice) inlaid with hepatizon
#gilded wooden stele
#gilded wooden sundial inlaid with silver
#gilded wooden sundial wreathed in continual flame
#gilded wooden totem (of a totem charge)
#gilded wooden totem (of a totem charge) inlaid with adamantine
#gilded wooden urn inlaid with silver
#gilded wooden vase inlaid with mithral
#gilded wooden vase set with black pearl
#gilded wooden vase set with golden yellow topaz
#glass eye
#gold amphora
#gold armband
#gold box set with red garnet
#gold bracers
#gold brazier wreathed in silver continual flame
#gold breastplate wreathed in white continual flame
#gold brooch
#gold buckle
#gold candlesticks
#gold candlesticks inlaid with platinum
#gold chime
#gold choker
#gold choker set with amber
#gold cloth choker
#gold cloth cloak
#gold cloth cloak set with brown-green garnet
#gold cloth cloak set with chrysoberyl
#gold cloth cloak set with coral
#gold cloth coat
#gold cloth coat set with deep blue spinel
#gold cloth coat set with golden pearl
#gold cloth coat set with golden yellow topaz
#gold cloth gloves
#gold cloth gown
#gold cloth gown set with coral
#gold cloth hunter\'s cap
#gold cloth pennant
#gold cloth ribbon
#gold cloth robe
#gold cloth robe set with chrysoberyl
#gold cloth robe set with violet garnet
#gold cloth sash
#gold cloth tabard
#gold cloth tabard set with brown-green garnet
#gold cloth tabard set with golden pearl
#gold cloth tabard set with jade
#gold cloth vest
#gold coffer
#gold diadem
#gold dice (pair) inlaid with brass
#gold earrings
#golden pearl miniature (of a demon)
#golden pearl urn
#gold ewer
#gold figurine (of a boar) inlaid with platinum
#gold framed masterpiece painting
#gold framed painting
#gold gauntlets
#gold gauntlets wreathed in white continual flame
#gold greatsword inlaid with adamantine
#gold hairpin
#gold helmet inlaid with orichalcum
#gold helmet wreathed in continual flame
#gold holy symbol (of a fire god)
#gold holy symbol (of a goddess of magic)
#gold idol (of a god of evil) inlaid with silver
#gold mask
#gold miniature (of a drake)
#gold music box inlaid with orichalcum
#gold music box wreathed in silver continual flame
#gold necklace set with jade
#gold pendant
#gold pendant inlaid with copper
#gold pendant inlaid with fine steel
#gold pendant inlaid with silver
#gold pin
#gold plate armor
#gold ring
#gold scepter
#gold shield inlaid with mithral
#gold shortsword scabbard inlaid with platinum
#gold shuriken set with smoky quartz
#gold sickle
#gold signet ring
#gold signet ring set with deep green spinel
#gold skull
#gold statue (of a horse)
#gold stele
#gold torc
#gold urn set with deep blue spinel
#gold vase set with violet garnet
#hematite bowl
#hematite urn set with golden pearl
#iolite coffer wreathed in silver continual flame
#iolite comb set with coral
#iolite jar
#iolite orb
#iolite statue (of a badger) wreathed in red continual flame
#iolite statue (of a female halfling merchant)
#iolite totem (of a totem charge)
#iron amulet
#iron armband
#iron armlet
#iron bell
#iron belt
#iron bound book (blank)
#iron bracelet
#iron brazier
#iron brooch
#iron buckle
#iron censer
#iron chain
#iron chime
#iron choker
#iron coffer
#iron diadem
#iron dice (pair)
#iron earrings
#iron ewer
#iron figurine (of a raven)
#iron flask
#iron flute
#iron gauntlets
#iron goblet
#iron hairpin
#iron helmet
#iron holy symbol (of a goddess of magic)
#iron idol (of a god of strength)
#iron idol (of an aberrant god)
#iron longsword
#iron mask
#iron medallion
#iron orb
#iron pectoral
#iron pendant
#iron pin
#iron ring
#iron rod
#iron scroll case
#iron shortsword scabbard
#iron shuriken
#iron sickle
#iron signet ring
#iron skull
#iron sundial
#iron tiara
#iron torc
#iron vase
#ivory amphora
#ivory bowl
#ivory box
#ivory coffer
#ivory comb
#ivory dice (pair) set with freshwater pearl
#ivory dice (pair) set with lapis lazuli
#ivory dice (pair) set with malachite
#ivory dice (pair) set with turquoise
#ivory ewer
#ivory figurine (of a female elf) set with onyx
#ivory goblet set with citrine
#ivory mask
#ivory miniature (of a god of good) set with lapis lazuli
#ivory necklace inlaid with brass
#ivory pedestal
#ivory puzzle box inlaid with silver
#ivory ring set with obsidian
#ivory rod
#ivory statue (of a mastiff)
#ivory statuette (of a sphinx)
#ivory stele set with black pearl
#ivory stele wreathed in continual flame
#ivory sundial set with golden pearl
#ivory totem (of a totem charge) wreathed in continual flame
#jade ring inlaid with copper
#jade urn
#jasper coffer wreathed in blue continual flame
#jet statue (of a nature god)
#jet totem (of a totem charge) wreathed in green continual flame
#lacquered wooden box
#lacquered wooden box set with peridot
#lacquered wooden coffer inlaid with gold
#lacquered wooden coffer set with red spinel
#lacquered wooden comb inlaid with bronze
#lacquered wooden comb inlaid with copper
#lacquered wooden comb set with rose quartz
#lacquered wooden comb set with zircon
#lacquered wooden dice (pair) set with obsidian
#lacquered wooden dice (pair) set with turquoise
#lacquered wooden goblet inlaid with copper
#lacquered wooden holy symbol (of a god of plants)
#lacquered wooden mask inlaid with brass
#lacquered wooden medallion
#lacquered wooden miniature (of a gnome sorceror) set with banded agate
#lacquered wooden miniature (of a god of chaos) set with turquoise
#lacquered wooden miniature (of a male human) set with turquoise
#lacquered wooden miniature (of an eagle) set with banded agate
#lacquered wooden orb
#lacquered wooden orb set with brown-green garnet
#lacquered wooden ring set with azurite
#lacquered wooden ring set with banded agate
#lacquered wooden ring set with malachite
#lacquered wooden ring set with turquoise
#lacquered wooden rod inlaid with fine steel
#lacquered wooden scroll case
#lacquered wooden statue (of a god of war)
#lacquered wooden sundial set with jet
#lacquered wooden vase
#lapis lazuli puzzle box
#lapis lazuli rod
#lapis lazuli scroll case inlaid with fine steel
#large carpet
#large carpet threaded with brass
#large carpet threaded with bronze
#large carpet threaded with copper
#large carpet threaded with fine steel
#large carpet threaded with gold
#large carpet threaded with silver
#large tapestry
#large tapestry threaded with brass
#large tapestry threaded with copper
#large tapestry threaded with electrum
#large tapestry threaded with fine steel
#large tapestry threaded with gold
#large tapestry threaded with platinum
#large tapestry threaded with silver
#leather belt
#leather belt set with azurite
#leather belt set with chrysoprase
#leather belt set with eye agate
#leather belt set with freshwater pearl
#leather belt set with jasper
#leather belt set with lapis lazuli
#leather belt set with obsidian
#leather belt set with peridot
#leather belt set with rhodochrosite
#leather belt set with rock crystal
#leather belt set with rose quartz
#leather belt set with sardonyx
#leather belt set with smoky quartz
#leather belt set with star rose quartz
#leather belt set with turquoise
#leather belt set with zircon
#leather belt with brass buckle
#leather belt with bronze buckle
#leather belt with copper buckle
#leather belt with electrum buckle
#leather belt with fine steel buckle
#leather belt with gold buckle
#leather belt with platinum buckle
#leather belt with silver buckle
#leather boots
#leather boots with brass buckles
#leather boots with bronze buckles
#leather boots with copper buckles
#leather boots with electrum buckles
#leather boots with fine steel buckles
#leather boots with gold buckles
#leather boots with silver buckles
#leather bound book (blank)
#leather bracers
#leather hunter\'s cap
#leather mask
#leather pouch
#leather ribbon
#leather sash
#leather shoes
#leather shortsword scabbard
#leather talisman
#leather vest
#leopard fur bound book (blank)
#leopard fur bracers
#leopard fur bracers inlaid with gold
#leopard fur choker
#leopard fur cloak
#leopard fur coat
#leopard fur coinpurse
#leopard fur coinpurse set with peridot
#leopard fur corset
#leopard fur corset inlaid with gold
#leopard fur corset set with aquamarine
#leopard fur gloves
#leopard fur hunter\'s cap
#leopard fur hunter\'s cap inlaid with brass
#leopard fur hunter\'s cap set with moonstone
#leopard fur longsword scabbard
#leopard fur longsword scabbard inlaid with electrum
#leopard fur ribbon set with blue quartz
#leopard fur ribbon set with freshwater pearl
#leopard fur shoes
#leopard fur shoes inlaid with brass
#leopard fur shoes inlaid with bronze
#leopard fur shoes set with sardonyx
#leopard fur shoes set with smoky quartz
#leopard fur shortsword scabbard
#leopard fur shortsword scabbard inlaid with silver
#leopard fur shortsword scabbard set with coral
#leopard fur tabard
#leopard fur tabard wreathed in continual flame
#leopard fur talisman set with azurite
#leopard fur talisman set with moss agate
#leopard fur talisman set with obsidian
#leopard fur talisman set with rhodochrosite
#leopard fur talisman set with turquoise
#malachite medallion
#malachite miniature (of a charger) set with hematite
#malachite ring set with hematite
#malachite statue (of a draconic goddess) inlaid with platinum
#marble bowl
#marble bowl inlaid with brass
#marble coffer
#marble comb
#marble comb set with jasper
#marble dice (pair) set with blue quartz
#marble figurine (of a water goddess)
#marble medallion
#marble necklace
#marble orb
#marble orb set with amber
#marble puzzle box
#marble ring set with rhodochrosite
#marble ring set with turquoise
#marble statue (of a mermaid) inlaid with silver
#marble statuette (of a god of ice) inlaid with platinum
#marble statuette (of a lion)
#marble statuette (of a monstrous god)
#marble stele
#marble stele inlaid with gold
#marble totem (of a totem charge)
#moonstone rod inlaid with electrum
#moonstone urn
#moonstone vase wreathed in silver continual flame
#moss agate figurine (of a male elf)
#moss agate holy symbol (of an earth god)
#obsidian dice (pair) set with obsidian
#obsidian miniature (of a male elf archer) set with eye agate
#onyx mask set with pink pearl
#onyx miniature (of a god of storms)
#onyx miniature (of a water goddess)
#onyx ring inlaid with silver
#ornate silver mirror
#ornate silver mirror set with alexandrite
#ornate silver mirror set with aquamarine
#ornate silver mirror set with azurite
#ornate silver mirror set with blue quartz
#ornate silver mirror set with deep blue spinel
#ornate silver mirror set with eye agate
#ornate silver mirror set with freshwater pearl
#ornate silver mirror set with golden yellow topaz
#ornate silver mirror set with lapis lazuli
#ornate silver mirror set with moss agate
#ornate silver mirror set with obsidian
#ornate silver mirror set with rhodochrosite
#ornate silver mirror set with turquoise
#ornate silver mirror set with violet garnet
#painted glass bowl
#painted glass box
#painted glass dice (pair)
#painted glass ewer
#painted glass figurine (of a goddess of storms)
#painted glass figurine (of a god of death)
#painted glass goblet
#painted glass holy symbol (of a god of good)
#painted glass mask
#painted glass medallion
#painted glass miniature (of a castle)
#painted glass miniature (of a dolphin)
#painted glass miniature (of a male dwarf archer)
#painted glass miniature (of a monstrous god)
#painted glass miniature (of an elf wench)
#painted glass miniature (of a raven)
#painted glass miniature (of a tower)
#painted glass necklace
#painted glass puzzle box
#painted glass ring
#painted glass rod
#painted glass scroll case
#painted glass urn
#peridot amphora
#peridot miniature (of a castle) inlaid with fine steel
#peridot orb inlaid with hepatizon
#peridot stele
#pewter armband
#pewter bell
#pewter belt
#pewter box
#pewter bracers
#pewter brazier
#pewter brooch
#pewter buckle
#pewter candlesticks
#pewter censer
#pewter chain
#pewter chalice
#pewter chime
#pewter choker
#pewter comb
#pewter decanter
#pewter diadem
#pewter dice (pair)
#pewter earrings
#pewter ewer
#pewter figurine (of a god of fate)
#pewter figurine (of a shark)
#pewter flask
#pewter flute
#pewter hairpin
#pewter holy symbol (of a goddess of honor)
#pewter holy symbol (of a god of trickery)
#pewter longsword
#pewter mace
#pewter medallion
#pewter miniature (of a god of good)
#pewter miniature (of a tree)
#pewter orb
#pewter pin
#pewter rod
#pewter scroll case
#pewter shortsword scabbard
#pewter shuriken
#pewter sickle
#pewter signet ring
#pewter skull
#pewter staff
#pewter statuette (of a female halfling warrior)
#pewter statuette (of an elf sorceror)
#pewter tiara
#pewter torc
#pewter urn
#pewter warhammer
#pink pearl bowl inlaid with platinum
#platinum amulet set with tourmaline
#platinum armband
#platinum belt
#platinum bound book (blank)
#platinum bound book (blank) inlaid with platinum
#platinum box
#platinum breastplate
#platinum brooch
#platinum brooch inlaid with copper
#platinum brooch set with jasper
#platinum buckle
#platinum candlesticks inlaid with gold
#platinum chalice inlaid with electrum
#platinum chest
#platinum chest wreathed in green continual flame
#platinum chime
#platinum cloth choker
#platinum cloth cloak
#platinum cloth cloak set with black pearl
#platinum cloth coat
#platinum cloth coat set with deep green spinel
#platinum cloth coat set with red garnet
#platinum cloth gloves
#platinum cloth gown
#platinum cloth gown set with red spinel
#platinum cloth hunter\'s cap
#platinum cloth ribbon
#platinum cloth robe
#platinum cloth robe set with amethyst
#platinum cloth robe set with red-brown spinel
#platinum cloth sash
#platinum cloth talisman
#platinum cloth vest
#platinum crown
#platinum decanter inlaid with platinum
#platinum diadem inlaid with bronze
#platinum dice (pair) inlaid with fine steel
#platinum earrings
#platinum ewer wreathed in continual flame
#platinum figurine (of a female halfling) set with jet
#platinum font
#platinum framed masterpiece painting
#platinum framed painting
#platinum gauntlets
#platinum mask inlaid with gold
#platinum medallion inlaid with gold
#platinum medallion set with silver pearl
#platinum pendant inlaid with bronze
#platinum pin
#platinum plate armor inlaid with orichalcum
#platinum plate armor wreathed in green continual flame
#platinum ring inlaid with copper
#platinum scepter
#platinum shuriken
#platinum shuriken inlaid with brass
#platinum sickle
#platinum skull inlaid with hepatizon
#platinum statuette (of a male human archer) inlaid with hepatizon
#platinum stele inlaid with orichalcum
#platinum stele wreathed in golden continual flame
#platinum stele wreathed in white continual flame
#platinum torc
#platinum warhammer wreathed in continual flame
#polished stone box
#polished stone comb
#polished stone dice (pair)
#polished stone figurine (of an earth god)
#polished stone goblet
#polished stone holy symbol (of a goddess of trickery)
#polished stone idol (of a goddess of love)
#polished stone idol (of a god of knowledge)
#polished stone jar
#polished stone mask
#polished stone miniature (of a castle)
#polished stone miniature (of a male elf)
#polished stone miniature (of an air god)
#polished stone miniature (of a temple)
#polished stone necklace
#polished stone puzzle box
#polished stone ring
#polished stone rod
#polished stone statuette (of a drake)
#polished stone sundial
#polished stone vase
#porcelain amphora carved with knotwork
#porcelain amphora inlaid with electrum
#porcelain box
#porcelain box inlaid with brass
#porcelain dice (pair) set with obsidian
#porcelain figurine (of a badger) inlaid with copper
#porcelain figurine (of a gnome priest)
#porcelain figurine (of a male gnome)
#porcelain figurine (of a raven)
#porcelain goblet
#porcelain goblet inlaid with bronze
#porcelain holy symbol (of a goddess of evil)
#porcelain holy symbol (of a god of good)
#porcelain jar set with red spinel
#porcelain mask inlaid with bronze
#porcelain miniature (of a female dwarf) set with lapis lazuli
#porcelain miniature (of a god of destruction) set with obsidian
#porcelain miniature (of a tower) set with banded agate
#porcelain necklace
#porcelain orb
#porcelain pedestal inlaid with silver
#porcelain pedestal set with alexandrite
#porcelain ring set with banded agate
#porcelain ring set with blue quartz
#porcelain ring set with malachite
#porcelain ring set with moss agate
#porcelain rod
#porcelain rod set with zircon
#porcelain scroll case carved with knotwork
#porcelain statue (of a god of law)
#porcelain stele
#porcelain sundial
#porcelain vase carved with knotwork
#porcelain vase inlaid with silver
#porcelain vase set with tourmaline
#rabbit fur belt
#rabbit fur boots
#rabbit fur bound book (blank)
#rabbit fur bracers
#rabbit fur choker
#rabbit fur coinpurse
#rabbit fur gloves
#rabbit fur hunter\'s cap
#rabbit fur mask
#rabbit fur pouch
#rabbit fur ribbon
#rabbit fur sash
#rabbit fur shoes
#rabbit fur shortsword scabbard
#rabbit fur talisman
#rabbit fur vest
#rare book (the astral book of amin)
#red-brown spinel dice (pair) inlaid with bronze
#red-brown spinel figurine (of a halfling queen)
#red-brown spinel miniature (of an aberrant god) set with sardonyx
#red-brown spinel orb inlaid with mithral
#red-brown spinel ring
#red-brown spinel vase wreathed in golden continual flame
#red garnet bowl
#red garnet ewer
#red garnet miniature (of a castle)
#red garnet miniature (of a god of ice)
#red garnet pedestal wreathed in green continual flame
#red garnet rod inlaid with silver
#red garnet statue (of a raven) wreathed in white continual flame
#red spinel mask set with coral
#red spinel ring
#red spinel sundial
#rhodochrosite bowl inlaid with bronze
#rhodochrosite bowl inlaid with fine steel
#rhodochrosite rod inlaid with bronze
#rock crystal bowl inlaid with gold
#rock crystal mask inlaid with gold
#rock crystal necklace
#rock crystal orb set with golden yellow topaz
#rock crystal puzzle box
#rock crystal ring
#rock crystal stele wreathed in violet continual flame
#rose quartz idol (of an earth god) inlaid with silver
#rose quartz ring set with iolite
#rose quartz stele
#rose quartz vase wreathed in continual flame
#rosewood amphora
#rosewood coffer
#rosewood coffer inlaid with electrum
#rosewood coffer set with silver pearl
#rosewood dice (pair) set with obsidian
#rosewood dice (pair) set with turquoise
#rosewood ewer
#rosewood figurine (of a goddess of chaos)
#rosewood figurine (of a god of storms)
#rosewood holy symbol (of a god of beauty)
#rosewood holy symbol (of a god of darkness)
#rosewood idol (of a fire god) inlaid with gold
#rosewood idol (of a god of animals)
#rosewood medallion
#rosewood medallion inlaid with copper
#rosewood miniature (of a halfling sorceress) set with malachite
#rosewood miniature (of a sea-lion) set with azurite
#rosewood necklace
#rosewood orb
#rosewood pedestal wreathed in continual flame
#rosewood puzzle box
#rosewood puzzle box set with pink pearl
#rosewood ring set with blue quartz
#rosewood scroll case
#rosewood statue (of a goddess of death) set with deep blue spinel
#rosewood statuette (of a god of animals) set with chrysoberyl
#rosewood statuette (of a griffon)
#rosewood stele
#rosewood sundial set with amethyst
#rosewood totem (of a totem charge)
#rosewood vase set with brown-green garnet
#sable belt
#sable belt wreathed in continual flame
#sable belt wreathed in violet continual flame
#sable boots
#sable boots set with red garnet
#sable bound book (blank)
#sable bound book (blank) inlaid with silver
#sable bound book (blank) wreathed in green continual flame
#sable bracers
#sable bracers inlaid with platinum
#sable bracers wreathed in blue continual flame
#sable choker
#sable cloak
#sable cloak wreathed in green continual flame
#sable coat
#sable coat wreathed in golden continual flame
#sable coat wreathed in violet continual flame
#sable coinpurse set with golden pearl
#sable corset
#sable hunter\'s cap set with jade
#sable longsword scabbard
#sable mask
#sable mask set with red spinel
#sable ribbon
#sable ribbon inlaid with bronze
#sable ribbon inlaid with silver
#sable ribbon set with rock crystal
#sable sash
#sable sash inlaid with adamantine
#sable shortsword scabbard
#sable shortsword scabbard inlaid with orichalcum
#sable shortsword scabbard wreathed in continual flame
#sable shortsword scabbard wreathed in white continual flame
#sable tabard
#sable tabard wreathed in silver continual flame
#sable talisman
#sable talisman inlaid with brass
#sable talisman set with moonstone
#sable vest inlaid with platinum
#sardonyx ring
#sardonyx scroll case
#set of crystal polyhedral dice
#silk choker threaded with gold
#silk choker threaded with silver
#silk choker trimmed with ermine
#silk choker trimmed with sable
#silk cloak
#silk cloak threaded with fine steel
#silk cloak threaded with gold
#silk cloak threaded with platinum
#silk cloak threaded with silver
#silk cloak trimmed with ermine
#silk cloak trimmed with sable
#silk coat
#silk coat threaded with brass
#silk coat threaded with bronze
#silk coat threaded with gold
#silk coat trimmed with ermine
#silk coat trimmed with fox fur
#silk coat trimmed with leopard fur
#silk coat trimmed with sable
#silk gloves threaded with electrum
#silk gloves threaded with silver
#silk gloves trimmed with ermine
#silk gloves trimmed with sable
#silk gown
#silk gown threaded with silver
#silk gown trimmed with ermine
#silk gown trimmed with sable
#silk hunter\'s cap threaded with platinum
#silk hunter\'s cap threaded with silver
#silk hunter\'s cap trimmed with ermine
#silk pennant threaded with copper
#silk pennant threaded with platinum
#silk pennant trimmed with ermine
#silk pennant trimmed with fox fur
#silk pennant trimmed with leopard fur
#silk robe
#silk robe threaded with platinum
#silk robe threaded with silver
#silk robe trimmed with ermine
#silk robe trimmed with fox fur
#silk robe trimmed with leopard fur
#silk robe trimmed with sable
#silk sash threaded with brass
#silk sash threaded with bronze
#silk sash threaded with silver
#silk sash trimmed with ermine
#silk sash trimmed with fox fur
#silk sash trimmed with leopard fur
#silk tabard
#silk tabard threaded with copper
#silk tabard threaded with electrum
#silk tabard threaded with gold
#silk tabard threaded with silver
#silk tabard trimmed with leopard fur
#silk tabard trimmed with sable
#silk vest threaded with silver
#silk vest trimmed with ermine
#silver amphora inlaid with adamantine
#silver amulet set with smoky quartz
#silver armlet
#silver armlet set with sardonyx
#silver bell
#silver belt set with red spinel
#silver bound book (blank) set with jet
#silver box set with jet
#silver bracelet
#silver bracelet inlaid with platinum
#silver bracelet set with deep green spinel
#silver bracers
#silver bracers inlaid with adamantine
#silver bracers wreathed in white continual flame
#silver brazier wreathed in continual flame
#silver brooch inlaid with bronze
#silver brooch set with moss agate
#silver buckle
#silver buckle inlaid with fine steel
#silver buckle set with moss agate
#silver candlesticks
#silver candlesticks set with citrine
#silver chain set with banded agate
#silver chain set with rock crystal
#silver chain set with turquoise
#silver chalice inlaid with platinum
#silver chest
#silver chime
#silver choker
#silver cloth choker
#silver cloth cloak
#silver cloth cloak set with alexandrite
#silver cloth cloak set with chrysoberyl
#silver cloth cloak set with deep green spinel
#silver cloth cloak set with red spinel
#silver cloth coat
#silver cloth coat set with golden pearl
#silver cloth coat set with red-brown spinel
#silver cloth coat set with silver pearl
#silver cloth coat set with white pearl
#silver cloth gloves
#silver cloth gown
#silver cloth gown set with deep green spinel
#silver cloth gown set with golden yellow topaz
#silver cloth hunter\'s cap
#silver cloth pennant
#silver cloth ribbon
#silver cloth robe
#silver cloth robe set with brown-green garnet
#silver cloth robe set with chrysoberyl
#silver cloth robe set with golden pearl
#silver cloth sash
#silver cloth tabard
#silver cloth tabard set with black pearl
#silver cloth tabard set with red-brown spinel
#silver cloth tabard set with tourmaline
#silver cloth talisman
#silver cloth vest
#silver coffer
#silver coffer inlaid with gold
#silver comb
#silver comb inlaid with silver
#silver crown
#silver dagger
#silver decanter
#silver diadem
#silver diadem inlaid with brass
#silver diadem set with citrine
#silver dice (pair) inlaid with copper
#silver dice (pair) set with azurite
#silver dice (pair) set with moss agate
#silver dice (pair) set with obsidian
#silver earrings
#silver earrings inlaid with brass
#silver figurine (of a god of illusions)
#silver figurine (of a human queen)
#silver flask
#silver flask inlaid with copper
#silver flute set with amethyst
#silver font
#silver framed masterpiece painting
#silver framed painting
#silver gauntlets
#silver greatsword
#silver hairpin
#silver hairpin set with rhodochrosite
#silver helmet wreathed in silver continual flame
#silver holy symbol (of a water goddess)
#silver idol (of a goddess of law) set with pink pearl
#silver longsword
#silver longsword scabbard wreathed in continual flame
#silver mace
#silver medallion
#silver miniature (of a god of light) inlaid with copper
#silver miniature (of an owl) set with chrysoprase
#silver miniature (of a phoenix) inlaid with silver
#silver miniature (of a temple) set with rose quartz
#silver music box
#silver necklace
#silver pearl dice (pair)
#silver pearl jar wreathed in white continual flame
#silver pearl miniature (of a god of good)
#silver pearl ring
#silver pectoral
#silver pectoral wreathed in continual flame
#silver pendant set with rock crystal
#silver pin inlaid with copper
#silver plate armor
#silver ring set with lapis lazuli
#silver ring set with turquoise
#silver rod
#silver scepter
#silver signet ring
#silver signet ring set with amber
#silver skull wreathed in continual flame
#silver staff wreathed in continual flame
#silver statue (of a female elf)
#silver statue (of a female human)
#silver statue (of a god of magic)
#silver stele
#silver tiara inlaid with gold
#silver totem (of a totem charge)
#silver urn set with black pearl
#silver vase
#silver warhammer inlaid with gold
#small bag of exotic spices
#small bag of incense
#small bag of spices
#small carpet
#small carpet threaded with brass
#small carpet threaded with bronze
#small carpet threaded with copper
#small carpet threaded with electrum
#small carpet threaded with fine steel
#small carpet threaded with platinum
#small carpet threaded with silver
#small silver mirror
#small tapestry
#small tapestry threaded with brass
#small tapestry threaded with bronze
#small tapestry threaded with copper
#small tapestry threaded with electrum
#small tapestry threaded with fine steel
#small tapestry threaded with platinum
#small tapestry threaded with silver
#small vial of exotic perfume
#small vial of perfume
#smoky quartz comb
#smoky quartz dice (pair)
#smoky quartz ring
#star rose quartz dice (pair)
#star rose quartz ewer set with aquamarine
#star rose quartz ring set with jasper
#star rose quartz rod
#tooled leather belt
#tooled leather boots
#tooled leather bound book (blank)
#tooled leather bound book (blank) inlaid with electrum
#tooled leather bound book (blank) inlaid with platinum
#tooled leather bracers
#tooled leather choker
#tooled leather cloak
#tooled leather cloak set with black pearl
#tooled leather cloak wreathed in continual flame
#tooled leather coat
#tooled leather coat inlaid with gold
#tooled leather coat wreathed in continual flame
#tooled leather coinpurse
#tooled leather coinpurse set with carnelian
#tooled leather coinpurse set with sardonyx
#tooled leather corset
#tooled leather corset set with golden yellow topaz
#tooled leather corset wreathed in continual flame
#tooled leather gloves set with carnelian
#tooled leather longsword scabbard
#tooled leather longsword scabbard inlaid with silver
#tooled leather longsword scabbard set with alexandrite
#tooled leather mask
#tooled leather mask inlaid with fine steel
#tooled leather pouch
#tooled leather pouch inlaid with bronze
#tooled leather ribbon set with banded agate
#tooled leather ribbon set with blue quartz
#tooled leather ribbon set with eye agate
#tooled leather ribbon set with freshwater pearl
#tooled leather ribbon set with hematite
#tooled leather ribbon set with lapis lazuli
#tooled leather ribbon set with turquoise
#tooled leather sash inlaid with electrum
#tooled leather shoes inlaid with brass
#tooled leather shoes inlaid with fine steel
#tooled leather tabard inlaid with platinum
#tooled leather talisman set with eye agate
#tooled leather talisman set with hematite
#tooled leather talisman set with lapis lazuli
#tooled leather talisman set with rhodochrosite
#tooled leather vest set with chrysoberyl
#tooled leather vest set with red spinel
#tooled leather vest set with silver pearl
#tourmaline ewer
#tourmaline miniature (of a dwarf sorceror) set with rose quartz
#turquoise rod
#unframed painting
#white pearl puzzle box
#white pearl puzzle box wreathed in continual flame
#wood framed painting
#zircon sundial inlaid with silver