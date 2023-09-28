extends Node2D

onready var ai = $AI
onready var player = $player
onready var labor_left = $labor_left
onready var labor_right = $labor_right
onready var soldier_left = $soldier_left
onready var soldier_right = $soldier_right
onready var none = $None
onready var to_name = $to_name
onready var speak = $Button/speak
var speak_line = 3
var data
var data_line = 0
var role

func _ready():
	Global.dialog_bool = true
	main()
	pass

func new_words(words):
	if speak_line == 3:
		speak_line = 0
		speak.text = words
	else:
		speak.text += "\n" + words
	speak_line += 1
	pass

func move_role(name,node):
	if node.position.x > 0:
		to_name.margin_left = -440
		to_name.margin_right = -340
		speak.align = 0
	else:
		to_name.margin_left = 340
		to_name.margin_right = 440
		speak.align = 2
	to_name.text = name
	data_line += 1
	speak_line = 3
	ai.hide()
	player.hide()
	soldier_left.hide()
	soldier_right.hide()
	labor_left.hide()
	labor_right.hide()
	node.show()
	pass

func main():
	if data_line == len(data):
		Global.dialog_bool = false
		queue_free()
	else:
		if data[data_line] == "AI":
			move_role("艾(AI)",ai)
		elif data[data_line] == "player":
			move_role("主  角",player)
		elif data[data_line] == "soldier1":
			move_role("士兵1",soldier_left)
		elif data[data_line] == "soldier2":
			move_role("士兵2",soldier_right)
		elif data[data_line] == "labor1":
			move_role("职员1",labor_left)
		elif data[data_line] == "labor2":
			move_role("职员2",labor_right)
		elif data[data_line] == "None":
			move_role("提  示",none)
		new_words(data[data_line])
		data_line += 1
	pass

# ============ 触发方式 ===================
func _on_Button_button_down():
	main()
	pass
func _input(event):
	if event.is_action_pressed("dialog_next"):
		main()
	pass
