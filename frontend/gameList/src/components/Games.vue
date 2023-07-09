<script setup>
import {onMounted, ref} from 'vue';
import axios from 'axios';
import { defineStore } from 'pinia'
const useGameStore = defineStore('games', ()=>{
  //定义管理游戏数据的state
  const gameList = ref([
  {
    'title': 'War',
    'genre': 'Tom',
    'played': 'false',
  },
  {
    'title': '4399',
    'genre': 'Tom',
    'played': 'false',
  },
  ])
  //定义action函数
  const addGame = (game)=>{
    gameList.value.push(game);
  }
  const deleteGame = (game) => {
    //找到下标值
    const itemIndex = gameList.value.findIndex((item)=>item['title']===game['title']);
    //数组过滤来删除元素
    gameList.value.splice(itemIndex,1);
  }
  const updateGame = (game) => {
    //找到下标值
    const itemIndex = gameList.value.findIndex((item)=>item['title']===game['title']);
    // console.log(gameList.value[itemIndex]['title']);
    gameList.value[itemIndex] = game;
  }
  return {
    gameList,
    addGame,
    deleteGame,
    updateGame,
  }
})
const gameStore = useGameStore()
const tableData = ref()
const path = 'http://192.168.133.130:5000/games'
const getGames = ()=>{
    // axios.get(path).then((res)=>{
    //     tableData.value = res.data.games;
    // })
    tableData.value = gameStore.gameList;
}
const addGame = (payload) => {
    // axios.post(path,payload).then((res)=>{
    //     console.log(res.data);
    //     message.value = res.data.message;
    //     getGames();
    //     ElMessage({
    //         message: message.value,
    //         type: 'success',
    //     })
    // })
    gameStore.addGame(payload);
    message.value = "game has added!";
    getGames();
    ElMessage({
        message: message.value,
        type : 'success',
    })
}
const deleteGame = (game)=>{
    // axios.delete(path+'/'+game_id).then((res)=>{
    //     getGames();
    //     message.value = res.data.message;
    //     ElMessage({
    //         message: message.value,
    //         type: 'success',
    //     })
    // })
    gameStore.deleteGame(game);
    getGames();
    message.value = "game has deleted!";
    ElMessage({
        message: message.value,
        type : 'success',
    })
}
const updateGame = (payload)=>{
    // axios.put(path+'/'+payload.id,payload).then((res)=>{
    //     message.value = res.data.message;
    //     getGames();
    //     ElMessage({
    //         message: message.value,
    //         type: 'success',
    //     })
    // })
    gameStore.updateGame(payload);
    getGames();
    message.value = "game has updated!";
    ElMessage({
        message: message.value,
        type : 'success',
    })
}
const editGame = (game)=>{
    updateGameDialog.value = true;
    console.log(game);
    console.log(game.title);
    updateGameForm.value.id = game.id;
    updateGameForm.value.title = game.title;
    updateGameForm.value.genre = game.genre;
    updateGameForm.value.played = game.played;
}


const message = ref('')
const addGameDialog = ref(false)
const addGameForm = ref({
    title:'',
    genre:'',
    played: false
})
const updateGameDialog = ref(false)
const updateGameForm = ref({
    id: '',
    title: '',
    genre: '',
    played: false
})
onMounted(()=>{
    getGames();
})
const onSubmit = () => {
    console.log(addGameForm.value.played);
    const payload = {
        title : addGameForm.value.title,
        genre : addGameForm.value.genre,
        played : addGameForm.value.played,
    }
    addGame(payload);
    addGameDialog.value = false;
}
const updateSubmit = () => {
    const payload = {
        id : updateGameForm.value.id,
        title : updateGameForm.value.title,
        genre : updateGameForm.value.genre,
        played : updateGameForm.value.played,
    }
    updateGame(payload);
    updateGameDialog.value = false;
}
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
                    <button class="btnAdd-popup" @click="addGameDialog=true">Add</button>
                    <el-divider/>
                </el-row>
            </el-header>
            <el-main>
                <hr><br>
                <el-table 
                    :data="tableData"  
                    style="max-width:800px;margin:0 auto"
                    >
                    <el-table-column prop="title" label="Title" min-width="80" align="center"/>
                    <el-table-column prop="genre" label="Genre" min-width="80" align="center"/>
                    <el-table-column prop="played" label="Played?" min-width="80" align="center"/>
                    <el-table-column label="Actions" min-width="150" align="center">
                        <!-- 要拿到对应的Id，必须通过使用作用域插槽来实现操作列的渲染 -->
                        <template v-slot="scope">
                            <el-button round type="primary" size="small" @click="editGame(scope.row)">update</el-button>
                            <el-button round type="danger" size="small" @click="deleteGame(scope.row)">delete</el-button>
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
    <el-dialog
        v-model="addGameDialog"
        title="Add a new game"
        width="30%">
        <el-form label-width="80px">
            <el-form-item label='title'>
                <el-input placeholder="enter title" v-model="addGameForm.title"></el-input>
            </el-form-item>
            <el-form-item label='genre'>
                <el-input placeholder="enter genre" v-model="addGameForm.genre"></el-input>
            </el-form-item>
            <el-form-item label="played?">
                <el-checkbox label="yes" v-model="addGameForm.played">{{ addGameForm.played }}</el-checkbox>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="onSubmit">Submit</el-button>
                <el-button @click="addGameDialog=false">Cancel</el-button>
            </el-form-item>
        </el-form>
    </el-dialog>
    <el-dialog
        v-model="updateGameDialog"
        title="Edit a game"
        width="30%">
        <el-form label-width="80px">
            <el-form-item label='title'>
                <el-input placeholder="enter title" v-model="updateGameForm.title"></el-input>
            </el-form-item>
            <el-form-item label='genre'>
                <el-input placeholder="enter genre" v-model="updateGameForm.genre"></el-input>
            </el-form-item>
            <el-form-item label="played?">
                <el-checkbox label="yes" v-model="updateGameForm.played">
                    {{ updateGameForm.played }}
                </el-checkbox>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="updateSubmit">Submit</el-button>
                <el-button @click="updateGameDialog=false">Cancel</el-button>
            </el-form-item>
        </el-form>
    </el-dialog>
</template>
<style scoped>
#building{
    background:linear-gradient(rgba(233, 226, 226, 0.251), rgba(228, 223, 223, 0.551)), url('../assets/wallhaven1.jpg') no-repeat ;
    background-attachment: fixed;
    width:100%;		
    height:100%;		
    background-size:100% 100%;
    position:fixed;
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