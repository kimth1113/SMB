<template>
  <div class="flex justify-content-center align-top" style="margin-top : 50px;">
    <div class="d-flex justify-content-start">
      <h3 style="margin-top : 50px;"><b>#내가 좋아하는 영화들</b></h3>
    </div>
      <div class="row">
        <div 
          v-for="(movie,idx) in userlikes"
          :key=idx
          class="col-2"
        >
          <div class="card">
            <MoviePoster
              :movie="movie"
            />
          </div>
        </div>
      </div>
    <div class="d-flex justify-content-start">
      <h3 style="margin-top : 50px;"><b>#내가 쓴 리뷰들</b></h3>
    </div>
    <div class="row">
      <div class="col-3">
        <h5><b></b></h5>
      </div>
      <div class="col-3">
        <h5><b>영화제목</b></h5>
      </div>
      <div class="col-3">
        <h5><b>평점</b></h5>
      </div>
      <div class="col-3">
        <h5><b>내용</b></h5>
      </div>
    </div>
    <br>
    <div
      class=""
      v-for="(review, idx) in userreviews"
      :key="idx" 
    >
      <MovieCard
        :review="review"
      />
    </div>
  </div>
</template>
<script>
import MoviePoster from '@/components/MoviePoster.vue'
import MovieCard from '@/components/MovieCard.vue'
export default {
  name : 'MyPage',
  components :{
    MoviePoster,
    MovieCard,
  },
  computed : {
    username () {
      return this.$store.getters.getUser
    },
    userlikes () {
      return this.$store.getters.getUserLikes
    },
    userreviews() {
      return this.$store.getters.getUserReviews
    }
  },
  created () {
      this.$store.dispatch('GET_USER_LIKES', this.$store.getters.getUserId)
      this.$store.dispatch('GET_USER_REVIEWS', this.$store.getters.getUserReviews)
      console.log(this.userreviews)
  },

  
}
</script>

<style>

</style>