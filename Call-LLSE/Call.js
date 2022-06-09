// 变量声明

//LiteXLoader Dev Helper
/// <reference path="c:\Users\Moxiner\.vscode\extensions\moxicat.lxldevhelper-0.1.8/Library/JS/Api.js" /> 



let PLUGIN_NAME = "Call";
let PLUGIN_DESCRIPTION = "LLSE 全服喊话 [输入 ll plugins Call 查看具体信息]";     //插件描述
let VERSION = [1, 0, 0];
let AUTHOR = "莫欣儿";
let CONNECT = "QQ Group : 850517473"
let CONFIG = {
    PATH: "./plugins/Call",
    NAME: "Config.json",
    CONCENT:
        `{
    "DISPLAYERMONEY":"元",
    "COMMAND":"Call",
    "DECRIPTION":"全服喊话",
    "ALIAS":"全服喊话",
    "MONEY": "money",    
    "COIN": 50,    
    "ALL_COIN": 300,    
    "MONEY_MODE": 1 
}`
}
let BANNER = {
    PATH: "./plugins/Call",
    NAME: "Banner.json",
    CONCENT:
        `[]`
}
var PlayerList = [] 
// 插件描述
ll.registerPlugin(PLUGIN_NAME, PLUGIN_DESCRIPTION, VERSION,
    {
        "Author": AUTHOR,
        "Connect": CONNECT
    });

// 文件操作
// 文件写入
var FileOppeate = {
    FileWrite: function (path, fileName, concent) {
        try {
            File.mkdir(CONFIG.PATH);
            File.writeTo(`${path}/${fileName}`, concent);
        } catch {
            logger.wram("[code:0]配置文件写入失败");
            logger.wram("[code:0] 请添加QQ群：850517473，以获取帮助");
        }
    },

    // 读取文件
    FileRead: function (path, fileName) {
        try {
            var configForm = File.readFrom(`${path}\\${fileName}`);
            if (configForm) {
                log(`${CONFIG.NAME} 读取成功`);
            } else {
                FileOppeate.FileWrite(CONFIG.PATH, CONFIG.NAME, CONFIG.CONCENT);
            }
        } catch {
            logger.wram("[code:1]配置文件写入失败");
            logger.wram("[code:1] 请添加QQ群：850517473，以获取帮助");
            FileOppeate.FileWrite(CONFIG.PATH, CONFIG.NAME, CONFIG.CONCENT);
        }
        return configForm;
    }
}

// 表单创建
var GUI = {
    //全服喊话表单
    AllGUI: function () {
        var AllGUI = mc.newCustomForm();
        AllGUI.setTitle("全服喊话");
        AllGUI.addLabel(`模式 : 全服喊话    人数 : ${DateDeal.GetPlayerNumber()}    花费 : ${DateDeal.MoneyMode(ConfigForm.MONEY_MODE)} ${ConfigForm.DISPLAYERMONEY}`)
        AllGUI.addLabel("请输入您要喊话的内容");
        AllGUI.addInput("", "请输入内容");
        return AllGUI;
    },
    // 向某人喊话表单
    PersonGUI: function () {
        var PersonGUI = mc.newCustomForm();
        PersonGUI.setTitle("向某人喊话");
        PersonGUI.addLabel(`模式 : 单人喊话    花费 : ${ConfigForm.COIN} ${ConfigForm.DISPLAYERMONEY}`)
        PersonGUI.addDropdown("请选择您要喊话的玩家",  DateDeal.GetPlayerList());
        PersonGUI.addInput("请输入您要喊话的内容", "内容");
        return PersonGUI;
    }
}

