<template>
    <div>
        <ul>
            <li>
                <img src="../assets/logo.png" alt="logo" class="logoimg">
            </li>
            <li><a href="#home">首页</a></li>
            <li><a href="#news">历史任务</a></li>
            <li><a href="#about">关于</a></li>
            <li class="menu">
                <a href="#" class="alink"><i class="el-icon-user"></i> 假装已经登陆的你 </a>
            </li>
        </ul>
    </div>
</template>


<style>
.menu {
    float: right;
}
.logo {
    float:left;
    margin-top: 2px;
}
.logoimg {
    height: 40%;
    width: 40%;
    min-width: 40px;
    min-height: 40px;
    margin-left: 10px;
}
ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
    overflow: hidden;
}
li {
    float: left;
}
li a {
    display: block;
    color: white;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
}
li a:hover {
    border-radius: 4px;
    background-color: #409EFF;
}
</style>
