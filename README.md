# My-Python-Learning-Journey
## 项目介绍：两人费用分摊计算器
### 项目建立的原因
  我们和朋友出去玩的时候可能会遇到一种情况，那就是AA。但是每次结束之后要计算每个活动的钱，以及这个钱是谁付的，我们需要给对方多少钱，或者对方需要给我们多少钱。项目较少的时候容易计算，但是项目一多可能就容易乱。因此从这个需求出发，建立此项目：两人费用分摊计算器。
### 如何运行
  使用分摊计算器时，首先要输入参与计算的两个人的名字。其次是记录消费项目、消费金额以及付款人，并将信息记录到消费列表。
```
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
```
  在输入和保存数据之后，要对数据进行计算。简单的思路就是计算总金额，再计算平均每个人应该付多少钱，每个人实际已经支付的钱与平均值相比较，若低于平均值，就应该给对方转钱，若高于平均值，就可以得到对方的转账。代码计算如下。
```
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
```
## 学习心得与规划
  GitHub是一个非常强大的python学习平台，上面有非常丰富的资源，很多开源的项目可以借鉴。除此之外还可以找到非常多的学习资源，比如可以从上面下载一些英语学习资料等等。在完成本次任务的过程中，我学会了如何通过git命令上传项目到GitHub。
  对于管理个人项目，GitHub靠分支管理多任务，还可以每一次修改都有记录，避免文件冗余，功能强大。仓库README写清项目背景、技术栈、核心功能与演示链接，比简历上 “熟练使用 Python” 更有说服力。
  可以用GitHub搭建专属学习仓库，分类管理内容，包括例如for循环板块、调用函数板块，清晰避免混乱。可以存知识点笔记，并附上实操代码，方便复盘。