// 数据处理
var DateDeal = {
    // 获取全服玩家人数
    GetPlayerList: function () {
        var ObjectList = mc.getOnlinePlayers();
        PlayerList = [] 
        for (i = 0; i < ObjectList.length; i++) {
            PlayerList.push(ObjectList[i].name);
        }
        return PlayerList;
    },
    GetPlayerNumber: function () {
        DateDeal.GetPlayerList();
        let PlayerNumber = mc.getOnlinePlayers().length;
        return PlayerNumber;
    },
    SpendMoney: function (pl, coin) {
        
        if (ConfigForm.MONEY == "LLMONEY") {
            let playermoney = money.get(pl.xuid);
            if (playermoney >= coin) {
                money.reduce(pl.xuid, coin)
                return true
            } else {
                pl.sendText("§l§7[§2Call§7]§e你没有足够的钱！")
                return false
            }
        } else {
            let playermoney = pl.getScore(ConfigForm.MONEY)
            if (playermoney >= coin) {
                pl.reduceScore(ConfigForm.MONEY, coin)
                return true
            } else {
                pl.sendText("§l§7[§2Call§7]§e你没有足够的钱！")
                return false
            }
        }

    },
    // 判断是否为管理员，是则返回真，否则扣费处理，并返回结果
    JudgeID: function (pl, coin) {
        if (pl.isOP()) {
            pl.sendText("§l§7[§2Call§7]§e检测到您是管理员身份，本次喊话免费！")
            return true;
        } else {
            if (DateDeal.SpendMoney(pl, coin)) {
                return true
            } else {
            return false
        }
    }},
    // 计算ALL_COIN，并返回数值
    MoneyMode: function (mode) {
        if (mode == 1) {
            return ConfigForm.ALL_COIN
        } else if (mode == 2) {
            return ConfigForm.ALL_COIN * DateDeal.GetPlayerNumber()
        } else {
            logger.wram("[code:1]配置文件错误");
            logger.wram("[code:1]但插件仍能使用，默认以 模式1 载入");
            logger.wram("[code:1]MoneyMode 项只允许写入 数字 1 或数字 2");
            logger.wram("[code:1] MoneyMode 请重新配置并重载插件");
            return ConfigForm.ALL_COIN
        }
    },
    Banner: function(pl) {
        // 加载黑名单
        try {
            BannerForm = JSON.parse(FileOppeate.FileRead(BANNER.PATH, BANNER.NAME));
            } catch {
                FileOppeate.FileWrite(BANNER.PATH, BANNER.NAME, BANNER.CONCENT);
                BannerForm = JSON.parse(FileOppeate.FileRead(BANNER.PATH, BANNER.NAME));    
        }
        if (BannerForm.indexOf(pl.name) != -1 ) {
            return false;
        }
        else {
            return true;
        }
    }
}
// 命令处理
var Command = {
    // 全服喊话处理
    Call: function (msg, sender, accpect = "@a") {
        mc.runcmdEx(`title ${accpect} title ${msg}`);
        mc.runcmdEx(`title ${accpect} subtitle §b来自 §e${sender}§b 的喊话`)
    }
}

// 监听函数
var onListener = {
    onCmd: function () {
        let cmd = mc.newCommand("call", "全服喊话", PermType.Any, 0x80);
    cmd.setAlias("全服喊话");
    cmd.setEnum("mode", ["a", "p"]);
    cmd.mandatory("action", ParamType.Enum, "mode", 1);
    cmd.overload(["mode"]);
    cmd.setCallback((_cmd, pl, _out, res) => {
        
        switch (res.action) {
            case "a":
                if (DateDeal.Banner(pl)) {
                    pl.player.sendForm(GUI.AllGUI(), onListener.onSelect);
                } else {
                    pl.player.sendText("§l§7[§2Call§7]§c您已被列入黑名单，无法进行全服喊话！")

                }
                break;
            case "p":
                if (DateDeal.Banner(pl)) {
                    pl.player.sendForm(GUI.PersonGUI() , onListener.onSelect );
            } else {
                pl.player.sendText("§l§7[§2Call§7]§c您已被列入黑名单，无法进行全服喊话！")
            }
            break;
        }        
    });
    cmd.setup();
        },

    onSelect: function (pl, form) {
        try {
            if (form instanceof Array) {
                
                if (form[2] == "") {
                    // 文字为空处理
                    pl.sendText("§l§7[§2Call§7]§6文字不能为空")
                } else if (form[1] == null) {
                    // 全服喊话
                    if (DateDeal.JudgeID(pl, DateDeal.MoneyMode(ConfigForm.MONEY_MODE))) {
                        Command.Call(form[2], pl.name)
                        pl.sendText("§l§7[§2Call§7]§b喊话成功");
                    }
                } else if (typeof(form[1]) == "number") {
                    // 单人喊话
                    var accpect = PlayerList[1];
                    if (DateDeal.JudgeID(pl, ConfigForm.COIN)) {
                        Command.Call(form[2], pl.name, accpect)
                        pl.sendText("§l§7[§2Call§7]§b喊话成功");
                    } 
                } 
            } else if (form == null) {
                // 喊话取消处理
                pl.sendText("§l§7[§2Call§7]§c喊话已取消");
            }
        } catch {
            // 捕获 onSelect 错误
            logger.warn("[code:2]喊话执行失败")
            logger.warn("[code:2]但插件仍可使用")
            logger.warn("[code:2]请联系作者维护(QQ群:1167270197")
        }
    }
}
// 加载配置文件
try {
ConfigForm = JSON.parse(FileOppeate.FileRead(CONFIG.PATH, CONFIG.NAME));
} catch {
    FileOppeate.FileWrite(CONFIG.PATH, CONFIG.NAME, CONFIG.CONCENT);
    ConfigForm = JSON.parse(FileOppeate.FileRead(CONFIG.PATH, CONFIG.NAME));
}

mc.listen("onServerStarted", onListener.onCmd);
logger.info("加载完成 v1.0.1");
logger.info(`作者 ${AUTHOR}`);