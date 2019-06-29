<template>
    <el-row>
        <el-col :span="12">
            <span class="logo">
                <img src="../assets/logo.png" alt="logo" class="logoimg">
            </span>
        </el-col>
        <el-col :span="12">
            <div class="menu">
                <el-link href="#" class="alink"><i class="el-icon-user"></i> 假装已经登陆的你 </el-link>
            </div>
        </el-col>
    </el-row>
</template>


<style>
.menu {
    float: right;
    margin-top: 30px;
    margin-right: 20px;
}
.logo {
    float:left;
    margin-top: 10px;
}
.logoimg {
    height: 45%;
    width: 45%;
    min-width: 57px;
    min-height: 57px;
    margin-left: 10px;
}
</style>
