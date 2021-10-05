<template>
  <div class="d-flex justify-content-around">
    <p>{{review.rate}}</p>
    <p>{{review.content}}</p>
    <p>{{review.username}}</p>
    <button class="btn btn-light" type="button" data-bs-toggle="modal" data-bs-target="#updateModal">EDT</button>
    <button class="btn btn-light" @click="deleteReview">DEL</button>


    <div class="modal fade" id="updateModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">한 줄 평</h5>
          </div>
          <div class="modal-body d-flex">
            <input style="width:100px" type="number" min="0" max="10" v-model="ReviewForm.rate">
            <input type="text" @keyup.enter="ReviewCreate" v-model="ReviewForm.content">
          </div>
          <div class="modal-footer">
            <button type="button" @click="updateReview" class="btn btn-light">수정하기</button>
          </div>
        </div>
      </div>
    </div>


  </div>
</template>

<script>
export default {
  name : 'Review',
  props : {
    review : Object,
    id : String,
  },
  data() {
    return {
      ReviewForm : {
        content : '',
        rate : '',
        movie_id : this.movie_id,
      }
    }

  },
  methods : {
    deleteReview() {
      const data = {
        'review_id' : this.review.id,
        'movie_id' : this.id,
        'username' : this.$store.getters.getUser,
        'user_id' : this.$store.getters.getUserId,
        'content' : this.ReviewForm.content,
        'rate' : this.ReviewForm.rate,
      }
      this.$store.dispatch('REVIEW_DELETE', data)
    },
    updateReview() {
      const data = {
        'review_id' : this.review.id,
        'movie_id' : this.id,
        'username' : this.$store.getters.getUser,
        'user_id' : this.$store.getters.getUserId,
        'content' : this.ReviewForm.content,
        'rate' : this.ReviewForm.rate,
      }
      this.$store.dispatch('UPDATE_REVIEW', data)
    }
  }

}
</script>

<style>

</style>