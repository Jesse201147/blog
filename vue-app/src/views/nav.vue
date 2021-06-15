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
              <el-col :span="3" :offset="3">
                <el-button class="quickLink" @click="open_url('https://www.zhihu.com/')">知乎</el-button>
              </el-col>
              <el-col :span="3">
                <el-button class="quickLink" @click="open_url('https://weibo.com/')">微博</el-button>
              </el-col>
              <el-col :span="3">
                <el-button class="quickLink" @click="open_url('https://juejin.cn/')">掘金</el-button>
              </el-col>
              <el-col :span="3">
                <el-button class="quickLink" @click="open_url('https://www.bilibili.com/')">B站</el-button>
              </el-col>
              <el-col :span="3">
                <el-button class="quickLink" @click="open_url('https://www.youtube.com/')">油管</el-button>
              </el-col>
              <el-col :span="3">
                <el-button class="quickLink" @click="open_url('https://github.com/')">GitHub</el-button>
              </el-col>
            </el-row>
            <el-row style="padding-top: 10px">
              <el-col :span="3" :offset="3">
                <el-button class="quickLink" @click="open_url('https://www.taobao.com/')">淘宝</el-button>
              </el-col>
              <el-col :span="3">
                <el-button class="quickLink" @click="open_url('https://www.jd.com/')">京东</el-button>
              </el-col>
              <el-col :span="3">
                <el-button class="quickLink" @click="open_url('https://www.1688.com/')">1688</el-button>
              </el-col>
              <el-col :span="3">
                <el-button class="quickLink" @click="open_url('https://www.smzdm.com/')">SMZDM</el-button>
              </el-col>
              <el-col :span="3">
                <el-button class="quickLink" @click="open_url('https://www.douyu.com/g_DOTA2')">斗鱼</el-button>
              </el-col>
              <el-col :span="3">
                <el-button class="quickLink" @click="open_url('https://www.huya.com/g/dota2')">虎牙</el-button>
              </el-col>
            </el-row>
            <el-row style="padding-top: 10px">
              <el-col :span="3" :offset="3">
                <el-button class="quickLink" @click="open_url('https://www.aliyun.com/')">阿里云</el-button>
              </el-col>
              <el-col :span="3">
                <el-button class="quickLink" @click="open_url('https://cloud.tencent.com/')">腾讯云</el-button>
              </el-col>
              <el-col :span="3">
                <el-button class="quickLink" @click="open_url('https://sg.godaddy.com/')">GoDaddy</el-button>
              </el-col>
              <el-col :span="3">
                <el-button class="quickLink" @click="open_url('https://www.aliyundrive.com/drive')">阿里云盘</el-button>
              </el-col>
              <el-col :span="3">
                <el-button class="quickLink" @click="open_url('https://drive.google.com/drive')">Colab</el-button>
              </el-col>
              <el-col :span="3">
                <el-button class="quickLink" @click="open_url('https://onedrive.live.com/')">oneDrive</el-button>
              </el-col>
            </el-row>
            <el-row style="padding-top: 10px">
              <el-col :span="3" :offset="3">
                <el-button class="quickLink" @click="open_url('https://www.szlcsc.com/')">立创商城</el-button>
              </el-col>
              <el-col :span="3">
                <el-button class="quickLink" @click="open_url('https://www.jlc.com/')">立创PCB</el-button>
              </el-col>
              <el-col :span="3">
                <el-button class="quickLink" @click="open_url('https://lceda.cn/')">立创EDA</el-button>
              </el-col>
              <el-col :span="3">
                <el-button class="quickLink" @click="open_url('https://mail.google.com/')">Gmail</el-button>
              </el-col>
              <el-col :span="3">
                <el-button class="quickLink" @click="open_url('https://mail.qq.com/')">QQ邮箱</el-button>
              </el-col>
              <el-col :span="3">
                <el-button class="quickLink" @click="open_url('https://mail.163.com/')">163邮箱</el-button>
              </el-col>
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
    },
    open_url(url) {
      window.open(url)
    }
  }
}
</script>

<style scoped>

</style>