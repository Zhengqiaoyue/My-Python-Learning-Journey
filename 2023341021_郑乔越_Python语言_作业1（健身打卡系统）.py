print('欢迎使用健身打卡系统')
print('请选择:\n',
      '1.记录今日运动\n',
      '2.查看运动总时长\n',
      '3.统计每种运动累计时长和平均时长\n',
      '4.退出系统')
records = []#在循环之外，确保数据不会被更改
while True:
    choice = int(input('请输入序号：'))

 #1.记录今日运动
    if choice == 1:
        sport_type = input('请输入运动类型（中强度/高强度）：')
        duration = int(input('运动时长（分钟）：'))
        records.append({
            '运动类型':sport_type,
            '运动时长':duration
            })
        print('记录成功')
#2.查看运动总时长
    elif choice == 2:
        if not records:
            print('暂无打卡记录')
            continue       
        else:  
            totaltime = 0
            for record in records:
                totaltime += record['运动时长']
            print('运动总时长为：',totaltime,'分钟')
#3.统计每种运动累计时长    
    elif choice == 3:
        if not records:
            print('暂无打卡记录')
            continue
        else:
            sport_state = {'中强度':0,'高强度':0}#用字典记录中高强度运动的累计时间
            count_state = {'中强度':0,'高强度':0}#用字典记录中高强度运动的分别的次数
            for record in records:
                sport_state[record['运动类型']] += record['运动时长']#累计时间
                count_state[record['运动类型']] += 1#累计次数
            print('中强度的运动时长为：',sport_state['中强度'],'分钟\n',
                  '高强度的运动时长为：',sport_state['高强度'],'分钟')
            if count_state['中强度'] > 0:
                middle = sport_state['中强度']/count_state['中强度']
            else:
                middle = 0#避免报错，这是没有中强度运动的情况
            if count_state['高强度'] > 0:
                high = sport_state['高强度']/count_state['高强度']  
            else:
                high = 0#避免报错，这是没有高强度运动的情况
            
            print('中强度运动平均时长为：'+str(middle)+'分钟\n',
                  '高强度运动平均时长为：'+str(high)+'分钟')
    elif choice == 4:
        print('您已退出系统！')
        break
    else:
        print('请输入1-4之间的有效序号')
         
         