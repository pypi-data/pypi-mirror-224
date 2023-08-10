from cttilemap import TileMap, Layer, Tile

t = TileMap(5, [], [], {}, [16, 16])

layer = Layer()

layer.resize(258, 258)

for x in range(258):
	for y in range(258):
		if x == 0 or x == 257 or y == 0 or y == 257:
			layer[x, y] = Tile.by_id(0x0000)
		else:
			layer[x, y] = Tile.by_xy(x, y)

layer.settings.collision = 0xFF
layer.settings.tile_dimensions = [12, 12]

t.layers.append(layer)

with open("tests/made.l", "wb+") as f:
	t.dump(f)
