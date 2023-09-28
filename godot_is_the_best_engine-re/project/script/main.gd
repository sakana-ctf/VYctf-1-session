extends Node2D

var labor = preload('res://scene/labor.tscn')
var soldier = preload('res://scene/soldier.tscn')
var dialog = preload('res://scene/dialog.tscn')
var linshi_node = preload('res://scene/linshi.tscn')


onready var global_camera = $Camera
onready var player_camera = $player/Camera
onready var player_mirror = $player/player_mirror
onready var player = $player
onready var player_anima = $player/hero
onready var player_area = $player/hero/Area2D
onready var player_sign = $player/sign
onready var ai = $AI
onready var timer = $Timer
onready var tween = $Tween
onready var tween_timer = $Tween/Tween_Timer
onready var table_first = $TileMap/city/Table01
onready var table_second = $TileMap/city/Table02
onready var table_third = $TileMap/city/Table03
onready var box_first = $TileMap/cabin/Box01
onready var box_second = $TileMap/cabin/Box02
onready var board_first = $TileMap/cabin/Board01
onready var vents_first = $TileMap/cabin/Vents1
onready var vents_second = $TileMap/cabin/Vents2
onready var audio = $AudioStreamPlayer
onready var layer = $CanvasLayer



const office_y = 12
const cabin_y = 264
const hero_move = 80

var bunker_bool:bool = false
var vents_bool:bool = false
var hide_in_bunker:bool = false
var hide_in_vents:bool = false
var skill_cool_down:bool = true
var cut_camera:bool = false

var linshi
var dialog_node

# ==================主程序=======================	
func _ready():
	player_camera.current = true
	player_sign.hide()
	player.position.x = 300
	player_anima.play("stop")
	ai.play("stop")
	linshi = linshi_node.instance()
	add_child(linshi)
	pass

func _process(delta):
	# 跳跃能力部分
	if Input.get_action_raw_strength("jump_skill") and not hide_in_bunker and not hide_in_vents and not Global.stop:
		move_hero_y()
		skill_cool_down = false
	# x轴移动部分	
	if Input.get_action_raw_strength("move_right") and not hide_in_bunker and not Global.stop:
		player_anima.flip_h = false
		player.position.x = clamp(player.position.x + hero_move * delta,-550,295)
		player_anima.animation = "move"
	elif Input.get_action_raw_strength("move_left") and not hide_in_bunker and not Global.stop:
		player_anima.flip_h = true
		player.position.x = clamp(player.position.x - hero_move * delta,-550,295)
		player_anima.animation = "move"
	else:
		player_anima.animation = "stop"
	
	# 躲藏功能
	if Input.get_action_raw_strength("active") and bunker_bool and skill_cool_down and not Global.dialog_bool and not Global.stop and not cut_camera:
		skill_cool_down = false
		timer.start()
		if hide_in_bunker:
			player_sign.hide()
			player_anima.show()
			player_area.set_collision_mask_bit(2, true)
			player_area.set_collision_layer_bit(2, true)
			player_area.monitorable = true
			hide_in_bunker = false
		else:
			player_sign.show()
			player_anima.hide()
			player_area.set_collision_mask_bit(2, false)
			player_area.set_collision_layer_bit(2, false)
			hide_in_bunker = true
	
	# 穿梭隧道功能
	if Input.get_action_raw_strength("active") and vents_bool and skill_cool_down and not Global.dialog_bool and not Global.stop and not cut_camera:
		skill_cool_down = false
		timer.start()
		if hide_in_vents:
			player_anima.show()
			player_sign.hide()
			player_area.set_collision_mask_bit(2, true)
			player_area.set_collision_layer_bit(2, true)
			player_area.set_collision_mask_bit(0, true)
			player_area.set_collision_layer_bit(0, true)
			player_area.monitorable = true
			hide_in_vents = false
		else:
			audio.play()
			player_anima.hide()
			player_sign.show()
			player_area.set_collision_mask_bit(2, false)
			player_area.set_collision_layer_bit(2, false)
			player_area.set_collision_mask_bit(0, false)
			player_area.set_collision_layer_bit(0, false)
			hide_in_vents = true
	# 观察功能
	if Input.get_action_raw_strength("cut_camera"):
		if not hide_in_bunker and not hide_in_vents: 
			player_mirror.show()
		global_camera.current = true
		cut_camera = true
	else:
		player_mirror.hide()
		player_camera.current = true
		cut_camera = false
	
	# 死亡前摇
	if Global.stop:
		modulate = Color(1,0.85,0.85,1)
	else:
		modulate = Color(1,1,1,1)

