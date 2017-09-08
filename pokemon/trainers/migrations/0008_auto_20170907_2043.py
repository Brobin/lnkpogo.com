# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-07 20:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainers', '0007_auto_20170907_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoritepokemon',
            name='number',
            field=models.IntegerField(choices=[(1, '1 - Bulbasaur'), (2, '2 - Ivysaur'), (3, '3 - Venusaur'), (4, '4 - Charmander'), (5, '5 - Charmeleon'), (6, '6 - Charizard'), (7, '7 - Squirtle'), (8, '8 - Wartortle'), (9, '9 - Blastoise'), (10, '10 - Caterpie'), (11, '11 - Metapod'), (12, '12 - Butterfree'), (13, '13 - Weedle'), (14, '14 - Kakuna'), (15, '15 - Beedrill'), (16, '16 - Pidgey'), (17, '17 - Pidgeotto'), (18, '18 - Pidgeot'), (19, '19 - Rattata'), (20, '20 - Raticate'), (21, '21 - Spearow'), (22, '22 - Fearow'), (23, '23 - Ekans'), (24, '24 - Arbok'), (25, '25 - Pikachu'), (26, '26 - Raichu'), (27, '27 - Sandshrew'), (28, '28 - Sandslash'), (29, '29 - Nidoran Female'), (30, '30 - Nidorina'), (31, '31 - Nidoqueen'), (32, '32 - Nidoran♂'), (33, '33 - Nidorino'), (34, '34 - Nidoking'), (35, '35 - Clefairy'), (36, '36 - Clefable'), (37, '37 - Vulpix'), (38, '38 - Ninetales'), (39, '39 - Jigglypuff'), (40, '40 - Wigglytuff'), (41, '41 - Zubat'), (42, '42 - Golbat'), (43, '43 - Oddish'), (44, '44 - Gloom'), (45, '45 - Vileplume'), (46, '46 - Paras'), (47, '47 - Parasect'), (48, '48 - Venonat'), (49, '49 - Venomoth'), (50, '50 - Diglett'), (51, '51 - Dugtrio'), (52, '52 - Meowth'), (53, '53 - Persian'), (54, '54 - Psyduck'), (55, '55 - Golduck'), (56, '56 - Mankey'), (57, '57 - Primeape'), (58, '58 - Growlithe'), (59, '59 - Arcanine'), (60, '60 - Poliwag'), (61, '61 - Poliwhirl'), (62, '62 - Poliwrath'), (63, '63 - Abra'), (64, '64 - Kadabra'), (65, '65 - Alakazam'), (66, '66 - Machop'), (67, '67 - Machoke'), (68, '68 - Machamp'), (69, '69 - Bellsprout'), (70, '70 - Weepinbell'), (71, '71 - Victreebel'), (72, '72 - Tentacool'), (73, '73 - Tentacruel'), (74, '74 - Geodude'), (75, '75 - Graveler'), (76, '76 - Golem'), (77, '77 - Ponyta'), (78, '78 - Rapidash'), (79, '79 - Slowpoke'), (80, '80 - Slowbro'), (81, '81 - Magnemite'), (82, '82 - Magneton'), (83, '83 - Farfetch’d'), (84, '84 - Doduo'), (85, '85 - Dodrio'), (86, '86 - Seel'), (87, '87 - Dewgong'), (88, '88 - Grimer'), (89, '89 - Muk'), (90, '90 - Shellder'), (91, '91 - Cloyster'), (92, '92 - Gastly'), (93, '93 - Haunter'), (94, '94 - Gengar'), (95, '95 - Onix'), (96, '96 - Drowzee'), (97, '97 - Hypno'), (98, '98 - Krabby'), (99, '99 - Kingler'), (100, '100 - Voltorb'), (101, '101 - Electrode'), (102, '102 - Exeggcute'), (103, '103 - Exeggutor'), (104, '104 - Cubone'), (105, '105 - Marowak'), (106, '106 - Hitmonlee'), (107, '107 - Hitmonchan'), (108, '108 - Lickitung'), (109, '109 - Koffing'), (110, '110 - Weezing'), (111, '111 - Rhyhorn'), (112, '112 - Rhydon'), (113, '113 - Chansey'), (114, '114 - Tangela'), (115, '115 - Kangaskhan'), (116, '116 - Horsea'), (117, '117 - Seadra'), (118, '118 - Goldeen'), (119, '119 - Seaking'), (120, '120 - Staryu'), (121, '121 - Starmie'), (122, '122 - Mr. Mime'), (123, '123 - Scyther'), (124, '124 - Jynx'), (125, '125 - Electabuzz'), (126, '126 - Magmar'), (127, '127 - Pinsir'), (128, '128 - Tauros'), (129, '129 - Magikarp'), (130, '130 - Gyarados'), (131, '131 - Lapras'), (132, '132 - Ditto'), (133, '133 - Eevee'), (134, '134 - Vaporeon'), (135, '135 - Jolteon'), (136, '136 - Flareon'), (137, '137 - Porygon'), (138, '138 - Omanyte'), (139, '139 - Omastar'), (140, '140 - Kabuto'), (141, '141 - Kabutops'), (142, '142 - Aerodactyl'), (143, '143 - Snorlax'), (144, '144 - Articuno'), (145, '145 - Zapdos'), (146, '146 - Moltres'), (147, '147 - Dratini'), (148, '148 - Dragonair'), (149, '149 - Dragonite'), (150, '150 - Mewtwo'), (151, '151 - Mew'), (152, '152 - Chikorita'), (153, '153 - Bayleef'), (154, '154 - Meganium'), (155, '155 - Cyndaquil'), (156, '156 - Quilava'), (157, '157 - Typhlosion'), (158, '158 - Totodile'), (159, '159 - Croconaw'), (160, '160 - Feraligatr'), (161, '161 - Sentret'), (162, '162 - Furret'), (163, '163 - Hoothoot'), (164, '164 - Noctowl'), (165, '165 - Ledyba'), (166, '166 - Ledian'), (167, '167 - Spinarak'), (168, '168 - Ariados'), (169, '169 - Crobat'), (170, '170 - Chinchou'), (171, '171 - Lanturn'), (172, '172 - Pichu'), (173, '173 - Cleffa'), (174, '174 - Igglybuff'), (175, '175 - Togepi'), (176, '176 - Togetic'), (177, '177 - Natu'), (178, '178 - Xatu'), (179, '179 - Mareep'), (180, '180 - Flaaffy'), (181, '181 - Ampharos'), (182, '182 - Bellossom'), (183, '183 - Marill'), (184, '184 - Azumarill'), (185, '185 - Sudowoodo'), (186, '186 - Politoed'), (187, '187 - Hoppip'), (188, '188 - Skiploom'), (189, '189 - Jumpluff'), (190, '190 - Aipom'), (191, '191 - Sunkern'), (192, '192 - Sunflora'), (193, '193 - Yanma'), (194, '194 - Wooper'), (195, '195 - Quagsire'), (196, '196 - Espeon'), (197, '197 - Umbreon'), (198, '198 - Murkrow'), (199, '199 - Slowking'), (200, '200 - Misdreavus'), (201, '201 - Unown'), (202, '202 - Wobbuffet'), (203, '203 - Girafarig'), (204, '204 - Pineco'), (205, '205 - Forretress'), (206, '206 - Dunsparce'), (207, '207 - Gligar'), (208, '208 - Steelix'), (209, '209 - Snubbull'), (210, '210 - Granbull'), (211, '211 - Qwilfish'), (212, '212 - Scizor'), (213, '213 - Shuckle'), (214, '214 - Heracross'), (215, '215 - Sneasel'), (216, '216 - Teddiursa'), (217, '217 - Ursaring'), (218, '218 - Slugma'), (219, '219 - Magcargo'), (220, '220 - Swinub'), (221, '221 - Piloswine'), (222, '222 - Corsola'), (223, '223 - Remoraid'), (224, '224 - Octillery'), (225, '225 - Delibird'), (226, '226 - Mantine'), (227, '227 - Skarmory'), (228, '228 - Houndour'), (229, '229 - Houndoom'), (230, '230 - Kingdra'), (231, '231 - Phanpy'), (232, '232 - Donphan'), (233, '233 - Porygon2'), (234, '234 - Stantler'), (235, '235 - Smeargle'), (236, '236 - Tyrogue'), (237, '237 - Hitmontop'), (238, '238 - Smoochum'), (239, '239 - Elekid'), (240, '240 - Magby'), (241, '241 - Miltank'), (242, '242 - Blissey'), (243, '243 - Raikou'), (244, '244 - Entei'), (245, '245 - Suicune'), (246, '246 - Larvitar'), (247, '247 - Pupitar'), (248, '248 - Tyranitar'), (249, '249 - Lugia'), (250, '250 - Ho-Oh')]),
        ),
    ]
