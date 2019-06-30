<template>
    <div>
        <!-- 一个人的卡片 -->
        <el-card class="box-card right-card list-card">
            <P style="margin-bottom: 45px;">
                <h2>
                    <i class="el-icon-s-flag"></i>
                    今天是{{ today | dateFormat() }}。
                </h2>
            </P>
            <div v-for="item in right_lists" :key="item.name" class="listitem">
                <el-row type="flex">
                    <el-col :span="12">
                        <div class="list">
                            <el-checkbox v-model="item.checked">
                                <span :class="{ delit: item.checked }" @click.prevent="open(item.id, item.name)" >{{ item.name }}</span>
                            </el-checkbox>
                        </div>
                    </el-col>
                    <el-col :span="11">
                        <span class="toright">{{ item.time }}</span>
                    </el-col>
                    <el-col :span="1">
                        <el-link :underline="false" class="toright close" @click="deletetask(item.id)">
                            <i class="el-icon-close"></i>
                        </el-link>
                    </el-col>
                </el-row>
                <el-divider></el-divider>
            </div>
            <!-- 用户添加任务 -->
            <div class="listitem">
                <el-row type="flex">
                    <el-col :span="12">
                        <el-input v-model="newtask" placeholder="添加任务" prefix-icon="el-icon-plus" style="width: 95%;"></el-input>
                    </el-col>
                    <el-col :span="10">
                        <el-time-picker
                            class="toright"
                            style="width: 75%;"
                            format="HH:mm"
                            value-format="HH:mm"
                            is-range
                            v-model="newtasktime"
                            range-separator="-"
                            start-placeholder="开始"
                            end-placeholder="结束"
                            placeholder="选择时间范围">
                        </el-time-picker>
                    </el-col>
                    <el-col :span="2">
                        <el-button type="primary" icon="el-icon-plus" circle @click="addtask" size="mini" class="toright"></el-button>
                    </el-col>
                </el-row>
                <el-divider></el-divider>
            </div>
            <!-- 用户添加任务 结束 -->
        </el-card>
        <!-- 一个人的卡片 结束 -->
    </div>
</template>

<script>
export default {
    data() {
        return {
            right_lists: [
                { 'id': 0, 'name': '早起', 'checked': true, 'time': '6:00 - 6:30', 'share': 0 },
                { 'id': 1, 'name': '吃早餐', 'checked': true, 'time': '6:30 - 7:00', 'share': 0 },
                { 'id': 2, 'name': '复习期末考试', 'checked': false, 'time': '7:00 - 11:00', 'share': 0 },
                { 'id': 3, 'name': '去食堂吃饭', 'checked': false, 'time': '11:00 - 11:30', 'share': 0 },
                { 'id': 4, 'name': '去超市买零食', 'checked': false, 'time': '11:30 - 13:00', 'share': 0 },
                { 'id': 5, 'name': '其他', 'checked': false, 'time': '13:00 - xx:xx', 'share': 0 }
            ],
            newtask: '',
            newtasktime: '',
            today: new Date()
        }
    },
    methods: {
        stopclick(value) {
            console.log(value)
        },
        check() {
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
            if ( this.check() ) {
                var task = {
                    'name': this.newtask,
                    'checked': false,
                    'time': this.newtasktime[0] + ' - ' + this.newtasktime[1],
                    'share': 0
                }
                this.right_lists.push(task)
                this.newtask = ''
            }
        },
        deletetask(taskid) {
            var index = this.right_lists.findIndex(item => {
                if (item.id == taskid) {
                    return true;
                }
            })
            this.right_lists.splice(index, 1)
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
        dateFormat: function(dateStr, pattern='') {
            var dt = new Date(dateStr)
            var y = dt.getFullYear()
            var m = (dt.getMonth() + 1).toString().padStart(2, '0')
            var d = dt.getDate().toString().padStart(2, '0')

            return `${y}年${m}月${d}日`
        }
    }
}
</script>

<style>
body {
    background-color: #c04851;
}
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
