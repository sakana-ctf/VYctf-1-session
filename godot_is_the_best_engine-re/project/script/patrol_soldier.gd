extends AnimatedSprite

onready var timer = $Timer

var go:int = 0
var where:int = 100
var rate = 80

func _ready():
	if go == where:
		animation = "stop"
	else:
		animation = "move"
	play(animation)
	pass

func _process(delta):
	if go < where:
		if position.x <= where and not flip_h:
			position.x += rate * delta
		elif position.x > where and not flip_h:
			flip_h = true
		elif position.x >= go and flip_h:
			position.x -= rate * delta
		elif position.x < go and flip_h:
			flip_h = false
	elif go > where:
		if position.x <= go and not flip_h:
			position.x += rate * delta
		elif position.x > go and not flip_h:
			flip_h = true
		elif position.x >= where and flip_h:
			position.x -= rate * delta
		elif position.x < where and flip_h:
			flip_h = false 
	pass

func _on_Area2D_area_entered(_area):
	Global.stop = true
	timer.start()
	pass

func _on_Timer_timeout():
	var error_code = get_tree().change_scene("res://scene/defeat.tscn")
	if error_code != 0:
		print("输出错误结果:",error_code)
	pass
