# 翻译细则

## 中英对照翻译稿

稿件开头附上视频链接。然后誊抄视频中文稿，并逐句翻译成英文。

注意：

1. 翻译稿须完整，包含所有对话、插入文字、气泡等等
2. 插入文本使用括号标出
3. 对话的部分，标明每句话的是谁说的，以便校对时建立上下文

可参考 [subtitles/](/subtitles/) 下已有的翻译稿作为范例。

## Pull Request

翻译稿文件名格式为 "日期 (YYYYMMDD)-视频标题"，如“20190801-rou-mo-zheng-dan”[^1]。PR 内需留言引用相应的 issue.

翻译稿应添加至 [subtitles/](/subtitles/) 下对应的子目录内，例如

- 美食作家王刚：[subtitles/wang-gang/](/subtitles/wang-gang/)
- 雪鱼探店：[subtitles/xue-yu/](/subtitles/xue-yu/)

如果以前没做过该频道的字幕，请同时在 subtitles/ 下建立一个新的子目录。

可参考已 merge 的 PR 作为范例

[^1] 由于 GitHub 的 bug，如果文件名有中文，在 PR review 的时候无法在文件内直接看到 line comments。因此文件名使用拼音。

## 对译表

本表为 美食作家王刚 视频中常见词汇及句式的翻译对照表

基本原则：

1. 中餐专有术语一律零翻译，使用拼音+字面意思。如 宽油 译作 Kuan You (literally "broad oil")
2. 菜名零翻译，一律使用拼音+字面意思或拼音+一句话解释。极少数有公认通用译名的例外，如宫保鸡丁 Kung Pao Chicken
3. 食材、调料等，如有常见英文俗名或商品名则使用该英文名，如 花椒 译作 Sichuan peppercorn。确保搜索该英文名能搜到正确的东西。
4. 没有常见英文名的，采用拼音+解释，如 糖色 译作 "Tang Se" Chinese style caramel syrup。食材名称一律不使用学名
5. 尽量精，简。

### 新鲜肉类 / Meat, Poultry, Fish & Seafood

|  中文  |           English            |
| :----: | :--------------------------: |
|  猪肉  |             pork             |
| 五花肉 |          pork belly          |
| 二刀肉 | Erdao Rou (pork leg top cut) |
| 里脊肉 |       pork tenderloin        |
|  牛柳  |       beef tenderloin        |
|  羊肉  |             lamb             |
| 羊腿肉 |           lamb leg           |
| 童子鸡 |        young chicken         |
|  鲤鱼  |             carp             |
|  草鱼  |          grass carp          |
|  花鲢  |         silver carp          |
|  鲈鱼  |             bass             |
| 笋壳鱼 |         marble goby          |

### 新鲜蔬菜 / Fresh Vegetables

|   中文    |       English        |
| :-------: | :------------------: |
|   小葱    | scallion/green onion |
|   大葱    |        Leeks         |
|   香葱    |        chive         |
|   西芹    |        celery        |
|   芹菜    |     leaf celery      |
|  青江菜   |    baby bok choy     |
|   马蹄    |    water chestnut    |
|   香菇    |  shiitake mushroom   |
|   紫菜    |         nori         |
|   海带    |         kelp         |
|   香菜    |      coriander       |
|   蒜苗    |    garlic sprouts    |
| 豇豆/豆角 |        cowpea        |
|  泡豇豆   |    pickled cowpea    |

### 油类 / Oils

|   中文   |                     English                      |
| :------: | :----------------------------------------------: |
| 熟菜籽油 |               cooked rapeseed oil                |
|   红油   | red oil (chilli and spice infused vegetable oil) |

### 腌制&干货 / Preserved Foods

| 中文 |                  English                  |
| :--: | :---------------------------------------: |
| 芽菜 | "Ya Cai" Sichuan preserved mustard greens |
| 泡椒 |               pickled chili               |
| 瑶柱 |           Conpoy/dried scallops           |

### 香料 / Spices

|     中文      |           English           |
| :-----------: | :-------------------------: |
|     生姜      |           ginger            |
|     仔姜      |        young ginger         |
|     良姜      |          galangal           |
|   沙姜/山奈   |         sand ginger         |
|     大蒜      |           garlic            |
|     花椒      |     Sichuan peppercorn      |
|    青花椒     |  Sichuan green peppercorn   |
|     八角      |         star anise          |
|     草果      |           tsao-ko           |
|    小茴香     |         fennel seed         |
|     白蔻      |       white cardamom        |
|     桂皮      |          cinnamon           |
|     香叶      |          bay leaf           |
|     孜然      |         cumin seed          |
|    干辣椒     |     dried chili pepper      |
| 子弹头/朝天椒 | "Chaotianjiao" chili pepper |
|    小米辣     |   "Xiaomila" chili pepper   |
|    二荆条     |  "Erjingtiao" chili pepper  |
|     陈皮      |    (dried) mandarin peel    |

### 调料 / Condiments

|   中文   |                English                 |
| :------: | :------------------------------------: |
|   料酒   |          Chinese cooking wine          |
|   生抽   |            light soy sauce             |
|   老抽   | dark soy sauce/Chinese black soy saucy |
|   香醋   |           Zhenjiang vinegar            |
|   鲜露   |   "Xian Lu" Chinese liquid seasoning   |
|   白酒   |                 baijiu                 |
|   鸡精   |     chicken flavoring/broth powder     |
|   糖色   | "Tang Se" Chinese style caramel syrup  |
|  豆瓣酱  |              doubanjiang               |
| 红油豆瓣 |         chilli oil doubanjiang         |
|   豆豉   |        "Dou Chi" fermented bean        |
|   酒糟   |  "Jiu Zao" rice wine distiller grain   |
|   冰糖   |            white rock sugar            |
|  甜面酱  |   "Tian Mian Jiang" sweet bean paste   |
|   卤水   |              master stock              |

### 术语 / Technical Terms

|      中文      |                   English                   |
| :------------: | :-----------------------------------------: |
|      点缀      |                   garnish                   |
|     凉拌…      |                   …salad                    |
|      辅料      |              minor ingredient               |
|      刀工      |                 knife skill                 |
|      切块      |          dice / cut ... into dice           |
|      切沫      |         shred / cut ... into shreds         |
|      切片      |         slice / cut ... into slices         |
| 顺着纹路（切） |               with the grain                |
| 逆着纹路（切） |              against the grain              |
|      切粒      |         fine dice/ grain-sized dice         |
|      切丝      |                  julienne                   |
|      明油      |   Ming You (literally "brightening oil")    |
|      宽油      |       Kuan You (literally "wide oil")       |
|      底油      |       Di You (literally "bottom oil")       |
|      断生      |        Duan Sheng” (“barely cooked”)        |
|      香味      |                    aroma                    |
|      鲜味      |                 umami taste                 |
|      麻味      |                   numbing                   |
|      爆香      | bring out the taste/stir fry until aromatic |
|      爆炒      |              Fry on high heat               |
|      爆干      |                                             |
|      入味      |              marinade/ infuse               |
|       腌       |                  marinade                   |

### 惯用句式 / Frequent Phrases

|          中文           |                   English                   |
| :---------------------: | :-----------------------------------------: |
|   哈喽大家好我是王刚    |      Hello everyone, this is Wang Gang      |
| 本期视频我跟大家分享... | In this video, I'll share the recipe of ... |
|    首先我们把锅烧热     |           First, heat up the wok            |
| 锅烧热之后加入（某油）  |         Add ... into the heated wok         |
|          备用           |        for later use (or set aside?)        |
|    下一步，开始实践     |             Next, the practice              |
