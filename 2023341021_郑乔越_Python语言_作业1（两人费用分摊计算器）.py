print('欢迎使用两人费用分摊计算器')
#首先输入用户的名字
person1 = input('请输入第一个人的名字：')
person2 = input('请输入第二个人的名字：')
expenses = []#用来存储消费记录
#记录消费项目
while True:
    print('请输入消费信息（输入“结束”退出）')
    description = input('消费项目：')
    if description == '结束':
        break
    #记录消费金额
    while True:
        amount = float(input('消费金额：'))
        if amount <= 0:
            print('消费金额必须大于0，请重新输入')
            continue
        break
#记录付款人
    print('请选择付款人：1.'+ person1 + '2.'+person2)
    while True:
        payerchoice = input('1 or 2 ?')
        if payerchoice =='1':
            payer = person1
            break
        elif payerchoice =='2':
            payer = person2
            break
        else:
            print('请输入1或2')        
            continue
#记录到消费列表
    expenses.append({
        '消费项目':description,
        '消费金额':amount,
        '付款人':payer
        })
if not expenses:
    print('没有输入消费记录')
else:
#计算每个人的支付总金额
    total_each_person = {person1: 0,person2:0}#初始每个人的支付总金额
    for expense in expenses:
        total_each_person[expense['付款人']] += expense['消费金额']
#总金额
    total = 0
    for money in total_each_person.values():
        total += money
#每个人承担的金额
    total_each = total/2
    print('总消费金额：',total ,'元\n',
          '每个人应承担',total_each ,'元\n',
          person1+'已支付：',total_each_person[person1],'元\n',
          person2+'已支付：',total_each_person[person2],'元') 
    if total_each_person[person1] > total_each_person[person2]:
        pay = total_each_person[person1]-total_each
        print(person2+'需要转',pay,'元给'+person1)
    elif total_each_person[person1] < total_each_person[person2]:
        pay = total_each_person[person2]-total_each
        print(person1+'需要转',pay,'元给'+person2)
    else:
        print('双方无需转账')
    


    