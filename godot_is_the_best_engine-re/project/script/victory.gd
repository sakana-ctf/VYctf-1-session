extends Node2D

func _ready():
	Global.level -= 1
	pass

func _on_play_button_down():
	var error_code = get_tree().change_scene("res://scene/title.tscn")
	if error_code != 0:
		print("输出错误结果:",error_code)
	pass