# =============一些工具函数====================
# 角色移动的一些动画函数
var anima_node_global
var anima_new_global
func position_tween(node, old_x, new_x, time, anima_node, anima_old, anima_new):
	tween.interpolate_property(
		node, "position:x",
		old_x, new_x,
		time,  Tween.TRANS_LINEAR, Tween.EASE_IN_OUT
	)
	anima_node_global = anima_node
	anima_new_global = anima_new
	anima_node_global.animation = anima_old
	tween_timer.wait_time = time
	tween_timer.start()
	tween.start()
	pass
func _on_Tween_Timer_timeout():
	anima_node_global.animation = anima_new_global
	pass

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
func role_object(node, the_y, the_x, where, rate, flip_h):
	var new_node = node.instance()
	new_node.flip_h = flip_h
	new_node.position = Vector2(the_x, the_y)
	new_node.go = the_x
	new_node.where = where
	new_node.rate = rate
	linshi.add_child(new_node)
	pass

# =============以下是用于处理交互物品的地方==================
### table ###
# table1判定
func _on_Area2D1_area_entered(_area):
	bunker_bool = true
	table_first.modulate = Color(0.8,0.8,0.8,1) 
	pass	
func _on_Area2D1_area_exited(_area):
	bunker_bool = false
	table_first.modulate = Color(0.88,0.88,0.88,1) 
	pass
	
# table2判定
func _on_Area2D2_area_entered(_area):
	bunker_bool = true
	table_second.modulate = Color(0.8,0.8,0.8,1) 
	pass
func _on_Area2D2_area_exited(_area):
	bunker_bool = false
	table_second.modulate = Color(0.88,0.88,0.88,1) 	
	pass
	
# table3判定
func _on_Area2D3_area_entered(_area):
	bunker_bool = true
	table_third.modulate = Color(0.8,0.8,0.8,1) 
	pass
func _on_Area2D3_area_exited(_area):
	bunker_bool = false
	table_third.modulate = Color(0.88,0.88,0.88,1) 
	pass

### box ###
# box1判定
func _on_Area2D4_area_entered(_area):
	bunker_bool = true
	box_first.modulate = Color(1,1,1,1) 
	pass
func _on_Area2D4_area_exited(_area):
	bunker_bool = false
	box_first.modulate = Color(0.75,0.75,0.75,1) 
	pass

# box2判定
func _on_Area2D5_area_entered(_area):
	bunker_bool = true
	box_second.modulate = Color(1,1,1,1) 	
	pass # Replace with function body.
func _on_Area2D5_area_exited(_area):
	bunker_bool = false
	box_second.modulate = Color(0.75,0.75,0.75,1)
	pass # Replace with function body.
	
# board1判定
func _on_Area2D6_area_entered(_area):
	bunker_bool = true
	board_first.modulate = Color(1,1,1,1) 	
	pass # Replace with function body.
func _on_Area2D6_area_exited(_area):
	bunker_bool = false
	board_first.modulate = Color(0.75,0.75,0.75,1) 	
	pass # Replace with function body.

### vents ###
# vents1判定
func _on_Area2D7_area_entered(_area):
	vents_bool = true
	vents_first.modulate = Color(0.5,0.5,0.5,1) 
	pass # Replace with function body.
