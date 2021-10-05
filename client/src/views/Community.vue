<template>
  <div style="margin-top : 50px;">

    <table class="table">
      <thead>
        <tr>
          <th scope="col" style="text-align: center;">#</th>
          <th scope="col" style="text-align: center;">제목</th>
          <th scope="col" style="text-align: center;">작성자</th>
        </tr>
      </thead>
      <tbody>
        <tr
          class=""
          v-for="(article, idx) in articles"
          :key="idx" 
        >
          <th scope="row">{{article_len-idx}}</th>
          <td>
            <router-link :to="`/api/v1/commuity/${article.id}/article_detail/`">
              <span style="color:black;" class="title">
                {{article.title}}
              </span>
            </router-link>
          </td>
          <td>{{article.username}}</td>
        </tr>
      </tbody>
    </table>
    <div class="d-flex justify-content-end">
      <router-link :to="`/api/v1/commuity/article/create/`">
        <button
          class="btn btn-light"
        ><b>글쓰기</b></button>
      </router-link>
    </div>
  </div>

<!-- 
<table class="table">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">First</th>
      <th scope="col">Last</th>
      <th scope="col">Handle</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">1</th>
      <td>Mark</td>
      <td>Otto</td>
      <td>@mdo</td>
    </tr>
    <tr>
      <th scope="row">2</th>
      <td>Jacob</td>
      <td>Thornton</td>
      <td>@fat</td>
    </tr>
    <tr>
      <th scope="row">3</th>
      <td colspan="2">Larry the Bird</td>
      <td>@twitter</td>
    </tr>
  </tbody>
</table>
 -->
</template>

<script>
export default {
  name : "Community",
  computed : {
    articles() {
      return this.$store.getters.getAritcles
    },
    article_len() {
      return this.articles.length
    }
  },
  async created () {
    this.$store.dispatch('GET_ARTICLES')
  },
}
</script>

<style>
.title:hover{
  background-color: blanchedalmond;
}
</style>