# Call
### 这里是 LLSE版 的介绍
![Liscense](https://img.shields.io/github/license/Moxiner/Call)
![Downloads](https://img.shields.io/github/downloads/Moxiner/Call/total)
![Release](https://img.shields.io/github/v/release/Moxiner/Call)
![BDS](https://img.shields.io/badge/support--Pyr--version-1.9.9-red)
![CodeFactor](https://www.codefactor.io/repository/github/Moxiner/Call/badge)  

LLSE版 | [Pyr版](README_PYR.md)

### 【指令介绍】
| 指令内容|	指令描述
----|----|
|/call a|	向所有玩家喊话
|/call p|	向某一个玩家喊话
|/ll reload Call| 重载插件

### 【配置文件】 *\plugins\Call\config.json*

```
@json
{
    "DISPLAYERMONEY": "元", // 货币单位
    "COMMAND": "Call",  // 顶级指令 （次级指令需到源码中修改）
    "DECRIPTION": "全服喊话", // 指令描述
    "ALIAS": "全服喊话", // 顶级指令别名
    "MONEY": "LLMONEY", // 经济系统   LLMONEY经济填写"LLMONEY"    计分板经济填写计分板名称
    "COIN": 50,    // 单次喊话费用
    "ALL_COIN": 300,   // 全服喊话费用
    "MONEY_MODE": 2    // 全服喊话费用计算模式，共两种模式，可填 "1" 或 "2"。
    }
//计算方式说明
// 方法 1    最终价格 = 全服喊话价格
// 方法 2    最终价格 = 全服喊话价格 X 服内人数

// 下个版本将加入：

// [+] 喊话黑名单
// [+] 可选是否扣除管理员经济

// 敬请期待
// 由于json文件不支持注释，此文件仅供参考，请不要直接复制此文件！

```
### 【使用方法】
   * 【step 1】请先安装 [LiteLoadBDS](https://github.com/LiteLDev/LiteLoaderBDS)
 前置加载器
   * 【step 2】将本插件丢进 BDS根目录\plugins\ 文件夹中
   * 【step 3】配置插件 
   * 【step 4】启动服务器，并看到控制台有以下输出（详情请看图 ”Loading“）

### 【说明】
 * 【1】此插件因玩家取消喊话，或喊话不合法将不会扣费（详情请看游戏效果截图）( •̀ ω •́ )y
 * 【2】此插件有两种价格计算方式 ( •̀ ω •́ )y
     * 模式 1 服内无论多少人：最终价格 = 全服喊话价格
     * 模式 2 按服内人数算：最终价格 = 全服喊话价格 X 服内人数 


## 【效果截图】
### 【控制台效果】
![控制台截图](https://www.minebbs.com/attachments/png.24592/)
### 【游戏效果】
![GUI效果](https://www.minebbs.com/attachments/png.24593/)
![游戏效果](https://www.minebbs.com/attachments/gui-png.24594/)

### 【最后】
* 本插件可以整合，但请保证版本更新为最新版
* 本插件原则不可商用，但如果商用整合，请经*Moxiner*授权！
* **感谢柳姐姐的指导，感谢LLSE的开发前辈的指导！之后我更新出更多功能的！ヾ(≧▽≦*)o** 

*Copyright © 2022 MOxiner (or Moxiners). All Rights Reserved.*


