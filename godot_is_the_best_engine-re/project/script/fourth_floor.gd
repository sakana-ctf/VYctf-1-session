extends Node2D

var labor = preload('res://scene/labor.tscn')
var soldier = preload('res://scene/soldier.tscn')

onready var player = $player
onready var player_area = $player/Area2D
onready var ai = $AI
onready var timer = $Timer
onready var tween = $Tween
onready var table_first = $TileMap/city/Table01
onready var table_second = $TileMap/city/Table02
onready var table_third = $TileMap/city/Table03
onready var box_first = $TileMap/cabin/Box01
onready var box_second = $TileMap/cabin/Box02
onready var board_first = $TileMap/cabin/Board01
onready var vents_first = $TileMap/cabin/Vents1
onready var vents_second = $TileMap/cabin/Vents2

const office_y = 12
const cabin_y = 264
const hero_move = 80

var bunker_bool:bool = false
var vents_bool:bool = false
var hide_in_bunker:bool = false
var hide_in_vents:bool = false
var skill_cool_down:bool = true

# ==================主程序=======================	
func _ready():
	player.position.x = -540
	player.play("stop")
	ai.play("stop")
	role_object(labor, office_y, -200, 10, 80)
	role_object(labor, office_y, -208, -20, 60)
	role_object(labor, office_y, -120, 10, 90)
	role_object(labor, office_y, -450, -250, 90)
	role_object(labor, office_y, 100, 250, 70)
	role_object(labor, office_y, -370, 0, 50)
	role_object(soldier, cabin_y, -400, 200, 80)
	role_object(soldier, cabin_y, 150, 250, 100)
	role_object(soldier, cabin_y, -100, -30, 60)
	role_object(soldier, cabin_y, -300, -150, 100)
	pass

func _process(delta):
	# 跳跃能力部分
	if Input.get_action_raw_strength("jump_skill") and not hide_in_bunker:
		move_hero_y()
		skill_cool_down = false
	# x轴移动部分	
	if Input.get_action_raw_strength("move_right") and not hide_in_bunker:
		player.flip_h = false
		player.position.x = clamp(player.position.x + hero_move * delta,-550,295)
		player.animation = "move"
	elif Input.get_action_raw_strength("move_left") and not hide_in_bunker:
		player.flip_h = true
		player.position.x = clamp(player.position.x - hero_move * delta,-550,295)
		player.animation = "move"
	else:
		player.animation = "stop"
	
	# 躲藏功能
	if Input.get_action_raw_strength("active") and bunker_bool and skill_cool_down:
		skill_cool_down = false
		timer.start()
		if hide_in_bunker:
			player.show()
			player_area.set_collision_mask_bit(2, true)
			player_area.set_collision_layer_bit(2, true)
			player_area.monitorable = true
			hide_in_bunker = false
		else:
			player.hide()
			player_area.set_collision_mask_bit(2, false)
			player_area.set_collision_layer_bit(2, false)
			hide_in_bunker = true
	
	# 穿梭隧道功能
	if Input.get_action_raw_strength("active") and vents_bool and skill_cool_down:
		skill_cool_down = false
		timer.start()
		if hide_in_vents:
			player.show()
			player_area.set_collision_mask_bit(2, true)
			player_area.set_collision_layer_bit(2, true)
			player_area.set_collision_mask_bit(0, true)
			player_area.set_collision_layer_bit(0, true)
			player_area.monitorable = true
			hide_in_vents = false
		else:
			player.hide()
			player_area.set_collision_mask_bit(2, false)
			player_area.set_collision_layer_bit(2, false)
			player_area.set_collision_mask_bit(0, false)
			player_area.set_collision_layer_bit(0, false)
			hide_in_vents = true
		

# =============一些工具函数==================	
# 对player的时间线移动进行判定	
func move_hero_y():
	if player.position.y == cabin_y and skill_cool_down:
		player.position.y = office_y
		timer.start()
	elif player.position.y == office_y and skill_cool_down:
		player.position.y = cabin_y
		timer.start()
	pass
	
# 用于限制能力与交互
func _on_Timer_timeout():
	skill_cool_down = true
	pass

# 调用场景角色
func role_object(node, the_y, the_x, where, rate):
	var new_node = node.instance()
	new_node.position = Vector2(the_x, the_y)
	new_node.go = the_x
	new_node.where = where
	new_node.rate = rate
	add_child(new_node)
	pass

# =============以下是用于处理交互物品的地方==================
### table ###
# table1判定
func _on_Area2D1_area_entered(area):
	bunker_bool = true
	table_first.modulate = Color(0.8,0.8,0.8,1) 
	pass	
func _on_Area2D1_area_exited(area):
	bunker_bool = false
	table_first.modulate = Color(0.88,0.88,0.88,1) 
	pass
	
# table2判定
func _on_Area2D2_area_entered(area):
	bunker_bool = true
	table_second.modulate = Color(0.8,0.8,0.8,1) 
	pass
func _on_Area2D2_area_exited(area):
	bunker_bool = false
	table_second.modulate = Color(0.88,0.88,0.88,1) 	
	pass
	
# table3判定
func _on_Area2D3_area_entered(area):
	bunker_bool = true
	table_third.modulate = Color(0.8,0.8,0.8,1) 
	pass
func _on_Area2D3_area_exited(area):
	bunker_bool = false
	table_third.modulate = Color(0.88,0.88,0.88,1) 
	pass

### box ###
# box1判定
func _on_Area2D4_area_entered(area):
	bunker_bool = true
	box_first.modulate = Color(1,1,1,1) 
	pass
func _on_Area2D4_area_exited(area):
	bunker_bool = false
	box_first.modulate = Color(0.75,0.75,0.75,1) 
	pass

# box2判定
func _on_Area2D5_area_entered(area):
	bunker_bool = true
	box_second.modulate = Color(1,1,1,1) 	
	pass # Replace with function body.
func _on_Area2D5_area_exited(area):
	bunker_bool = false
	box_second.modulate = Color(0.75,0.75,0.75,1)
	pass # Replace with function body.
	
# board1判定
func _on_Area2D6_area_entered(area):
	bunker_bool = true
	board_first.modulate = Color(1,1,1,1) 	
	pass # Replace with function body.
func _on_Area2D6_area_exited(area):
	bunker_bool = false
	board_first.modulate = Color(0.75,0.75,0.75,1) 	
	pass # Replace with function body.

### vents ###
# vents1判定
func _on_Area2D7_area_entered(area):
	vents_bool = true
	vents_first.modulate = Color(0.5,0.5,0.5,1) 
	pass # Replace with function body.
func _on_Area2D7_area_exited(area):
	vents_bool = false
	vents_first.modulate = Color(1,1,1,1) 
	pass
	
# vents2判定
func _on_Area2D8_area_entered(area):
	vents_bool = true
	vents_second.modulate = Color(0.5,0.5,0.5,1) 
	pass # Replace with function body.
func _on_Area2D8_area_exited(area):
	vents_bool = false
	vents_second.modulate = Color(1,1,1,1) 
	pass # Replace with function body.

### 通道 ###
# come判定
func _on_come_area_entered(area):
	get_tree().change_scene("res://scene/third_floor.tscn")
	pass
