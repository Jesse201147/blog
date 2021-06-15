<template>
  <el-menu
      id="toolbar"
      :default-active="Index"
      class="el-menu-demo"
      mode="horizontal"
      @select="handleSelect"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b">
    <el-row type="flex" class="row-bg">

      <el-col :span="1" :offset="1">
        <div class="grid-content bg-purple">
          <el-menu-item class="navText" index="1" @click="this.$router.push({ name: 'nav'})">Home</el-menu-item>
        </div>
      </el-col>
      <el-col :span="1">
        <div class="grid-content bg-purple">
          <el-menu-item class="navText" index="2" @click="this.$router.push({ name: 'blog'})">Blog</el-menu-item>
        </div>
      </el-col>
      <el-col :span="1">
        <div class="grid-content bg-purple">
          <el-menu-item class="navText" index="3" @click="this.$router.push({ name: 'gist'})">gist</el-menu-item>
        </div>
      </el-col>

    </el-row>
  </el-menu>
</template>


<script>
export default {
  name: 'HeadNav',
  props: {
    activeIndex: String
  },
  data() {
    return {
      Index: this.activeIndex
    };
  },
  methods: {}
}
</script>
