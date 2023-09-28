extends Node2D

onready var clocktower = $ClockTower
onready var tween = $Tween
onready var button = $button
onready var audio = $AudioStreamPlayer
onready var mass = $massage

func _ready():
	audio.play()
	pass

func position_tween(node, go, where):
	tween.interpolate_property(
		node, "position:x",
		go, where,
		1, Tween.TRANS_QUINT
	)
	tween.start()
	pass

func _on_exit_button_down():
	get_tree().quit()
	pass # Replace with function body.


func _on_developer_button_down():
	position_tween(clocktower, 509.111, 450)
	position_tween(button, 0, -350)
	position_tween(mass, 950, 30)
	pass # Replace with function body.


func _on_return_button_down():
	position_tween(clocktower, 450, 509.111)
	position_tween(button, -350, 0)
	position_tween(mass, 30, 950)
	pass # Replace with function body.


func _on_play_button_down():
	var error_code = get_tree().change_scene("res://scene/main.tscn")
	if error_code != 0:
		print("输出错误结果:",error_code)
	pass # Replace with function body.
