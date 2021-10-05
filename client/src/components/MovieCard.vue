<template>
  <div class="justify-content-around ">
    <div class="row align-items-center">
      <div class="col-3">
        <img :src="`https://image.tmdb.org/t/p/w500/${this.backdrops[1]}`" alt=".">
      </div>
      <div class="col-3">
        <p>{{this.title}}</p>
      </div>
      <div class="col-3">
        <p>{{review.rate}}</p>
      </div>
      <div class="col-3">
        <p>{{review.content}}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name : 'MovieCard',
  data () {
    return {
      backdrops : [],
      title : '',
    }
  },
  props : {
    review : Object,
  },
  computed : {

  },

  created () {
    
    const GET_IMAGES_URL = `https://api.themoviedb.org/3/movie/${this.review.movie_id}/images?api_key=223815248626f4669e7ce900ef58a20d`
    axios.get(GET_IMAGES_URL)
    .then((res)=>{
      for(let i=0 ; i < res.data.backdrops.length; i++){
        this.backdrops.push(res.data.backdrops[i].file_path)
      }
    })
    const GET_MOVIE_URL = `https://api.themoviedb.org/3/movie/${this.review.movie_id}?api_key=223815248626f4669e7ce900ef58a20d&language=ko`
    axios.get(GET_MOVIE_URL)
    .then((res)=>{
      this.title = res.data.title
    })



  },
}
</script>

<style>

</style>