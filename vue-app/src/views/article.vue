<template>

  <el-container class="maxHeight">
    <el-header style="padding: 0;">
      <HeadNav activeIndex='2'></HeadNav>
    </el-header>
    <el-row class="maxHeight">
      <el-col class="maxHeight" :span="4">
        <div class="grid-content bg-purple maxHeight" style="background-color: #2c3e50">111</div>
      </el-col>
      <el-col :span="14">
        <div class="grid-content bg-purple-light maxHeight" style="background-color: #888888">
          <!--          文章内容部分開始             -->
          {{ article }}
          <h1 class="title">{{ article.title }}</h1>
          <p class="description">{{ article.author }}</p>
          <p class="article">{{ article.body }}</p>

    <Markdown :source="article.body" />


          <!--          文章内容部分結束             -->
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
import axios from "axios";
import Markdown from 'vue3-markdown-it';

export default {
  name: "article",
  components: {
    HeadNav,
    Markdown
  },
  data() {
    return {
      article_id: this.$route.query.id,
      article: {}
    };
  },
  mounted() {
    this.get_article_detail()
  },
  methods: {
    get_article_detail() {
      axios.get(this.$apiUrl + "/blog/article/" + this.article_id)
          .then(
              (response) => {
                this.article = response.data.data;
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