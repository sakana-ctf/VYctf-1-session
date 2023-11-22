extends Sprite


func _on_Area2D_mouse_entered():
	print("\t[",position.x,",",position.y,"],")
	modulate = Color(0,0,0,1)
