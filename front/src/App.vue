<template>
    <div id="app">
        <el-container>
            <el-header>
                <myheader></myheader>
            </el-header>
            <el-main>
                <router-view></router-view>
            </el-main>
        </el-container>
    </div>
</template>

<script>
import Header from './components/Header.vue'

export default {
  name: 'app',
  components: {
      'myheader': Header
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>
