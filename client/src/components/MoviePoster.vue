<template>
  <div
    class="d-inline"
  >
    <router-link 
      :to="`/api/v1/movies/detail/${this.movie.movie_id}/`">
      <img 
        class="poster"
        width="300px"
        :src="`https://image.tmdb.org/t/p/w500/${this.poster_path}`" 
        alt=""
      >
    </router-link>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name : 'MoviePoster',
  data () {
    return {
      poster_path : '',
    }
  },
  props : {
    movie : Object,
  },
  async created () {
    const GET_MOVIE_POSTER = `https://api.themoviedb.org/3/movie/${this.movie.movie_id}/images?api_key=223815248626f4669e7ce900ef58a20d`
    axios.get(GET_MOVIE_POSTER)
    .then((res)=>{
      this.poster_path = res.data.posters[0].file_path
    })
  },
}
</script>

<style>
.poster:hover {
  transform : scale(0.95);
  
}
</style>