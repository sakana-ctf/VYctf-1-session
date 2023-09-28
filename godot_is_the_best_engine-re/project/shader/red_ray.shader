shader_type canvas_item;

uniform vec4 ray_color : hint_color;


void fragment() {	
	vec4 col = texture(SCREEN_TEXTURE,SCREEN_UV);
	if (cos(TIME) > 0.0){
		COLOR = col * ray_color * cos(TIME);
		COLOR += 0.2;
	}else{
		COLOR = col * ray_color * -cos(TIME);
		COLOR += 0.2
	}
}
