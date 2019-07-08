<template>
    <div>
        <el-container>
            <el-header>
                <myheader></myheader>
            </el-header>

            <!-- 一个人的卡片 -->
                <el-card class="box-card right-card list-card">
                    <span style="margin-bottom: 45px;">
                        <h2>
                            <i class="el-icon-s-flag"></i>
                            今天是{{ today | dateFormat() }}。
                        </h2>
                    </span>
                    <el-checkbox-group v-model="right_lists">
                        <div v-for="item in right_lists" class="listitem">
                            <el-row type="flex">
                                <el-col :span="23">
                                    <div class="list">
                                        <el-checkbox v-model="item.checked" @click="checkedtask(item.id)">
                                            <span :class="{ delit: item.checked }" @click.prevent="open(item.id, item.task)" >{{ item.task }}</span>
                                        </el-checkbox>
                                    </div>
                                </el-col>
                                <el-col :span="1">
                                    <el-link :underline="false" class="toright close" @click="deletetask(item.id)">
                                        <i class="el-icon-close"></i>
                                    </el-link>
                                </el-col>
                            </el-row>
                            <el-divider></el-divider>
                        </div>
                    </el-checkbox-group>
                    <!-- 用户添加任务 -->
                    <div class="listitem">
                        <el-row type="flex">
                            <el-col :span="23">
                                <el-input v-model="newtask" placeholder="添加任务" prefix-icon="el-icon-plus" style="width: 98%;"></el-input>
                            </el-col>
                            <el-col :span="1">
                                <el-button type="primary" icon="el-icon-plus" circle @click="addtask" class="toright"></el-button>
                            </el-col>
                        </el-row>
                        <el-divider></el-divider>
                    </div>
                    <!-- 用户添加任务 结束 -->
                </el-card>
                <!-- 一个人的卡片 结束 -->
            </el-main>
        </el-container>

    </div>
</template>

<script>
// api
import { getTask, deleteTask, changeTask } from '../api/todo.js'
import { getTaskList, addTask } from '../api/todolist.js'

// components
import Header from './Header.vue'

/* eslint-disable */
export default {
    components: {
        'myheader': Header
    },
    data() {
        return {
            right_lists: [
                { 'id': 0, 'task': '网络异常...', 'checked': true, 'share': 0 },
            ],
            newtask: '',
            today: new Date(),
            checkList: ['选中且禁用','复选框 A']
        }
    },
    methods: {
        fetchData() {
            // 初始化数据
            getTaskList().then(response => {
                console.log(response.data)
                this.right_lists = response.data
            })
        },
        stopclick(value) {
            console.log(value)
        },
        check() {
            // 检测输入框为空
            if ( this.newtask == '' ) {
                this.$message({
                    showClose: true,
                    message: '抱歉，任务名不能为空呀！',
                    type: 'warning'
                });
                return false
            } else {
                return true
            }
        },
        addtask() {
            // 添加任务
            if ( this.check() ) {
                var task = {
                    'task': this.newtask,
                    'checked': false,
                    'share': 0
                }
                // 扔后端
                addTask(task).then( response => {
                    console.log(response)
                } )


                this.right_lists.push(task)
                this.newtask = ''
            }
        },
        deletetask(taskid) {
            // 删除任务
            // 后端删除
            deleteTask(taskid)
            // 前端删除
            var index = this.right_lists.findIndex(item => {
                if (item.id == taskid) {
                    return true;
                }
            })
            this.right_lists.splice(index, 1)
        },
        checkedtask(taskid) {
            console.log(taskid)
        },
        open(taskid, taskname) {
            this.$confirm('添加额外内容，待增加', taskname, {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'info'
            })
        }
    },
    filters: {
        dateFormat: function( dateStr, pattern = '' ) {
            var dt = new Date(dateStr)
            var y = dt.getFullYear()
            var m = (dt.getMonth() + 1).toString().padStart(2, '0')
            var d = dt.getDate().toString().padStart(2, '0')

            return `${y}年${m}月${d}日`
        }
    },
    created() {
        this.fetchData()
    }
}
</script>

<style>
.list-card {
    height:auto!important;
    min-height:800px;
    height:auto;
}
.delit {
    text-decoration: line-through;
}
.toright {
    float: right;
}
.close {
    margin-right: 2%;
}
.listitem:hover .el-divider {
    background-color: #c04851;
}
</style>
