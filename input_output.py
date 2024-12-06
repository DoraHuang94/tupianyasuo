def main():
    # 获取用户输入
    print("欢迎使用输入输出程序！")
    name = input("请输入你的名字：")
    age = input("请输入你的年龄：")
    
    try:
        # 将年龄转换为整数
        age = int(age)
        
        # 输出信息
        print("\n===== 个人信息 =====")
        print(f"姓名：{name}")
        print(f"年龄：{age}")
        
        # 根据年龄输出不同信息
        if age < 18:
            print("你还是未成年人")
        elif age < 35:
            print("你正值青春年华")
        else:
            print("你是一位成熟的人")
            
    except ValueError:
        print("错误：年龄必须是数字！")

if __name__ == "__main__":
    main() 