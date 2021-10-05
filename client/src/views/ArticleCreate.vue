<template>
  <div>
    <div style="margin-top : 50px;"></div>
    <div class="mb-3">
      <input v-model="articleForm.title" type="text" class="form-control" id="exampleFormControlInput1" placeholder="title" >
    </div>
    <div class="mb-3">
      <textarea v-model="articleForm.content" class="form-control" id="exampleFormControlTextarea1" @keyup.enter="Submit" placeholder="content" rows="3"></textarea>
    </div>
    <button @click="Submit">작성하기</button>
  </div>
</template>

<script>
export default {
  name : 'ArticleCreate',
  data () {
    return {
      articleForm : {
        title : '',
        content : '',
      }
    }
  },
  methods : {
    Submit() {
      this.$store.dispatch('ARTICLE_CREATE', this.articleForm)
      .then(()=>{
          this.$router.push('/api/v1/community/')
      })
    },
  }

}
</script>

<style>

</style>