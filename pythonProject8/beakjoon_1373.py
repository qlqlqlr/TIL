def binary_to_octal(binary):
    decimal = int(binary, 2)  # 2진수 문자열을 10진수로 변환
    octal = ''  # 8진수로 변환된 문자열

    # 10진수를 8진수로 변환
    while decimal > 0:
        remainder = decimal % 8
        octal = str(remainder) + octal
        decimal //= 8

    return octal

num = input()  # 입력 받은 2진수 문자열
octal_result = binary_to_octal(num)  # 2진수를 8진수로 변환

print(octal_result)