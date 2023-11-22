import os

fn main() {
	if os.args.len < 2 {
		println('\033[31m[false] \033[0m请至少添加一个文件!')
		exit(1)
	}

	mut return_filename := os.args[1]
	program := os.read_file(return_filename) or {
		println('\033[31m[false] \033[0m找不到文件')
		exit(1)
	}
	return_filename_suffix := return_filename#[-3..]
	if return_filename_suffix == ".bf" {
		return_filename = return_filename#[..-3] + '.txt'
	}else{
		println('\033[33m[warn] \033[0m文件后缀名不是".bf",将自动保留信息为default.txt文件')
		return_filename = "default.txt"
	}

	mut new_file := os.create(return_filename)!

	mut memory := []u8{len: 256}
	mut address := u8(0)
	mut stack := []int{}
	mut program_counter := 0

	for program_counter < program.len {
		match program[program_counter] {
			`O` {
				address++
			}
			`w` {
				address--
			}
			`*` {
				memory[address]++
			}
			`@` {
				memory[address]--
			}
			`.` {
				data := memory[address].ascii_str() 
				new_file.write_string(data)!
				print(data)
			}
			`,` {
				input := os.input_opt('') or { '' }
				memory[address] = input[0]
			}
			`v` {
				stack << program_counter
			}
			`~` {
				if memory[address] != 0 {
					program_counter = stack[stack.len - 1]
				} else {
					stack.pop()
				}
			}
			else {}	
		}
		program_counter++
	}
	new_file.close()
	println("")
}

