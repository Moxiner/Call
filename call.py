# Copyright © 2022 MOxiner (or Moxiners). All Rights Reserved.
# 萌新切勿修改 
"""
下个版本将加入：

[+] 喊话黑名单
[+] LL经济
[+] 可选是否扣除管理员经济

敬请期待
"""
# ========================================= 代码界面 =========================================
# 模块声明
import os
import mc
import json
import time

# 初始变量
formid = 0
reportedNameList = []
reporterNameList = []
banNameList = []
PlugName = "Call"
ConfigPath = "plugins/py/" + PlugName
j = {              
    "money":"money",         
    "coin":50,               
    "all_coin":100 ,
    "money_made":1
    } 

# 控制台输出类
class PrintLog:
    '''打印类'''
    def GetTime():
        '''获取当前时间'''
        return time.strftime("%H:%M:%S")

    def InfoLog(concent:str):
        '''弹出 Info 通知
        concent:打印内容
        '''
        print(f"[{PrintLog.GetTime()} Info][{PlugName}] {concent}")

    def WarmLog(concent:str):
        '''弹出 Warm 通知'''
        print(f"\033[33m[{PrintLog.GetTime()} Warm][{PlugName}] {concent}\033[0m")

    def ErrorLog(concent:str):
        '''弹出 Errror 通知'''
        print(f"\033[31m[{PrintLog.GetTime()} Error][{PlugName}] {concent}\033[0m")

    def TestLog(concent:str):
        '''弹出 Test 通知'''
        print(f"\033[36m[{PrintLog.GetTime()} Test][{PlugName}] {concent}\033[0m")

# 文件类
class Film:
    '''文件类'''
    def CreateFilm(path:str,name:str):
        '''
        检测文件存在，不存在则创建此文件
        path:文件路径
        name: 文件名称
        '''
        if os.path.exists(f"{path}/{name}"):    
            try:    
                Film.ReadFilm(path, name)     # 顺便读取 Config.json 数据
            except:
                PrintLog.ErrorLog("[code:1] 配置文件发生错误")
                time.sleep(5)
                exit()
        else:
            if not os.path.exists(path):
                os.makedirs(f"{path}")
            with open(f"{path}/{name}","w+"):
                Film.WriteFilm(path , name, j)    # 顺便写入 Config.json 数据
                try:
                    Film.ReadFilm(path, name)     # 顺便读取 Config.json 数据
                except:
                    time.sleep(5)
                    PrintLog.ErrorLog("[code:1] 配置文件发生错误")
                    exit()        
    def WriteFilm(path:str , name:str, concent:dict ):
        '''
        写入 json 文件
        path:文件路径
        name:文件名称
        json:写入内容
        '''
        with open(f"{path}/{name}" , "w") as config:
            json.dump(concent, config, indent=4)
            config.close()
            PrintLog.InfoLog("文件创建完成")

    # 加载配置文件参数
    def ReadFilm(path:str, name:str):
        '''
        读取 json 文件
        path:文件路径
        name:文件名称
        '''
        with open(f"{path}/{name}","r") as f:
            Config = json.load(f)
            global Money
            global Coin
            global All_coin
            global Money_Mode       
            Money = Config["money"]         
            Coin = Config["coin"]            
            All_coin = Config["all_coin"]
            Money_Mode = Config["money_made"]
    

# GUI类
class GUI:
# 全服喊话GUI
    def AllGUI(e):
        '''
        向 e 发送 全体喊话 的 GUI
        e:MC玩家指针
        return:表单ID
        '''
        player = e
        DateDeal.GetPlayerList()      
        return player.sendCustomForm('{"content":[{"type":"label","text":"请输入要喊话的内容  服内人数  ' + str(PlayerNumber) + '  将花费  ' + str(DateDeal.MoneyMode(Money_Mode)) + ' 管理员免费"},{"placeholder":"请输入喊话的内容","default":"","type":"input","text":""}], "type":"custom_form","title":"全服喊话"}', onListener.onSelect)

    def PersonGUI(e):
        '''
        向 e 发送 向某一个人喊话 的 GUI
        e:MC玩家指针
        return:表单ID
        '''
        DateDeal.GetPlayerList()      
        player = e
        return player.sendCustomForm('{"content":[{"default":0,"options":'+ json.dumps(PlayerList_Str) +',"type":"dropdown","text":"请选择要喊话的玩家    将花费  ' + str(Coin) + '    管理员免费"},{"placeholder":"在这里填写","default":"","type":"input","text":"请输入喊话内容"}],"type":"custom_form","title":"全服喊话"}', onListener.onSelect)