func _on_Area2D7_area_exited(_area):
	vents_bool = false
	vents_first.modulate = Color(1,1,1,1) 
	pass
	
# vents2判定
func _on_Area2D8_area_entered(_area):
	vents_bool = true
	vents_second.modulate = Color(0.5,0.5,0.5,1) 
	pass # Replace with function body.
func _on_Area2D8_area_exited(_area):
	vents_bool = false
	vents_second.modulate = Color(1,1,1,1) 
	pass # Replace with function body.

### 通道 ###
# come判定
func _on_come_area_entered(_area):
	linshi.free()
	linshi = linshi_node.instance()
	add_child(linshi)
	if Global.level == 0:
		Global.level = 1
		first_floor()
		print("第一关")
	elif Global.level == 1:
		Global.level = 2
		second_floor()
		print("第二关")
	elif Global.level == 2:
		Global.level = 3
		third_floor()
		print("第三关")
	elif Global.level == 3:
		Global.level = 4
		fourth_floor()
		print("第四关")
	else:
		Global.level = 1
		get_tree().change_scene("res://scene/victory.tscn")
	player.position.x = -540
	# 不知道为什么开局会有执行一次_on_Area2D6_area_exited(_area)函数, 导致出现bug开始可以在非区域隐藏的bug
	bunker_bool = false
	pass

# 判定对话系统(第三关处)
func _on_Area2D_area_entered(_area):
	if Global.level == 3:
		dialog_node = dialog.instance()
		dialog_node.data = [
			"player",
			"糟糕",
			"前面过不去了",
			"AI",
			"冷静, 这里有个下水道",
			"player",
			"只能通过下水道下去了吗?",
			"你不是神吗, 快想想办法让我空间转移过去呀",
			"AI",
			"笨蛋",
			"这样只会让故事性变得不幸",
			"自己慢慢爬过去吧",
			"None",
			"在下水道口可通过按下`Space`或`W`键进行操作"
		]
		ai.position.x = -400
		layer.add_child(dialog_node)
	pass

# ==================关卡设计=======================
func first_floor():
	player.position.y = cabin_y
	role_object(labor, office_y, -200, 10, 60, false)
	role_object(soldier, cabin_y, 100, 100, 60, false)
	role_object(soldier, cabin_y, -300, -300, 60, false)
	role_object(soldier, cabin_y, -200, 150, 80, false)
	role_object(soldier, cabin_y, -400, -100, 100, false)
	dialog_node = dialog.instance()
	dialog_node.data = [
		"None",
		"通过按下`H`键跳转回办公楼",
		"player",
		"竟然回来了, 还是在办公楼里面",
		"大家应该还在外面抗议吧",
		"AI",
		"我给你的能力现在只能修复这栋楼",
		"外面对于你来说依旧很混乱",
		"可争取不要被丢出去哦",
		"player",
		"啊......那我要做什么才能让一切恢复正常?",
		"AI",
		"现在可以确定的是",
		"造成你们时间线变动的原因是时钟塔被雷劈中出现故障",
		"player",
		"也就是说如果我把时钟塔修好以后时间线就能恢复正常了?",
		"AI",
		"总之先试着爬上时钟塔吧",
		"作为被我宠幸的仆人",
		"恢复正常后至少应该帮我找出造成变动的原因吧",
		"player",
		"不是才说了时钟塔出现故障才出现时间线变动的吗......",
		"None",
		"注意向上爬的过程不要被人发现, 在掩体附近按`Space`或`W`可进行躲藏"
	]
	position_tween(ai, -200, -400, 10, ai, "move", "stop")
	layer.add_child(dialog_node)
	pass

