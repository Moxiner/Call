# Call
### 这里是 Pyr版 的介绍
![Liscense](https://img.shields.io/github/license/Moxiner/Call)
![Downloads](https://img.shields.io/github/downloads/Moxiner/Call/total)
![Release](https://img.shields.io/github/v/release/Moxiner/Call)
![BDS](https://img.shields.io/badge/support--Pyr--version-1.9.9-red)
![CodeFactor](https://www.codefactor.io/repository/github/Moxiner/Call/badge)  

Pyr版 | [LLSE版](README.md)

**Pyr版接入经济插件的全服喊话** 
**目前仅接入计分板经济，后续版本会接入*LL经济***

### 【指令介绍】
| 指令内容|	指令描述
----|----|
|/calla|	向所有玩家喊话
|/callp|	向某一个玩家喊话
|/callreload| 重载插件
【注意】BDSPyr不支持含有空格的指令，我也没有办法！o(*￣▽￣*)ブ
### 【配置文件】 *\plugins\py\Call\config.json*

```
@json
{
    "money": "money",    // 计分板经济
    "coin": 50,    // 向某人喊话价格
    "all_coin": 300,    // 向全服喊话价格
    "money_made": 1  // 计算方式 可以填入1 或 2
}

//计算方式说明
// 方法 1    最终价格 = 全服喊话价格
// 方法 2    最终价格 = 全服喊话价格 X 服内人数


// 下个版本将加入：

// [+] 喊话黑名单
// [+] LL经济
// [+] 可选是否扣除管理员经济

// 敬请期待
// 由于 Pyr 中的 Json 文件不允许有注释
// 请不要直接复制本描述代码
// 配置文件会在第一次启动时生成

```
### 【使用方法】
   * 【step 1】请先安装 [BDSPyruner](https://github.com/WillowSauceR/BDSpyrunner/)
 前置加载器
   * 【step 2】将本插件丢进 BDS根目录\plugins\py 文件夹中
   * 【step 3】配置插件 
   * 【step 4】启动服务器，并看到控制台有以下输出（详情请看图 ”Loading“）

### 【说明】
 * 【1】此插件仅支持计分板经济（LL经济后续适配）
 * 【2】此插件因玩家取消喊话，或喊话不合法将不会扣费（详情请看游戏效果截图）( •̀ ω •́ )y
 * 【3】此插件会在后台输出一些不必要的信息，目前我还无力差别屏蔽（详情见图”command“）( •̀ ω •́ )y
 * 【4】此插件有两种价格计算方式
     * 模式 1 服内无论多少人：最终价格 = 全服喊话价格
     * 模式 2 按服内人数算：最终价格 = 全服喊话价格 X 服内人数 


## 【效果截图】
### 【控制台效果】
![控制台截图](https://www.minebbs.com/attachments/gui-png.24594/)
### 【游戏效果】
![GUI效果](https://www.minebbs.com/attachments/png.24593/)
![游戏效果](https://www.minebbs.com/attachments/gui-png.24594/)

### 【最后】
* 本插件可以整合，但请保证版本更新为最新版
* 本插件原则不可商用，但如果商用整合，请经*Moxiner*授权！
* **感谢柳姐姐的指导，感谢Pyr的开发前辈的指导！之后我更新出更多功能的！ヾ(≧▽≦*)o** 

*Copyright © 2022 MOxiner (or Moxiners). All Rights Reserved.*


