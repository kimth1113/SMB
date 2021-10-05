<template>
  <div class="align-center" style="margin-top : 50px;">
    <div>
      <h3 class="d-flex"><b>#조회수가 높은 영화</b></h3>
    </div>
    <div>
      <div v-if="Recommended" class="row">
        <div 
          v-for="(movie,idx) in Recommended"
          :key=idx
          class="col"
        >
          <div class="card">
            <MoviePoster
              :movie="movie"
            />
            <span>{{movie.cnt}}</span>
          </div>
        </div>
      </div>
    </div>
    <div>
       <h3 class="d-flex"><b>#리뷰가 많은 영화</b></h3>
    </div>
    <div>
      <div v-if="ManyReview" class="row">
        <div 
          v-for="(movie,idx) in ManyReview"
          :key=idx
          class="col"
        >
          <div class="card">
            <MoviePoster
              :movie="movie"
            />
            <span>{{movie.movie_id__count}}</span>              
          </div>
        </div>
      </div>
    </div>
    <div>
       <h3 class="d-flex"><b>#좋아요가 많은 영화</b></h3>
    </div>
    <div>
      <div class="row">
        <div 
          v-for="(movie,idx) in manylike"
          :key=idx
          class="col"
        >
          <div class="card">
            <MoviePoster
              :movie="movie"
            />
            <span>{{movie.movie_id__count}}</span>              
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MoviePoster from '@/components/MoviePoster.vue'

export default {
  name : 'Recommendation',
  components : {
    MoviePoster
  },
  data () {
    return {
      Recommended : '',
      ManyReview : '',
      manylike : '',
    }
  },
  computed : {
    recommended () { 
      return this.$store.getters.getRecommended
    },
    manyReview(){
      return this.$store.getters.getManyReview
    },
    manyLike() {
      return this.$store.getters.getManyLike
    }
  },
  watch : {
    recommended(val) {
      this.Recommended = val
    },
    manyReview(val) {
      this.ManyReview = val
    },
    manyLike(val) {
      this.manylike = val
    }
  },
  async created() {
    this.$store.dispatch('RECOMMEND_MOVIE')
    this.$store.dispatch('Many_Rate')
    this.$store.dispatch('Many_Like')

  },
}
</script>

<style>

</style>