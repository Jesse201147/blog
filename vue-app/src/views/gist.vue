<template>

  <el-container class="maxHeight">
    <el-header style="padding: 0;">
      <HeadNav activeIndex="3"></HeadNav>
    </el-header>
    <el-row class="maxHeight">
      <el-col class="maxHeight" :span="4">
        <div class="grid-content bg-purple maxHeight" style="background-color: #2c3e50">111</div>
      </el-col>
      <el-col :span="14">
        <div class="grid-content bg-purple-light maxHeight" style="background-color: #888888">222
        </div>
      </el-col>
      <el-col :span="6">
        <div class="grid-content bg-purple maxHeight" style="background-color: aliceblue">333</div>
      </el-col>
    </el-row>
  </el-container>

</template>

<script>
import HeadNav from "../components/HeadNav.vue";

export default {
  name: "gist",
  components: {
    HeadNav
  },
  data() {
    return {
    };
  },
  mounted() {
  }

}
</script>

<style scoped>

</style>