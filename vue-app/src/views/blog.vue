<template>
  <el-container class="maxHeight">
    <el-header style="padding: 0;">
      <HeadNav :activeIndex="2"></HeadNav>
    </el-header>
    <el-row class="maxHeight">
      <el-col class="maxHeight" :span="4">
        <div class="grid-content bg-purple maxHeight" style="background-color: #2c3e50">111</div>
      </el-col>
      <el-col :span="14">
        <div class="grid-content bg-purple-light maxHeight" style="background-color: #888888">
          <el-row v-for="article in articles">
            <el-col :span="22" :offset="1">
              <el-card shadow="hover" style="margin-top:15px">

                <el-row>
                  <el-col :span="18" :offset="1" style="text-align: left;margin-top:5px;font-size:2rem">
                    {{ article.title }}
                  </el-col>
                </el-row>
                <el-row>
                  <el-col :span="4" :offset="1" style="text-align: left;font-size:1rem">
                    {{ article.author }}
                  </el-col>
                  <el-col :span="4" :offset="1" style="text-align: right">
                    {{ formatDate(article.updated) }}
                  </el-col>
                </el-row>
              </el-card>
            </el-col>
            <br/>
          </el-row>
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
import axios from 'axios'

export default {
  name: "blog",
  components: {
    HeadNav
  },
  data() {
    return {
      articles: []
    };
  },
  mounted() {
    this.get_article()
  },
  methods: {
    get_article() {
      axios.get(this.$apiUrl + "/blog/articles/")
          .then(
              (response) => {
                this.articles = response.data.data;
              })
          .catch(err => console.log(err));
    },
    formatDate: function (dateValue) {
      let date = new Date(dateValue)
      return `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate()} ${date.getHours()}:${date.getMinutes()}`
    }
  }

}
</script>

<style scoped>

</style>