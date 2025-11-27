import sys
if len(sys.argv)!=3:
    print("usage : python script.py <weight> <height>")
    weight=80
    height=9
else :
    script_name=sys.argv[0]
    weight=float(sys.argv[1])
    height=(sys.argv[2])
bmi = weight / (height * height)
print("BMI is ",bmi)