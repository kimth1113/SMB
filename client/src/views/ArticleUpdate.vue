<template>
  <div>
    <h1 style="margin-top : 50px;">수정하기</h1>
    <input type="text" v-model="articleForm.title">
    <br>
    <input type="text" v-model="articleForm.content" @keyup.enter="Submit">
    <br>
    <button @click="Submit">Edit</button>
  </div>
</template>

<script>
export default {
  name : 'ArticleCreate',
  data () {
    return {
      articleForm : {
        title : this.$store.getters.getDetailArticle.title,
        content : this.$store.getters.getDetailArticle.content,
        user : this.$store.getters.getUserId,
        username : this.$store.getters.getUser,
        article_id : this.$store.getters.getDetailArticle.id,
      }
    }
  },
  props : {
    article_id : String,
  },
  methods : {
    Submit() {
      this.$store.dispatch('ARTICLE_UPDATE', this.articleForm)
      .then(()=>{
        this.$router.push(`/api/v1/commuity/${this.article_id}/article_detail/`)
      })
    },
  }
  
}
</script>

<style>

</style>