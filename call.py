# Copyright © 2022 MOxiner (or Moxiners). All Rights Reserved.
# 萌新切勿修改 
"""
下个版本将加入：

[+] 喊话黑名单
[+] LL经济
[+] 全服喊话单价与个人喊话单价不同
[+] 可选是否扣除管理员经济

敬请期待
"""
# ========================================= 代码界面 =========================================
# 模块声明
from cmd import Cmd
import os
import mc
import json
import time

# 初始变量
formid = 0
reportedNameList = []
reporterNameList = []
banNameList = []
ConfigPath = "plugins/py/Call/"

# 获取当前时间 
def GetTime():
    return time.strftime("%H:%M:%S")

# 规范化输出
def PrintLog(content: str):
    mc.logout(f"[{GetTime()} Info][Call]{content} \n")

# 初始化配置文件
def InitializationFilm():
    configconcent = {
       "TIME":240,              
        "MONEY":"money",         
        "PRICE":100,               
        "ALL_PRICE":300,
    }
    if os.path.exists(ConfigPath):
        pass
        PrintLog("文件已存在")
    else :
        os.makedirs(f"{ConfigPath}")
        with open(f"{ConfigPath}/config.json" , "w") as config:
            json.dump(configconcent, config,indent=4)
            config.close()
        PrintLog("文件创建完成")

# 加载配置文件参数
def InitializationConfig():
    global TIME
    global MONEY
    global PRICE
    global ALL_PRICE
    ConfigFilm = open(f"{ConfigPath}/config.json",)
    Config = json.load(ConfigFilm)
    TIME = Config["TIME"]       
    MONEY = Config["MONEY"]         
    PRICE = Config["PRICE"]            
    ALL_PRICE = Config["ALL_PRICE"]

# 喊话指令
def Call(msg, sender , accpect="@a"):
    mc.runcmd("title " + accpect + " title " + msg )
    mc.runcmd("title " + accpect + " subtitle §b来自§e" + sender + "§b的喊话" )

# 判断是否为管理员身份
def JudgeID(e):
    global PlayerPerm
    PlayerPerm = e["player"].perm
    if PlayerPerm != 0 :
        return True
    if PlayerPerm == 0 :
        i = SpendMoney(e)
        return i
            
# 全服喊话GUI
def AllGUI(e):
    global formid
    sender = e["player"]
    formid = sender.sendCustomForm('{"content":[{"type":"label","text":"请输入要喊话的内容"},{"placeholder":"请输入喊话的内容","default":"","type":"input","text":""}], "type":"custom_form","title":"全服喊话"}')

# 获得全服玩家名单
def GetPlayerList() :
    global playerNameList
    global playerList
    playerList = []
    playerNameList = []
    playerList = mc.getPlayerList()
    for player in playerList:
            playerNameList.append(player.name)

# 扣费处理
def SpendMoney(e):
    player = e["player"]
    if MONEY == "LLMONEY" :
        pass
    elif MONEY != "LLMONEY":
        playermoney = player.getScore(MONEY)
        if playermoney << PRICE :
            player.modifyScore(MONEY , -PRICE , 1)
            return True
        else :
            player.sendTextPacket("§l§7[§2Call§7]§e你没有足够的钱！") 
            return False 

# 请求不合法时，退还费用            
def BackMoney(e) :
    player = e["player"]
    if MONEY == "LLMONEY" :
        pass
    elif MONEY != "LLMONEY":
        player.modifyScore(MONEY , PRICE , 1)

# 检测指令
def onCmd(e):
    global mode
    if e['cmd'] == '/call a':
        if JudgeID(e) :
            AllGUI(e)
            return False
    elif e["cmd"] == "/call p":
        if JudgeID(e) :
            PersonGUI(e)
            return False
    else:
        pass

# 向某人喊话GUI      
def PersonGUI(e):
    global formid
    GetPlayerList()
    player = e["player"]
    formid = player.sendCustomForm('{"content":[{"default":0,"options":'+json.dumps(playerNameList)+',"type":"dropdown","text":"请选择要喊话的玩家"},{"placeholder":"在这里填写","default":"","type":"input","text":"请输入喊话内容"}],"type":"custom_form","title":"全服喊话"}')
  
# 表单数据处理
def onSelect (e):
    global Accpect
    global Msg
    global Sender
    if not formid == e["formid"] :
        return False  
    Select = e["selected"]
    Sender = e["player"].name
    SelectList = json.loads(Select)
    try :
        if SelectList[0] == None :
            Accpect = "@a"
        else : 
            Accpect = playerNameList[SelectList[0]]
        Msg = SelectList[1]
        if Msg == "" :
            e["player"].sendTextPacket("§l§7[§2Call§7]§6文字为空或§c请求不合法")
            BackMoney(e)
        else :
            e["player"].sendTextPacket("§l§7[§2Call§7]§b喊话成功")
            Call(Msg ,Sender ,Accpect)
    except :
        if PlayerPerm != 0 :
            e["player"].sendTextPacket("§l§7[§2Call§7]§c请求不合法")
        else :
            e["player"].sendTextPacket("§l§7[§2Call§7]§c请求不合法")
            BackMoney(e)

# 一大堆监听器和注册指令
InitializationFilm()
InitializationConfig()
mc.setListener('onInputCommand',onCmd)
mc.setListener('onSelectForm',onSelect)
mc.setCommandDescription('call a','全服喊话')
mc.setCommandDescription('call p','向某人喊话')
PrintLog("加载完成 v2.0")
PrintLog("作者 一只莫欣儿（Moxiner）")