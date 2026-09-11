#calculate_electricity_cost(units)
#1-50 2.50 per unit
#51-100 3.00 per unit
#101-200 3.50 per unit
#>200 4.00 per unit
#+ 25 bath per mouth
#press 1 for start press 2 for exit

def calculate_electricity_cost(units):
    if units <= 50:
        cost = units * 2.50
    elif units <= 100:
        cost = (50 * 2.50) + ((units - 50) * 3.00)
    elif units <= 200:
        cost = (50 * 2.50) + (50 * 3.00) + ((units - 100) * 3.50)
    else:
        cost = (50 * 2.50) + (50 * 3.00) + (100 * 3.50) + ((units - 200) * 4.00)
        
    total_cost = cost + 25
    return total_cost
print("==== โปรแกรมคำนวณค่าไฟฟ้า ====")
print("1, คำนวณค่าไฟ")
print("2, ออกจากโปรแกรม")
one_or_two = ""
while one_or_two != "2":
    one_or_two = input("เลือกเมนู: ")
    if one_or_two == "1":
        units = float(input("กรอกจำนวนหน่วยไฟฟ้า: "))
        total_cost = calculate_electricity_cost(units)
        if units <=50:
            print ("ค่าบริการ: 25 บาท")
            print (f"รวมค่าไฟทั้งสิ้น {units} หน่วย เป็นจำนวนเงิน: {total_cost:.2f} บาท")
        elif units <=100:
            print (f"1-50 หน่วย: 125 บาท")
            print (f"51-{units} หน่วย: {(units-50)*3:.2f} บาท")
            print ("ค่าบริการ: 25 บาท")
            print (f"รวมค่าไฟทั้งสิ้น {units} หน่วย เป็นจำนวนเงิน: {total_cost:.2f} บาท")
        elif units <=200:
            print (f"1-50 หน่วย: 125 บาท")
            print (f"51-100 หน่วย: 150 บาท")
            print (f"101-{units} หน่วย: {(units-100)*3.50:.2f} บาท")
            print ("ค่าบริการ: 25 บาท")
            print (f"รวมค่าไฟทั้งสิ้น {units} หน่วย เป็นจำนวนเงิน: {total_cost:.2f} บาท")
    elif one_or_two == "2":
        print("ออกแล้ว")
    else:
        print("เลือกเมนูไม่ถูกต้อง")





    