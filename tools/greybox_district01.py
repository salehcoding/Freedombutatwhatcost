import unreal, math, random
rnd = random.Random(7)
eas = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
cube = unreal.load_asset("/Engine/BasicShapes/Cube.Cube")
C = {"T01": (0, 0), "T02": (30000, 0), "T03": (75000, 0)}
cnt = {"T01": 0, "T02": 0, "T03": 0}
T = ["T01", "T02", "T03"]
def S(piece, tile, lx, ly, z, sx, sy, sz, yaw=0):
    try:
        cx, cy = C[tile]
        a = eas.spawn_actor_from_object(cube, unreal.Vector(cx+lx, cy+ly, z), unreal.Rotator(0, yaw, 0))
        a.set_actor_label(f"{tile}_{piece}_{cnt[tile]}")
        a.set_actor_scale3d(unreal.Vector(sx, sy, sz))
        try: a.set_folder_path(f"Greybox/{tile}")
        except: pass
        try:
            a.tags.append(f"Tile={tile}")
            a.tags.append(f"Piece={piece}")
        except:
            try:
                a.add_actor_tag(f"Tile={tile}")
                a.add_actor_tag(f"Piece={piece}")
            except: pass
        cnt[tile] += 1
        return a
    except Exception as e:
        print(f"spawn fail {piece} {tile}: {e}")
        return None
try:
    for i in range(16):
        d = math.radians(i * 22.5)
        S("StoneWall", "T01", math.cos(d)*1800, math.sin(d)*1800, 125, 4, 0.4, 2.5, yaw=i*22.5+90)
except Exception as e: print(f"StoneWall T01: {e}")
try:
    for i in range(22):
        S("StoneWall", "T02", -8000+(i%11)*800, -1200 if i<11 else 1200, 125, 4, 0.4, 2.5, yaw=0)
except Exception as e: print(f"StoneWall T02: {e}")
try:
    for i in range(16):
        S("StoneWall", "T03", -6000+i*800, 0, 125, 4, 0.4, 2.5, yaw=90)
except Exception as e: print(f"StoneWall T03: {e}")
try:
    for i in range(14):
        S("MudWall", "T01", -1800+(i%7)*600, -600+(i//7)*1200, 125, 4, 0.4, 2.5, yaw=0)
    for i in range(12):
        S("MudWall", "T02", rnd.uniform(-8000,8000), rnd.uniform(-3000,3000), 125, 4, 0.4, 2.5, yaw=rnd.choice([0,90]))
    for i in range(12):
        S("MudWall", "T03", rnd.uniform(-7000,7000), rnd.uniform(-3000,3000), 125, 4, 0.4, 2.5, yaw=rnd.choice([0,90]))
except Exception as e: print(f"MudWall: {e}")
try:
    for i in range(30):
        S("Pillar", T[i%3], rnd.uniform(-7000,7000), rnd.uniform(-5000,5000), 140, 0.6, 0.6, 2.8)
except Exception as e: print(f"Pillar: {e}")
try:
    for i in range(24):
        S("RoofSlab", T[i%3], rnd.uniform(-7000,7000), rnd.uniform(-5000,5000), 275, 4, 4, 0.3)
except Exception as e: print(f"RoofSlab: {e}")
try:
    for i in range(30):
        S("Frame", T[i%3], rnd.uniform(-7000,7000), rnd.uniform(-5000,5000), 105, 1.2, 0.4, 2.1, yaw=rnd.choice([0,90]))
except Exception as e: print(f"Frame: {e}")
try:
    for i in range(24):
        t, bx, by, yw = T[i%3], rnd.uniform(-7000,7000), rnd.uniform(-5000,5000), rnd.choice([0,90])
        S("PergolaPost", t, bx-190, by, 110, 0.2, 0.2, 2.2, yaw=yw)
        S("PergolaPost", t, bx+190, by, 110, 0.2, 0.2, 2.2, yaw=yw)
        S("PergolaBeam", t, bx, by, 230, 4, 0.2, 0.2, yaw=yw)
except Exception as e: print(f"Pergola: {e}")
try:
    for i in range(32):
        h = rnd.uniform(100,120)
        S("Terrace", T[i%3], rnd.uniform(-7000,7000), rnd.uniform(-5000,5000), h/2, 4, 0.6, h/100, yaw=rnd.choice([0,90]))
except Exception as e: print(f"Terrace: {e}")
try:
    for i in range(46):
        t, ox, oy = T[i%3], rnd.uniform(-8000,8000), rnd.uniform(-6000,6000)
        S("OliveTrunk", t, ox, oy, 100, 0.3, 0.3, 2.0)
        S("OliveCanopy", t, ox, oy, 325, 2.5, 2.5, 1.5, yaw=rnd.uniform(0,90))
except Exception as e: print(f"Olive: {e}")
try:
    for i in range(30):
        S("Crate", T[i%3], rnd.uniform(-7000,7000), rnd.uniform(-5000,5000), 50+100*(i%2), 1, 1, 1, yaw=rnd.choice([0,15,30,45]))
except Exception as e: print(f"Crate: {e}")
try:
    for i in range(38):
        sx, sy, sz = rnd.uniform(1,3), rnd.uniform(1,3), rnd.uniform(0.3,0.6)
        S("Rubble", T[i%3], rnd.uniform(-8000,8000), rnd.uniform(-5000,5000), sz*50, sx, sy, sz, yaw=rnd.uniform(0,180))
except Exception as e: print(f"Rubble: {e}")
try:
    for i in range(18):
        t, qx, qy, yw = T[i%3], rnd.uniform(-7000,7000), rnd.uniform(-5000,5000), rnd.choice([0,90,180,270])
        S("StairLow", t, qx, qy, 30, 3, 1, 0.6, yaw=yw)
        S("StairHigh", t, qx, qy, 90, 3, 1, 0.6, yaw=yw)
except Exception as e: print(f"Stair: {e}")
print(f"T01={cnt['T01']} T02={cnt['T02']} T03={cnt['T03']} TOTAL={sum(cnt.values())}")
