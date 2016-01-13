worlds["world"] = "C:\Users\Richard\Desktop\Minecraft-Server\world" 

def townFilter(poi): 	### blue town icon
    if poi['id'] == 'Town':
        try:
            return (poi['name'] + '\n' + poi['description'])
        except KeyError:
            return poi['name'] + '\n'

def mineFilter(poi):	### blue mine icon
    if poi['id'] == 'Mine':
        try:
            return (poi['name'] + '\n' + poi['description'])
        except KeyError:
            return poi['name'] + '\n'
			
def constrFilter(poi):	### red mine icon
    if poi['id'] == 'ConstructionSite':
        try:
            return (poi['name'] + '\n' + poi['description'])
        except KeyError:
            return poi['name'] + '\n'		
			
def castleFilter(poi):	### blue tower icon
    if poi['id'] == 'Castle':
        try:
            return (poi['name'] + '\n' + poi['description'])
        except KeyError:
            return poi['name'] + '\n'	
			
def dungeonFilter(poi):	### red tower icon
    if poi['id'] == 'Dungeon':
        try:
            return (poi['name'] + '\n' + poi['description'])
        except KeyError:
            return poi['name'] + '\n'	

def factoryFilter(poi):	### blue factory icon
    if poi['id'] == 'Factory':
        try:
            return (poi['name'] + '\n' + poi['description'])
        except KeyError:
            return poi['name'] + '\n'

def farmFilter(poi):	### blue farm icon
    if poi['id'] == 'Farm':
        try:
            return (poi['name'] + '\n' + poi['description'])
        except KeyError:
            return poi['name'] + '\n'	

def mobFarmFilter(poi):	### red farm icon
    if poi['id'] == 'mobFarm':
        try:
            return (poi['name'] + '\n' + poi['description'])
        except KeyError:
            return poi['name'] + '\n'			

renders['renderDay'] = {
    'world':'world',
    'title':'Overworld Day',
	'rendermode':'smooth_lighting',
	'forcerender':False,
    'manualpois':[
                   {'id':'Town',		### spawn town
                    'x':44,
                    'y':77,
                    'z':18,
                    'name':'Dorf',
                    'description':'Spawn, Base of Ueda Ichitaka'},
                   {'id':'Town',		### bauernhaus
                    'x':1645,
                    'y':72,
                    'z':135,
                    'name':'Bauernhaus'},
					{'id':'Town',		### strandhaus
                    'x':811,
                    'y':64,
                    'z':926,
                    'name':'Strandhaus'},
					{'id':'Castle',		### hybridfestung
                    'x':254,
                    'y':64,
                    'z':-1510,
                    'name':'Festung Ueda'},
					{'id':'Castle',		### festung chaos
                    'x':270,
                    'y':70,
                    'z':170,
                    'name':'Festung Chaos'},
					{'id':'Dungeon',		### end festung
                    'x':-604,
                    'y':62,
                    'z':-157,
                    'name':'End Festung'},
					{'id':'Dungeon',		### atlantis 1
                    'x':1143,
                    'y':63,
                    'z':1879,
                    'name':'Atlantis 1'},
					{'id':'Dungeon',		### atlantis 2
                    'x':1576,
                    'y':63,
                    'z':1223,
                    'name':'Atlantis 2'},
					{'id':'Dungeon',		### atlantis 3
                    'x':-2265,
                    'y':63,
                    'z':2080,
                    'name':'Atlantis 3'},
					{'id':'Dungeon',		### mine
                    'x':-111,
                    'y':70,
                    'z':-160,
                    'name':'Eingang Mine'},
					{'id':'Farm',		### farm site
                    'x':79,
                    'y':67,
                    'z':40,
                    'name':'Farm Site'},
					{'id':'mobFarm',		### monsterfalle
                    'x':-70,
                    'y':75,
                    'z':-167,
                    'name':'Monsterfalle'},
					{'id':'ConstructionSite',		### cavespider
                    'x':-141,
                    'y':38,
                    'z':-207,
                    'name':'Cavespider Spawner'},
					{'id':'ConstructionSite',		### spider dungeon
                    'x':-19,
                    'y':71,
                    'z':-189,
                    'name':'Spider Dungeon'},
					{'id':'ConstructionSite',		### hexenhaus
                    'x':-205,
                    'y':69,
                    'z':-1499,
                    'name':'Hexenhaus'},
					{'id':'ConstructionSite',		### big tower chaos
                    'x':128,
                    'y':94,
                    'z':118,
                    'name':'Big Tower Chaos'},
					{'id':'ConstructionSite',		### innenhof chaos
                    'x':190,
                    'y':75,
                    'z':163,
                    'name':'Innenhof Chaos'},
					],
    'markers': [dict(name="Towns", filterFunction=townFilter, icon="icons/marker_town.png"),
				dict(name="Mines", filterFunction=mineFilter, icon="icons/marker_mine.png"),
				dict(name="Construction Sites", filterFunction=constrFilter, icon="icons/marker_mine_red.png"),
				dict(name="Castles", filterFunction=castleFilter, icon="icons/marker_tower.png"),
				dict(name="Dungeons", filterFunction=dungeonFilter, icon="icons/marker_tower_red.png"),
				dict(name="Factories", filterFunction=factoryFilter, icon="icons/marker_factory.png"),
				dict(name="Farms", filterFunction=farmFilter, icon="icons/marker_hoe.png"),
				dict(name="Mob Farms", filterFunction=mobFarmFilter, icon="icons/marker_hoe_red.png")],
    ### Note: The 'icon' parameter allows you to specify a custom icon, as per
    ###       standard markers. This icon must exist in the same folder as your
    ###       custom webassets or in the same folder as the generated index.html
    ###       in this case, we use the marker_town.png icon which comes with
    ###       the Overviewer by default, located in a subdirectory of web_assets.
}	

renders['renderDay2'] = {
	'world':'world',
	'title':'Overworld Day 2',
	'rendermode':'smooth_lighting',
	'northdirection':'lower-right',
	'forcerender':False,
}	

renders['renderNight'] = {
	'world':'world',
	'title':'Overworld Night',
	'rendermode': 'smooth_night',
	'forcerender':False,
}	

renders['renderNight2'] = {
	'world':'world',
	'title':'Overworld Night 2',
	'rendermode': 'smooth_night',
	'northdirection':'lower-right',
	'forcerender':False,
}

renders['renderNether'] = {
	'world':'world',
	'title':'Nether',
	'rendermode': 'nether',
	'dimension':'nether',
	'forcerender':False,
}

renders['renderNether2'] = {
	'world':'world',
	'title':'Nether 2',
	'rendermode': 'nether',
	'dimension':'nether',
	'northdirection':'lower-right',
	'forcerender':False,
}

renders['renderEnd'] = {
	'world':'world',
	'title':'End',
	'rendermode': 'smooth_lighting',
	'dimension':'end',
	'forcerender':False,
}

renders['Railways'] = {
	'world':'world',
	'title':'Railways',
	'rendermode': [ClearBase(), MineralOverlay(minerals = [(27, (255, 0, 0)), (28, (255, 0, 0)), (66, (255, 0, 0))]), EdgeLines()],
	'forcerender':False,
}

outputdir = "C:\Users\Richard\Desktop\map render"
### outputdir = "C:\Users\Karsten\Desktop\map render"
### texturepath = "C:\Users\Karsten\Desktop\map render\Misa.zip"