![艺术](https://img-blog.csdnimg.cn/507ee2ff794946b1851b54f1ba86cadb.png)

# 0. 环境
1. OS: `Ubuntu20.04`
2. pipenv: `2023.7.4`
3. Flask: `2.0.1`
4. nodejs: `v18.16.1` ： **基于 Chrome V8 引擎的JS运行环境**
5. npm: `6.14.4` ： **node.js 的包管理工具**
6. Vue:`@vue/cli 5.0.8`
7. element-plus: `2.3.7`
8. bootstrap: `4.6.1`
9. pinia: `2.1.3`
>1. npm国内换源：
>`sudo npm config set registry https://registry.npm.taobao.org`
>2. 为了升级node全局安装n版本管理工具n：`sudo npm install n -g`
>(1)`su root`
>(2)`export N_NODE_MIRROR=https://npm.taobao.org/mirrors/node`
>(3) `n stable`
>3. 安装Vue：`sudo npm install -g vue`
> 安装Vue脚手架`sudo npm install -g @vue/cli`
# 1. 项目结构初始化
## 🐵backend
后端工作：python环境，使用虚拟环境
```shell
~/Desktop/flask-vue-tutorial/backend
$ pipenv shell
$ nano requirements.txt
$ pipenv install -r requirements.txt
$ nano main.py
$ python main.py
```
![依赖](https://img-blog.csdnimg.cn/d548da062f07499aaa0c7f552fda36ea.png)
![hello](https://img-blog.csdnimg.cn/feba90f5005a43ac8a7bdf5955a66a5b.png)
按照惯例，Hello一下🖐️
![hello](https://img-blog.csdnimg.cn/02b9a77c972f430aac8f8d16b91d0719.png)
## 💰frontend
```shell
~/Desktop/flask-vue-tutorial/frontend
$ npm init vue@latest
$ cd gameList/
$ npm install
$ npm run format
$ npm run dev
```
- 修改vite.config.js
![配置](https://img-blog.csdnimg.cn/3cf5d04073f7480eaf67612e11cad920.png)
还可设置`port:8086`，设置`open: true`让服务启动时自动打开浏览器
- Hello一下🖐️
![Hello](https://img-blog.csdnimg.cn/08838b7298ce45ef83f44b2f084a7c0d.png)
# 2. axios配置
`npm i axios`
## 配置路由
![路由](https://img-blog.csdnimg.cn/d7b4b27bc41147ef960d83642176c8d5.png)
## 在前端通过axios请求后台服务
![shark](https://img-blog.csdnimg.cn/d9f9b658d14446779d04a5eaf62bca87.png)
## 后台响应
![shark](https://img-blog.csdnimg.cn/691bc2c294654dbea794552c49014403.png)
## 前台回显结果，合作愉快🤝
![ping](https://img-blog.csdnimg.cn/511bf95c0d9b44bc91836a4fa410c757.png)
# 3. 🍃页面设计
## 引入Element Plus!
- 安装：
`npm install element-plus --save`
- 配置按需导入：
`npm install -D unplugin-vue-components unplugin-auto-import`
- vite.config.js中配置：	![plugin](https://img-blog.csdnimg.cn/dd38e713d99d4bcd9f48189d4dd5da40.png)
- 注释原来的样式文件main.css
![注释](https://img-blog.csdnimg.cn/f7f269bbb4c94bcdb3adc0ce1c96e734.png)
## ✌单页面设计
`frontend/gameList/src/components/Games.vue`
```js
<script setup>
import {ref} from 'vue';
import axios from 'axios';
const tableData = ref()
const path = 'http://192.168.133.130:5000/games'
axios.get(path).then((res)=>{
    tableData.value = res.data.games;
})
</script>
<template>
    <div>
        <el-container>
            <el-header>
                <el-row justify="center">
                    <el-text tag="b" type="primary" size="large">Games Library🕹️</el-text>
                </el-row>
                <el-divider/>
            </el-header>
            <el-main>
                <!-- Alert Message -->
                <el-row justify="center">
                    <el-button plain type="success" @click="addGame">Add Game</el-button>
                </el-row>
                <el-table :data="tableData" stripe>
                    <el-table-column prop="title" label="Title" min-width="80" align="center"/>
                    <el-table-column prop="genre" label="Genre" min-width="80" align="center"/>
                    <el-table-column prop="played" label="Played?" min-width="80" align="center"/>
                    <el-table-column fixed="right" label="Actions" min-width="150" align="center">
                        <template #default>
                            <el-button round type="primary" size="small" @click="updateGame"
                            >update</el-button
                            >
                            <el-button round type="danger" size="small" @click="deleteGame">delete</el-button>
                        </template>
                    </el-table-column>
                </el-table>
            </el-main>
            <el-footer>
                <el-row justify="center">
                    <el-text type="info">Over</el-text>
                </el-row>
            </el-footer>
        </el-container>
    </div>
</template>
```
## 后台响应💡
 `backend/main.py`
![hbtl](https://img-blog.csdnimg.cn/075d3babca0c4eaababb4a596977a80b.png)
## UI效果：
![UI效果](https://img-blog.csdnimg.cn/d8e6fcf270ab4c55b6202d944a85fd5e.png)
## 尝试用用bootstrap!
`npm install bootstrap@4.6.1 --save`
![zgjw](https://img-blog.csdnimg.cn/48dfe75b69714e26ab2175cb8b367605.png)
### 引入bootswatch CDN
[bootswatch CDN](https://www.bootstrapcdn.com/bootswatch/)
`选择`：[Sketchy](https://bootswatch.com/sketchy/)
![sketchy](https://img-blog.csdnimg.cn/05676335298c45eca8fedf280d048e80.png)

### 思考🤔：
1. bootstrap和elementplus搭配是否可行？ 
2. element-plus的表格如何自定义样式？
3. 怎么加背景图，怎么让表格透明显示？ 
### 背景图：
![背景](https://img-blog.csdnimg.cn/f7d4f0eb2ef1416ba7def424148a4796.jpeg)
### 对样式进行魔改⌨️
```js
<script setup>
import {ref} from 'vue';
import axios from 'axios';
const tableData = ref()
const path = 'http://192.168.133.130:5000/games'
axios.get(path).then((res)=>{
    tableData.value = res.data.games;
})
</script>
<template>
    <div id="building">
    <br/>
    <div class="jumbotron vertical-center" id="content">
        <el-container>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/sketchy/bootstrap.min.css" integrity="sha384-RxqHG2ilm4r6aFRpGmBbGTjsqwfqHOKy1ArsMhHusnRO47jcGqpIQqlQK/kmGy9R" crossorigin="anonymous">
            <el-header>
                <!-- bootswatch CDN -->
                <el-row class="nav">
                    <h2 class="logo">To Play🕹️</h2>
                    <button class="btnAdd-popup" @click="addGame">Add</button>
                    <el-divider/>
                </el-row>
            </el-header>
            <el-main>
                <!-- Alert Message -->
                <hr><br>
                <el-table 
                    :data="tableData"  
                    style="max-width:800px;margin:0 auto"
                    >
                    <el-table-column prop="title" label="Title" min-width="80" align="center"/>
                    <el-table-column prop="genre" label="Genre" min-width="80" align="center"/>
                    <el-table-column prop="played" label="Played?" min-width="80" align="center"/>
                    <el-table-column label="Actions" min-width="150" align="center">
                        <template #default>
                            <el-button round type="primary" size="small" @click="updateGame"
                            >update</el-button
                            >
                            <el-button round type="danger" size="small" @click="deleteGame">delete</el-button>
                        </template>
                    </el-table-column>
                </el-table>
            </el-main>
            <el-footer>
                <hr><br>
                <el-row justify="center">
                    <el-text tag="ins" class="footer">Copyright &copy; . All Rights Reserved 2023.</el-text>
                </el-row>
            </el-footer>
        </el-container>
    </div>
    </div>
</template>
<style scoped>
#building{
    background:linear-gradient(rgba(233, 226, 226, 0.251), rgba(228, 223, 223, 0.551)), url('../assets/wallhaven1.jpg') no-repeat ;
    width:100%;		
    height:100%;		
    position:fixed;
    background-size:100% 100%;
}
#content{
    margin-left:20px;
    margin-right:20px;
}
.nav{
    justify-content: space-between;
    align-items: center;
    z-index: 99;
}
.logo{
    font-size: 2em;
    font-weight: bolder;
    color : #fff;
    user-select: none;
    margin-left:45%;
}
.nav .btnAdd-popup{
    width: 130px;
    height: 50px;
    background: transparent;
    border: 2px solid #fff;
    outline: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1.1em;
    color: #fff;
    font-weight: 500;
    margin-right:40px;
    transition: .5s;
}
.nav .btnAdd-popup:hover{
    background: #fff;
    color: #162938;
}
.footer{
    font-size:1.1em;
    font-weight: bolder;
    color:antiquewhite;
}
:deep(.el-table){
    border: 1px solid black;
    background-color: transparent;
}
:deep(.el-table th){
    background-color: rgba(223, 168, 168, 0.5);
}
:deep(.el-table tr){
    background-color: transparent;
}
:deep(.el-table td){
    background-color: rgba(255,255,255,0.5);
}
:deep(.el-table th .cell){
    color:#fff;
    font-weight: bold;
    font-size:large;
}
:deep(.el-table td .cell){
    color:green;
    font-weight: bold;
    font-size:large;
}
</style>
```
## 🤟最终UI效果：
![toplay](https://img-blog.csdnimg.cn/38d73538d0834a9e868442613f111ef2.png#pic_center =600x300)
# 4. 🕹️按钮点击事件
## 后台API
```py
@app.route('/games', methods=['GET', 'POST'])
def allGames():
	response_object = {'status': 'success'}
	if request.method == 'POST':
		post_data = request.get_json()
		GAMES.append({
      			'id': uuid.uuid4().hex,
			'title': post_data.get('title'),
			'genre': post_data.get('genre'),
			'played': post_data.get('played')
		})
		response_object['message'] = 'Game Added!'
	else:
		response_object['games'] = GAMES
	return jsonify(response_object)

@app.route('/games/<game_id>', methods=['PUT','DELETE'])
def single_game(game_id):
  response_object = {'status': 'success'}
  if request.method == 'PUT':
    post_data = request.get_json()
    remove_game(game_id)
    GAMES.append({
      'id': uuid.uuid4().hex,
      'title': post_data.get('title'),
      'genre': post_data.get('genre'),
      'played': post_data.get('played')
	})
    response_object['message'] = 'Game updated!'
  if request.method == "DELETE":
    remove_game(game_id)
    response_object['message'] = 'Game removed!'
  return jsonify(response_object)

def remove_game(game_id):
  for game in GAMES:
    if game['id'] == game_id:
      GAMES.remove(game)
      return True
  return False
```
## 增➕
1. `dialog`变量控制弹窗显示, `form`变量绑定表单数据
![d;yi](https://img-blog.csdnimg.cn/4156a9ceee3842edb1babe8978c62a18.png)
2. `click`触发弹窗
![click](https://img-blog.csdnimg.cn/76351415fbd449fa9efc21f70342544d.png)
3. `dialog`的具体样式
![dvhw](https://img-blog.csdnimg.cn/581260cff46e40ddb707cf0166410195.png)
![样式](https://img-blog.csdnimg.cn/f826a60b52854759b6d123f3edfa3ff7.png)

4. 点击<kbd>submit</kbd>后，打包数据，传给API
![submit](https://img-blog.csdnimg.cn/b3a92227c0f2460c90b424e4dbf30177.png)
5. 前台API的实现, 发送请求，刷新数据，消息提示
![在这里插入图片描述](https://img-blog.csdnimg.cn/c6f82f6e96b34da8b2b4ed15ce9e2b5f.png)
![效果](https://img-blog.csdnimg.cn/c26c61f241914e5abf603482769c1050.png)
## 删❌
1. 思考：点击删除按钮，需要传递当前行的id，怎么传递？
 答： 通过**作用域插槽**
 ![作用域插槽](https://img-blog.csdnimg.cn/5ef45cea5ad64c918dc7cb4469813f2a.png)
 2. 与后台通信，然后更新列表，回显消息
![处理](https://img-blog.csdnimg.cn/5d262187e42b4f9e9cf959293761b0bb.png)
## 改✂️
1. `dialog`变量控制弹窗显示, `form`变量绑定表单数据
![bmld](https://img-blog.csdnimg.cn/5acd0e84b772415787910ea7496c2db3.png)
2. `click`触发弹窗, 使用作用域插槽传递当前行信息
![插槽](https://img-blog.csdnimg.cn/43a081b45db24c21a10a55b12cf162f6.png)
![传参](https://img-blog.csdnimg.cn/a2cffd37089c45448ee980761a8642e0.png)
3. `dialog`的具体样式
![对话](https://img-blog.csdnimg.cn/40b0df6e7ee24ce18b8f50381e529577.png)
4. 点击<kbd>submit</kbd>后，打包数据，传给API
![打包](https://img-blog.csdnimg.cn/e77f40a8e5c94caa9751cbceb697625d.png)
5. API的实现, 发送请求，刷新数据，消息提示
![uixm](https://img-blog.csdnimg.cn/e123af5b44214ad08cd67f598a0a90a6.png)

# 5. [预览网址](https://sparkling-frangollo-b5c2ea.netlify.app/)📖
部署在Netlify上
为了简单，去掉了flask后端，使用pinia来进行状态管理
可以查看源码的front分支

> 什么是Netlify?
> 一个现代网站自动化系统，只要在本机Git中编写前端代码，然后推送它，网站就能完美地对外呈现，类似网站托管工具

![部署](https://img-blog.csdnimg.cn/35d08009b20547a7b378e1c66dc908e2.png)










