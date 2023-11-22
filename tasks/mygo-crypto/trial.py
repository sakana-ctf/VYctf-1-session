from random import randint as rt

flag = "VYctf{fake_flag}"

print("""
              ,~~>i1}}}1+>!~~~`!"':               
           :'!"!~!~~'~~~~~~~~!>>~~"!:            
        ,i}>"i~"!~"~~~~~>'>"~~~~~!"+/"!,         
       :"+>~/">i'~"~"~~~'i!~l>'~i~~~">>i~!;       
      ""i'i1i1'~"">"'~~';++;/]]i">+;~'++>+}+`     
     `}}!!l}1''>">+'~~~~;+1'/}}}i+1i;~~"~il*];    
    `}1i']*/'~i1>1+'~~i!'1}>}}11}+}l!''~+]l/1};   
    ,]1!"l1~!>}//l+"!!/~~}1/}111}}+]+'~~"~~+]]"   
    >>+"+]"ii} lKX/+~ii"+}}}11*W %N&/~~~i*l}+}}'  
    /l]"/]11}] *%El1>/>]}}}11}1l X%W+'~"+***IXKF/,
`*FXX#*!}]}11}#%%E*}}11111111}}]#%%E/'~i}***YEFX*I
YY*YF$I!1/1}}1FEEK]}}11111111}}1&EEK/~~+}***XEEYY]
]1iY&Wl"}1}}]]}11111111111111111}11}/""i*****YX$FY
]i~]FE1i }}1111lI]/}}]]]]]]]]]}11I*}/i>i****}]FY1'
}"~~~!>}  l}111}11X           #K}1}111>"****}~]&YX
1!~~~!i]    l}}}}}1}Y&&FXF&&&Xl1}}}}}]>~]***};!*IF
+~~~!"}           l]}}}}}}}}}}]]i'}   >'1***]! il!
i~~~~i]         lll**IIIIIII*ll*l}  ,l!;i***]>  }/
+'!!'1+~lll  l}1]i+}+"1:::...:/ii]1}l/;'>**l]/   i
"~"'!1.>]]l ]1}l>'}}!+]".....;1};>l}}";'i*l]l}!   

""")

a = int(input(">Welcome to Sakiko's trials!\n first data:"))
b = int(input(" second data:"))

magic_number = 23456789

# 你对组乐团感兴趣吗?
if b <= 0:
    print("Please make me forget everything.\n")
    exit(0)

if pow(magic_number, a - 1, a) != 1:
    print("I wish you happiness.\n")
    exit(0)

# 弱小的我已经死掉了.
trial_numbers = [rt(0, 26) for i in range(10)]

for number in trial_numbers:
    c = a + b * number
    if pow(magic_number, c - 1, c) != 1:
        print("You can't be soyo's mouthpiece.\n")
        exit(0)

# 我无畏遗忘.
d = a + b * max(trial_numbers)
if (d.bit_length() < 55):
    print(f"Welcome to ave mujica, your flag is: {flag}")
else:
    print("thank you for your feedback, but I'm not your mouthpiece.\n")
