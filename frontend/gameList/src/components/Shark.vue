<script setup>
import axios from 'axios';
import {ref} from 'vue';
const msg = ref()
const path = 'http://192.168.133.130:5000/shark'
axios.get(path).then((res)=>{
    console.log(res.data);
    msg.value = res.data;
})
</script>
<template>
    <el-button round>{{ msg }}</el-button>
    <button type="button" class="btn btn-primary">shark🦈</button>
</template>