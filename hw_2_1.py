# 身体质量指数BMI
weight, height = eval(input('请输入您的体重（kg）与身高(m),以逗号分隔:'))

int_weight = int(weight)
int_height = float(height)
int_height_2 = pow(int_height,2)

bmi = int_weight / int_height_2
# bmi = bmi_0.format('%.2f')

if bmi < 18.5:
    print(f"您的身体质量指数BMI为: {round(bmi,2)},too thin")
elif 18.5 <= bmi <= 23.9:
    print(f"您的身体质量指数BMI为: {round(bmi,2)},normal")
elif 24 <= bmi <= 27.9 :
    print(f"您的身体质量指数BMI为: {round(bmi,2)},overweight")
else:
    print(f"您的身体质量指数BMI为: {round(bmi,2)},fat")

