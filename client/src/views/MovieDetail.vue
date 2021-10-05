<template>


  <div v-if="movie">
    <div class="card my-5 mx-auto" style="width: 60%">
      <div class="card-header">
        <h5 class="card-title">{{this.movie.title}}</h5>
        <button
          style="color:red;"
          v-if="LikeBtn"
          @click="Like"
        ><i class="fas fa-heart"></i></button>
        <button 
          v-else
          @click="Like"
        >
          <i class="far fa-heart"></i>
        </button>
      </div>
      <img :src="`https://image.tmdb.org/t/p/w300${this.movie.poster_path}`"  class="mx-auto" style="width: 100%" alt="">
      <div class="card-body">
        <p
          v-if="this.movie.overview"
          class="overview card-text fs-5"
        >{{this.movie.overview}}</p>
        <div v-if="this.TRAILER_URL" style="margin-right:10px">
          <a :href="this.TRAILER_URL"><span style="color:blue"><button type="button" class="btn btn-warning">예고편</button></span></a>
        </div>
        <p
          v-else
        >
          아직 줄거리가 없습니다.....
        </p>
      </div>
      <div class="card-footer">
        <div v-if="reviews">
          <div
            v-for="(review, idx) in Reviews"
            :key="idx"
          >
            <Review
              :review="review"
              :id="id"
            />
          </div>
        </div>
        <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
          한 줄 평 작성하기
        </button>
      </div>
    </div>
    
    
      


    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
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
            <button type="button" @click="ReviewCreate" class="btn btn-light">저장하기</button>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import Review from '@/components/Review.vue'
import axios from 'axios'
export default {
  name : 'Moviedetail',
  components : {
    Review
  },
  data () {
    return {
      userLikes : '',
      likeStatus : '',
      backgroundImage : '',
      TRAILER_URL : '',
      posters : '',
      backdrops : [],
      ReviewForm : {
        rate : '',
        content :'',
        user_id : '',
        username : '',
        movie_id : '',
      },
      reviews : '',
      movie_id : this.id
    }
  },
  computed : {
    movie() {
      return this.$store.getters.getMovieDetail
    },

    LikeBtn() {
      if (this.$store.getters.getUserLikes) {
        for (let i = 0; i < this.$store.getters.getUserLikes.length;i ++){
          if (this.$store.getters.getUserLikes[i].movie_id == this.id){
            return true
          }
        }
      }
      return false
    },
    Reviews() {
      return this.$store.getters.getMovieReviews
    }

  },
  watch : {
    Reviews(val) {
      this.reviews = val
    },
    LikeBtn(val) {
      this.likeStatus = val
    },
  },
  props: {
    id : String,
  },
  created () {
    this.$store.dispatch('GET_MOVIE_DETAIL', this.id)
    this.$store.dispatch('GET_USER_LIKES', this.$store.getters.getUserId)
    this.$store.dispatch('MOVIE_REVIEW_LIST', this.id)
    this.$store.dispatch('MOVIE_CNT_URL', this.id)

    const GET_TRAILER_URL = `https://api.themoviedb.org/3/movie/${this.id}/videos?api_key=223815248626f4669e7ce900ef58a20d`
    axios.get(GET_TRAILER_URL)
    .then((res)=>{
      const YOUTUBE_TRAILER_URL = `https://www.youtube.com/watch?v=${res.data.results[0].key}`
      this.TRAILER_URL = YOUTUBE_TRAILER_URL
    })



    const DETAIL_MOVIE_REVIEWS = `api/v1/movies/${this.id}/review/list/`
    axios.get(DETAIL_MOVIE_REVIEWS)

  },
  methods : {
    Like(){
      this.$store.dispatch('USER_LIKE', this.id)
      if(this.likeStatus == true) {
        this.likeStatus = false
      }else{
        this.likeStatus = true
      }
    },
    ReviewCreate() {
      this.ReviewForm.movie_id = this.id
      this.ReviewForm.username = this.$store.getters.getUser
      this.ReviewForm.user_id = this.$store.getters.getUserId
      this.$store.dispatch('REVIEW_CREATE', this.ReviewForm)
      .then(()=>{
        this.$router.push(`/api/v1/movies/detail/${this.id}/`)
      })
      this.ReviewForm.rate = ''
      this.ReviewForm.content = ''
      
    },
  }
}
</script>

<style scoped>


</style>