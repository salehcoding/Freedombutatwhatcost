import unreal
try:
    s = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    c = len([a for a in s.get_all_level_actors() if str(a.get_folder_path()) == "Play"])
    print(f"Play count: {c}")
except Exception as e:
    print(f"folder op failed: {e}")
try:
    p = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.PlayerStart, unreal.Vector(0, 0, 300), unreal.Rotator(0, 0, 0))
    p.set_folder_path(unreal.Name("Play"))
    p.set_actor_label("T01_PlayerStart")
    print(f"label: {p.get_actor_label()}")
except Exception as e:
    print(f"spawn op failed: {e}")
try:
    unreal.EditorLevelLibrary.save_current_level()
    print("saved current level")
except Exception as e:
    print(f"save op failed: {e}")
