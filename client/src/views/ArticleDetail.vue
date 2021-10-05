<template>
  <div v-if="detail_article" >
    <h1 style="margin-top : 50px;">{{this.detail_article.title}}</h1>
    <p><b>{{this.detail_article.content}}</b></p>
    <br>
    <div class="d-flex justify-content-end">
      <router-link :to="`/api/v1/commuity/${this.detail_article.id}/article_update/`">
        <button class="btn btn-light">Edit</button>
      </router-link>
      <button style="margin-left : 10px;" class="btn btn-light" @click="articleDelete">Del</button>
    </div>
    <br>
    <div
      class="d-flex"
      v-for= "(comment,idx) in comments"
      :key="idx"
    >
      <p
        :comment="comment"
        v-if="comment"
        @click="Delete(comment)"
      >{{comment.content}}</p>
    </div>
    <input 
      type="text" 
      v-model="commentForm.content"
      @keyup.enter="Submit"
    >
  </div>
</template>

<script>
export default {
  name : "Articledetail",
  data () {
    return {
      commentForm : {
        article_id : '',
        content : '',
      },
      commentdeleteForm: {
        article_id : '',
        comment_id : '',
      },
      articledeleteForm : {
        article_id : '',
      },
      articleupdateForm : {
        article_id : '',
      },
    }
  },
  computed : {
    detail_article() {
      return this.$store.getters.getDetailArticle
    },
    comments() {
      return this.$store.getters.getArticleComment
    },
  },
  props : {
    article_id : String,
  },
  async created () {
    this.$store.dispatch('GET_ARTICLE_DETAIL', this.$route.params.article_id)
    this.$store.dispatch('GET_ARTICLE_COMMENT', this.$route.params.article_id)
  },
  methods : {
    Submit() {
      this.commentForm['article_id'] = this.$store.getters.getDetailArticle['id']
      this.$store.dispatch('CREATE_ARTICLE_COMMENT', this.commentForm)
      this.commentForm.content = ''
    },
    Delete(comment) {
      this.commentdeleteForm['article_id'] = this.$store.getters.getDetailArticle['id']
      this.commentdeleteForm['comment_id'] = comment['id']
      this.$store.dispatch('DELETE_ARTICE_COMMENT', this.commentdeleteForm)
      .then(()=>{
        this.$router.go('/api/v1/community/')
      })
    },
    articleDelete() {
      this.articledeleteForm['article_id'] = this.$store.getters.getDetailArticle['id']
      this.$store.dispatch('DELETE_ARTICLE', this.articledeleteForm)
      .then(
        this.$router.push('/api/v1/community/')
      )
    },
  },
}
</script>

<style>

</style>