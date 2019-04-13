def rmb_input(): 
    CN_yuan = input("请输入人民币金额：") # 输入人民币金额
    while True:       
        if CN_yuan.isdigit():
            rmb = int(CN_yuan)
            break
        else:
            CN_yuan = input('请重新输入正确的人民币金额：')
            continue

    return rmb


def dollar_exchange(rmb):  # 换算美元
    exchange_rate = 6.77
    dollar = rmb/exchange_rate
    return dollar


def main():  # running
    rmb = rmb_input()
    dollar = dollar_exchange(rmb)
    print("按汇率兑换的美元金额为：{0:.2f}".format(dollar))


main()