func second_floor():
	role_object(labor, office_y, -200, 10, 60, false)
	role_object(labor, office_y, -500, -500, 60, true)
	role_object(soldier, cabin_y, -400, -400, 80, true)
	role_object(labor, office_y, -200, -200, 60, true)
	role_object(labor, office_y, -150, 100, 40, false)
	role_object(labor, office_y, -180, 100, 90, false)
	role_object(soldier, cabin_y, -90, -10, 80, false)
	role_object(soldier, cabin_y, -300, -200, 60, false)
	dialog_node = dialog.instance()
	
	dialog_node.data = [
		"AI",
		"哈哈哈哈哈",
		"被吓到了吧",
		"player",
		"什么意思?",
		"糟糕, 前面的路被堵住了",
		"快帮帮忙吧",
		"AI",
		"你是笨蛋吗?",
		"player",
		"?!",
		"AI",
		"我给了你修复这栋楼时间和空间的能力",
		"但是用还是不用都取决于你",
		"None",
		"按下`H`键可再次回到船舱",
		"AI",
		"这样吧, 考虑到仅凭你的视点通过会比较困难",
		"我决定赏赐这次被我宠幸的仆人一项能力",
		"现在你也可以像我一样拥有完整的视点了",
		"None",
		"按下`L`键可以获取完整视角",
		"player",
		"什么意思",
		"但是我好像什么都感觉不到",
		"AI",
		"放心, 我的仆人会指引你的",
		"player",
		"仆人......",
		"不是指我吗?"
	]
	ai.position.x = -400
	layer.add_child(dialog_node)
	pass
	
func third_floor():
	role_object(labor, office_y, 10, -200, 60, true)
	role_object(labor, office_y, -208, -10, 80, false)
	role_object(labor, office_y, -10, -150, 90, true)
	role_object(labor, office_y, -150, -50, 40, false)
	role_object(labor, office_y, -200, 10, 100, false)
	role_object(labor, office_y, -400, -250, 90, false)
	role_object(labor, office_y, -370, -10, 90, false)
	role_object(soldier, cabin_y, -450, -450, 90, false)
	role_object(soldier, cabin_y, -400, -400, 90, true)
	role_object(soldier, cabin_y, -10, -10, 60, true)
	role_object(soldier, cabin_y, -400, -215, 100, false)
	dialog_node = dialog.instance()
	dialog_node.data = [
		"soldier1",
		"怎么好像听到了猫叫?",
		"soldier2",
		"可能是从哪个乱时空被吸引来的吧",
		"不管了, 猫可比那些引起混乱的人安全多了",
		"soldier1",
		"可爱即是正义!",
		"player",
		"猫, 难道是它的声音吗?",
		"`乱时空`还有`引起混乱的人`又是什么意思呢?"
	]
	ai.position = Vector2(-280, 240)
	layer.add_child(dialog_node)
	pass

func fourth_floor():
	role_object(labor, office_y, -200, 10, 80, false)
	role_object(labor, office_y, -208, -20, 60, false)
	role_object(labor, office_y, -120, 10, 90, false)
	role_object(labor, office_y, -450, -250, 90, false)
	role_object(labor, office_y, 100, 250, 70, false)
	role_object(labor, office_y, -370, 0, 50, false)
	role_object(soldier, cabin_y, -400, 200, 80, false)
	role_object(soldier, cabin_y, 150, 250, 100, false)
	role_object(soldier, cabin_y, -100, -30, 60, false)
	role_object(soldier, cabin_y, -300, -150, 100, false)
	dialog_node = dialog.instance()
	dialog_node.data = [
		"soldier1",
		"我们什么时候能够回去?",
		"soldier2",
		"你还不知道吗?",
		"这里的时间早就停下来了",
		"现在还在流动的是其他地方的时间",
		"soldier1",
		"我肯定知道啊",
		"也不知道大犬座的干扰该怎么解决",
		"soldier2",
		"感觉没什么希望了",
		"那些研究员整天神神叨叨的, 像是放弃了一样",
		"soldier1",
		"为什么我们不直接抢夺别的时空再作打算呢?",
		"AI",
		"喵呜",
		"soldier2",
		"哪里来的野猫?"
	]
	ai.position = Vector2(200, 243)
	layer.add_child(dialog_node)
	pass