class Command:
# 喊话指令
    def Call(msg, sender , accpect="@a"):
        '''
        向游戏中发送 Call 指令
        msg:发送消息
        sender:发送者实体类
        accpect:接收者ID
        '''
        sender = sender.getName()
        mc.runCommand("title " + accpect + " title " + msg )
        mc.runCommand("title " + accpect + " subtitle §b来自 §e" + sender + "§b 的喊话" )

# 数据处理
class DateDeal:
    def GetPlayerList(): 
        '''
        获取玩家列表
        return:玩家列表
        '''
        global PlayerList_Str
        global PlayerNumber
        PlayerList_Str = []
        PlayerNumber = 0
        playerList_List = mc.getPlayerList()
        for player in playerList_List:
                PlayerList_Str.append(player.getName())
                PlayerNumber = PlayerNumber + 1
    
    def MoneyMode(mode:int):
        '''
        费用计算方式
        mode:计算模式
        '''
        if mode == 1:
            return All_coin
        if mode == 2:
            return All_coin * PlayerNumber
        else:
            PrintLog.WarmLog("[code:1] 配置文件错误")        
            PrintLog.WarmLog("[code:1] 但插件仍能使用，默认以 模式1 载入 ")        
            PrintLog.WarmLog("[code:1] MoneyMode 项只允许写入 数字 1 或数字 2")        
            PrintLog.WarmLog("[code:1] MoneyMode 请重新配置并重启服务器")       
            return All_coin
             
   
    def SpendMoney(e ,coin:int):
        '''
        处理扣费问题
        e:MC玩家类
        coin:花费 money 数量
        '''
        if Money == "LLMONEY" :
            pass
        elif Money != "LLMONEY":
            playermoney = e.getScore(Money)
            if playermoney << coin :
                e.reduceScore(Money, coin)
                return True
            else :
                e.sendText("§l§7[§2Call§7]§e你没有足够的钱！") 
                return False 
                    
    def JudgeID(e , coin ):
        '''
        判断玩家是否可执行
        e:MC实体类
        return:是否执行
        '''
        PlayerPerm = e.getPermissions()
        if PlayerPerm != 1 :
            return True
        elif PlayerPerm == 1 :
            if DateDeal.SpendMoney(e , coin):
                return True 
            else:
                return False
        else:
            return False
class onListener:
    def reload(e,cmd):
        '''
        重载配置文件
        e:MC实体类
        cmd:指令内容
        '''
        try:
            if e.getPermissions() == 2:
                Film.ReadFilm(ConfigPath,"config.json")
                e.sendText("§l§7[§2Call§7]§b插件重载完成")
                PrintLog.TestLog("插件重载完成！")

            else:
                e.sendText("§l§7[§2Call§7]§c你没有足够的权限！")
        except:
            PrintLog.WarmLog("[code:1] 配置文件发生错误")
            PrintLog.WarmLog("[code:1] 插件重载失败")
            


    def onCmd(e , cmd):
        '''
        触发指令
        e:MC实体类
        cmd:指令内容
        '''
        if cmd == 'calla':
            GUI.AllGUI(e)
            return False
        elif cmd == "callp":
            GUI.PersonGUI(e)
            return False

    def onSelect(e , form):
        '''
        接收表单内容，判断是否执行
        e:MC实体类
        form:接收表单信息
        '''
        form = json.loads(form)
        # 提交空文本
        try:
            if form[1] == "":
                    e.sendText("§l§7[§2Call§7]§6文字不能为空")
            # 全服喊话
            elif form[0] == None:
                if DateDeal.JudgeID(e , DateDeal.MoneyMode(Money_Mode)):
                    Command.Call(form[1] , e)
                    e.sendText("§l§7[§2Call§7]§b喊话成功")
            # 单人喊话
            else:
                accpect =  PlayerList_Str[form[0]]
                if DateDeal.JudgeID(e , Coin):
                    Command.Call(form[1] ,e ,accpect)
                    e.sendText("§l§7[§2Call§7]§b喊话成功")
        except TypeError:
            e.sendText("§l§7[§2Call§7]§c请求不合法")
        except:
            PrintLog.WarmLog("[code:2] 喊话执行失败")
            PrintLog.WarmLog("[code:2] 但插件仍可使用")
            PrintLog.WarmLog("[code:2] 请联系作者维护(QQ群:1167270197")

Film.CreateFilm(ConfigPath,"config.json")
# 一大堆监听器和注册指令
mc.registerCommand('calla',onListener.onCmd,'全服喊话')
mc.registerCommand('callp',onListener.onCmd,'向某人喊话')
mc.registerCommand("callreload", onListener.reload,'重载插件')
PrintLog.InfoLog("加载完成 v1.1")
PrintLog.InfoLog("作者 一只莫欣儿（Moxiner）")