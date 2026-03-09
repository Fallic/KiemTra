def calcREP():
    a = float(input("Nhập số thứ nhất: "))
    b = float(input("Nhập số thứ hai: "))
    phep_toan = input("Nhập phép toán (+, -, *, /): ")

    if phep_toan == "+":
        print("Kết quả:", a + b)
    elif phep_toan == "-":
        print("Kết quả:", a - b)
    elif phep_toan == "*":
        print("Kết quả:", a * b)
    elif phep_toan == "/":
        if b != 0:
            print("Kết quả:", a / b)
        else:
            print("Không thể chia cho 0")
    else:
        print("Phép toán không hợp lệ")


if __name__ == "__uu__":
    calcREP()