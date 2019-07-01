<template>
    <el-form ref="form" :model="form" label-width="80px" class="loginForm">
        <el-form-item>
            <el-input placeholder="用户名" v-model="form.username"></el-input>
        </el-form-item>
        <el-form-item>
            <el-input placeholder="密码" v-model="form.password" show-password></el-input>
        </el-form-item>
        <el-form-item>
            <el-input placeholder="确认密码" v-model="form.password2" show-password></el-input>
        </el-form-item>
        <el-form-item class="submitLink">
            <el-link @click="onSubmit" :underline="false"><h2 class="submitFont">登陆</h2></el-link>
        </el-form-item>
    </el-form>
</template>

<script>
export default {
    data() {
        return {
            form: {
                name: '',
                password: '',
                passwoed2: ''
            }
        }
    },
    methods: {
        onSubmit() {
            console.log('submit!');
        }
    }
}
</script>

<style>
.submitLink {
    text-align: center;
}
.submitFont {
    color: #409EFF;
}
.loginForm {
    margin-top: 13%;
    margin-left: 40%;
    margin-right: 40%;
    min-width: 300px;
}
</style>
