import unreal,math,random
random.seed(7)
eas=unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
cube=unreal.EditorAssetLibrary.load_asset("/Engine/BasicShapes/Cube.Cube")
cnt={"T01":0,"T02":0,"T03":0}
def P(t,m,dx,dy,dz,x,y,h,yaw=0):
 c=cnt[t]+1;cnt[t]=c
 a=eas.spawn_actor_from_object(cube,unreal.Vector(x,y,float(h)),unreal.Rotator(0,0,float(yaw)))
 a.set_actor_scale3d(unreal.Vector(dx/100.0,dy/100.0,dz/100.0))
 a.set_actor_label("%s_Piece_%d"%(t,c))
 try:a.set_folder_path("Greybox/%s"%t)
 except:
  try:eas.set_actor_folder_path(a,"Greybox/%s"%t)
  except:pass
 try:a.tags=[m]
 except:pass
 return a
d=0
for a in eas.get_all_level_actors():
 try:fp=str(a.get_folder_path())
 except:
  try:fp=str(eas.get_actor_folder_path(a))
  except:fp=""
 try:lb=a.get_actor_label()
 except:lb=""
 if fp.startswith("Greybox") or lb.startswith("T01_") or lb.startswith("T02_") or lb.startswith("T03_"):
  try:eas.destroy_actor(a);d+=1
  except:pass
print("Cleanup deleted %d Greybox actors"%d)
try:
 R=1800
 for i in range(16):
  if i==0:continue
  th=math.radians(i*22.5);x=R*math.cos(th);y=R*math.sin(th)
  P("T01","StoneWall",400,40,250,x,y,125,math.degrees(th)+180)
 P("T01","Pillar",60,60,280,1800,200,140,0);P("T01","Pillar",60,60,280,1800,-200,140,0)
 P("T01","Frame",120,40,210,1800,100,105,90);P("T01","Frame",120,40,210,1800,-100,105,90)
 P("T01","MudWall",800,40,250,-600,300,125,0);P("T01","MudWall",340,40,250,-830,-300,125,0)
 P("T01","MudWall",340,40,250,-370,-300,125,0);P("T01","MudWall",40,600,250,-1000,0,125,0)
 P("T01","MudWall",40,600,250,-200,0,125,0)
 P("T01","MudWall",800,40,250,600,300,125,0);P("T01","MudWall",340,40,250,370,-300,125,0)
 P("T01","MudWall",340,40,250,830,-300,125,0);P("T01","MudWall",40,600,250,200,0,125,0)
 P("T01","MudWall",40,600,250,1000,0,125,0)
 P("T01","Roof",800,600,30,-600,0,265,0);P("T01","Roof",800,600,30,600,0,265,0)
 P("T01","Frame",120,40,210,-600,-300,105,0);P("T01","Frame",120,40,210,600,-300,105,0)
 for px,py in [(-600,300),(600,300),(-600,1500),(600,1500)]:P("T01","Wood",40,40,220,px,py,110,0)
 P("T01","Wood",1200,40,40,0,300,220,0);P("T01","Wood",1200,40,40,0,1500,220,0)
 for sx,sy in [(-600,-600),(600,-600)]:
  for k in range(3):P("T01","Crate",80,80,80,sx,sy,40+80*k,0)
 for dg in (45,135,225,315):
  th=math.radians(dg);P("T01","Olive",100,100,200,800*math.cos(th),800*math.sin(th),100,0)
 for dg in (20,80,140,200,260,320):
  th=math.radians(dg);P("T01","Rubble",120,120,60,2700*math.cos(th),2700*math.sin(th),30,0)
except Exception as e:print("T01 failed: %s"%e)
try:
 for k in range(-4000,4001,800):
  P("T02","StoneWall",700,40,250,30000+k,-1200,125,0)
  P("T02","StoneWall",700,40,250,30000+k,1200,125,0)
 P("T02","Pillar",80,80,300,22000,-1200,150,0);P("T02","Pillar",80,80,300,22000,1200,150,0)
 P("T02","Pillar",80,80,300,38000,-1200,150,0);P("T02","Pillar",80,80,300,38000,1200,150,0)
 for cx,cy in [(28000,-900),(29500,900),(30500,-900),(32000,900)]:P("T02","Crate",80,80,80,cx,cy,40,0)
 for rx in (30000,30400,30800):
  for ry in (1800,2200):P("T02","Rubble",120,120,60,rx,ry,30,0)
except Exception as e:print("T02 failed: %s"%e)
try:
 n=0
 for yy in (-1000,0,1000):
  for xx in range(71000,79001,800):
   if n>=22:break
   P("T03","TerraceWall",700,40,150,xx,yy,75,0);n+=1
  if n>=22:break
 P("T03","MudWall",600,40,250,75000,300,125,0);P("T03","MudWall",600,40,250,75000,-300,125,0)
 P("T03","MudWall",40,600,250,74700,0,125,0);P("T03","MudWall",40,600,250,75300,0,125,0)
 P("T03","Roof",600,600,30,75000,0,265,0)
 P("T03","Frame",120,40,210,75000,-300,105,0);P("T03","Frame",120,40,210,75300,0,105,90)
 for ox in (74400,75000,75600):
  P("T03","Olive",100,100,200,ox,2000,100,0);P("T03","Olive",100,100,200,ox,2400,100,0)
 for rx in (74600,75000,75400):
  P("T03","Rubble",120,120,60,rx,-2000,30,0);P("T03","Rubble",120,120,60,rx,-2400,30,0)
 P("T03","Stairs",300,800,80,75000,-500,40,0);P("T03","Stairs",300,800,80,75000,500,40,0)
except Exception as e:print("T03 failed: %s"%e)
print("T01 total %d"%cnt["T01"])
print("T02 total %d"%cnt["T02"])
print("T03 total %d"%cnt["T03"])
