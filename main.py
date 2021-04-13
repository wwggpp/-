import xlrd
import random
import time


def read_excel_xls(path):
    workbook = xlrd.open_workbook(path)
    sheets = workbook.sheet_names()
    worksheet = workbook.sheet_by_name(sheets[0])
    dict = []
    for i in range(0, worksheet.nrows):
        eng = worksheet.cell_value(i, 0)
        chi = worksheet.cell_value(i, 1)
        if (" " in eng):
            eng = eng.replace(" ", "")
        if ("." in eng):
            eng = eng.replace(".", "")
        if (" " in chi):
            chi = chi.replace(" ", "")
        if ("." in chi):
            chi = chi.replace(".", "")
        dict.append(("{}:{}".format(eng, chi)))
    return len(dict), dict


def main():
    path = "./vocabulary.xlsx"
    tot_num, voc = read_excel_xls(path)
    print("乱序背单词程序\n词库为自己挑选单词\n输入 ”y“ 或 ”Y“ 开始背单词\n结束背单词请输入 ”exit“")
    begin = str(input('input here:'))
    if begin == 'exit':
        print('程序结束，即将自动退出')
        return 0
    while begin != "y" and begin != "Y":
        print()
        print("input error, try again!")
        begin = str(input('input here:'))
    else:
        while 1:
            sel = str(input("输入 “w” 选择输入单词模式，输入 “n” 选择其他模式\ninput here:"))
            nums = list(range(0, tot_num))
            print("词库生成完毕")
            if sel == 'w' or sel == 'W':
                print()
                print("输入模式，请努力作答\n输入 ”exit“ 结束背单词\n按 “r” 重新选择模式")
                while 1:
                    if len(nums) == 0:
                        print("词库全部单词复习完毕")
                        break
                    i = random.choice(nums)
                    nums.remove(i)
                    sample = voc[i]
                    eng, chi = sample.split(':')
                    print()
                    print(chi, ":", end="")
                    ans = str(input())
                    if ans == "exit":
                        print()
                        print("程序结束，即将自动退出")
                        time.sleep(0.5)
                        return 0
                    elif ans == 'r' or ans == 'R':
                        print()
                        print('重新选择模式')
                        break
                    elif ans == eng:
                        print("bingo!")
                    else:
                        print("wrong! 正确答案为：{}".format(eng))
            elif sel == 'n' or sel == 'N':
                print("其他模式，按回车显示单词，再次按回车显示中文\n按 “r” 重新选择模式")
                while 1:
                    if len(nums) == 0:
                        print("词库全部单词复习完毕")
                        break
                    i = random.choice(nums)
                    nums.remove(i)
                    sample = voc[i]
                    eng, chi = sample.split(':')
                    print(eng, end="")
                    ans = input()
                    if ans == 'r' or ans == 'R':
                        print()
                        print('重新选择模式')
                        break
                    elif ans == 'exit':
                        print('程序结束，即将自动退出')
                        time.sleep(0.5)
                        return 0
                    print(chi)
                    ans = input()
                    if ans == 'r' or ans == 'R':
                        print()
                        print('重新选择模式')
                        break
                    elif ans == 'exit':
                        print('程序结束，即将自动退出')
                        time.sleep(0.5)
                        return 0




if __name__ == "__main__":
    main()