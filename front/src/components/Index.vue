<template>
    <el-row>
        <el-col :span="12">
            <!-- 左侧卡片 -->
            <el-card class="box-card left-card list-card">
                <P style="margin-bottom: 45px;">小明的任务：</P>
                <div v-for="item in left_lists" :key="item.name">
                    <el-checkbox v-model="item.checked">
                        <span :class="{ delit: item.checked }" >{{ item.name }}</span>
                    </el-checkbox>
                    <span class="showtime">{{ item.time }}</span>
                    <el-divider></el-divider>
                </div>
            </el-card>
            <!-- 左侧卡片 结束 -->
        </el-col>
        <el-col :span="12">
            <!-- 右侧卡片 -->
            <el-card class="box-card right-card list-card">
                <P style="margin-bottom: 45px;"><i class="el-icon-s-flag"></i> 你的任务：</P>
                <div v-for="item in right_lists" :key="item.name">
                    <div class="list">
                        <el-checkbox v-model="item.checked">
                            <span :class="{ delit: item.checked }" >{{ item.name }}</span>
                        </el-checkbox>
                    </div>
                    <span class="showtime">{{ item.time }}</span>
                    <el-divider></el-divider>
                </div>
            <!-- 用户添加任务 -->
            <div>
                <el-row>
                    <el-col :span="11">
                        <el-input v-model="newtask" placeholder="添加任务" prefix-icon="el-icon-plus" style="width: 400px;"></el-input>
                    </el-col>
                    <el-col :span="11">
                            <el-time-picker
                                style="float:right;"
                                format="HH:mm"
                                value-format="HH:mm"
                                is-range
                                v-model="newtasktime"
                                range-separator="至"
                                start-placeholder="开始时间"
                                end-placeholder="结束时间"
                                placeholder="选择时间范围">
                            </el-time-picker>
                    </el-col>
                    <el-col :span="2">
                        <el-button type="primary" icon="el-icon-plus" circle style="float:right;" @click="addtask"></el-button>
                    </el-col>
                </el-row>
                <el-divider></el-divider>
            </div>
            <!-- 用户添加任务 结束 -->
            </el-card>
            <!-- 右侧卡片 结束 -->
        </el-col>
    </el-row>
</template>

<script>
export default {
    data() {
        return {
            left_lists: [
                { 'name': '早起', 'checked': true, 'time': '6:00 - 6:30', 'share': 0 },
                { 'name': '吃早餐', 'checked': true, 'time': '6:30 - 7:00', 'share': 0 },
                { 'name': '看一小时书', 'checked': true, 'time': '7:00 - 8:00', 'share': 0 },
                { 'name': '学习线性代数', 'checked': false, 'time': '8:00 - 11:00', 'share': 0 },
                { 'name': '去食堂吃饭', 'checked': false, 'time': '11:00 - 11:30', 'share': 0 },
                { 'name': '刷题', 'checked': false, 'time': '11:30 - 18:00', 'share': 0 },
                { 'name': '其他', 'checked': false, 'time': '18:00 - xx:xx', 'share': 0 }
            ],
            right_lists: [
                { 'name': '早起', 'checked': true, 'time': '6:00 - 6:30', 'share': 0 },
                { 'name': '吃早餐', 'checked': true, 'time': '6:30 - 7:00', 'share': 0 },
                { 'name': '复习期末考试', 'checked': false, 'time': '7:00 - 11:00', 'share': 0 },
                { 'name': '去食堂吃饭', 'checked': false, 'time': '11:00 - 11:30', 'share': 0 },
                { 'name': '去超市买零食', 'checked': false, 'time': '11:30 - 13:00', 'share': 0 },
                { 'name': '其他', 'checked': false, 'time': '13:00 - xx:xx', 'share': 0 }
            ],
            newtask: '',
            newtasktime: ''
        }
    },
    methods: {
        stopclick(value) {
            console.log(value)
        },
        addtask() {
            var task = {
                'name': this.newtask,
                'checked': false,
                'time': this.newtasktime[0] + ' - ' + this.newtasktime[1],
                'share': 0
            }
            this.right_lists.push(task)
            this.newtask = ''
            this.newtasktime = []
        }
    }
}
</script>

<style>
body {
    background-color: #c04851;
    height: 43px;
}
.list-card {
    height:auto!important;
    min-height:800px;
    height:auto;
    min-width: 500px;
}
.left-card {
    margin-right: 10px;
}
.right-card {
    margin-left: 10px;
}
.delit {
    text-decoration: line-through;
}
.showtime {
    float: right;
    margin-right: 5px;
}
</style>
