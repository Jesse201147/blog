<template>

  <el-container class="maxHeight">
    <el-header style="padding: 0;">
      <HeadNav activeIndex="1"></HeadNav>
    </el-header>
    <el-row class="maxHeight">

      <el-col :span="14" :offset="4">
        <div class="grid-content bg-purple-light maxHeight">
          <div>
            <el-row style="padding-top: 15%">
              <el-col :span="3" :offset="4" style="margin-top: 15px">
                <el-select v-model="select" placeholder="请选择" default-first-option>
                  <el-option key="1" label="Google" value="1"></el-option>
                  <el-option key="2" label="Baidu" value="2"></el-option>
                  <el-option key="3" label="Bing" value="3"></el-option>
                </el-select>
              </el-col>
              <el-col :span="12">
                <div class="grid-content bg-purple-light">
                  <div style="margin-top: 15px">
                    <el-input
                        placeholder="请输入内容"
                        v-model="input"
                        class="input-with-select"
                        @keydown.enter="search()"
                    >
                      <template #append>
                        <el-button icon="el-icon-search" @click="search()"></el-button>
                      </template>
                    </el-input>
                  </div>
                </div>
              </el-col>
            </el-row>
            <el-row style="padding-top: 10%">
              <el-col :span="3" :offset="3" style="background-color: brown"><el-button class="quickLink">默认按钮</el-button></el-col>
              <el-col :span="3"  style="background-color: greenyellow"><el-button class="quickLink">默认按钮</el-button></el-col>
              <el-col :span="3"  style="background-color: greenyellow"><el-button class="quickLink">默认按钮</el-button></el-col>
              <el-col :span="3"  style="background-color: greenyellow"><el-button class="quickLink">默认按钮</el-button></el-col>
              <el-col :span="3"  style="background-color: greenyellow"><el-button class="quickLink">默认按钮</el-button></el-col>
              <el-col :span="3"  style="background-color: greenyellow"><el-button class="quickLink">默认按钮</el-button></el-col>
            </el-row>
            <el-row style="padding-top: 10px">
              <el-col :span="3" :offset="3" style="background-color: brown"><el-button class="quickLink">默认按钮</el-button></el-col>
              <el-col :span="3"  style="background-color: greenyellow"><el-button class="quickLink">默认按钮</el-button></el-col>
              <el-col :span="3"  style="background-color: greenyellow"><el-button class="quickLink">默认按钮</el-button></el-col>
              <el-col :span="3"  style="background-color: greenyellow"><el-button class="quickLink">默认按钮</el-button></el-col>
              <el-col :span="3"  style="background-color: greenyellow"><el-button class="quickLink">默认按钮</el-button></el-col>
              <el-col :span="3"  style="background-color: greenyellow"><el-button class="quickLink">默认按钮</el-button></el-col>
            </el-row>

          </div>
        </div>
        <div>
        </div>
      </el-col>
    </el-row>
  </el-container>


</template>

<script>
import HeadNav from "../components/HeadNav.vue";
import Search from "../components/search.vue";

export default {
  name: "nav",
  components: {
    Search,
    HeadNav,
  },
  data() {
    return {
      input: "",
      select: "1",
      quickLink: {},
    };
  },
  mounted() {
  },
  methods: {
    search() {
      let url;
      if (this.select === "1") {
        url = "https://www.google.com/search?q=" + this.input;
      } else if (this.select === "2") {
        url = "https://www.baidu.com/s?wd=" + this.input;
      } else if (this.select === "3") {
        url = "https://www.bing.com/search?q=" + this.input;
      }
      console.log(url);
      window.open(url)
    }
  }
}
</script>

<style scoped>

</style>