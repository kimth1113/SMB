<template>
  <div class="flex justify-content-center align-top">
    <input class="searchbar" type="text" placeholder="Search Movie" v-model="keyword" @keyup.enter="Search" @change="Search">
    <div class="justify-content-around">
      <div class="row">
        <button class="icon col">
          <i class="fas fa-ghost" id="horror"></i>
        </button>
        <button class="icon col">
          <i class="fas fa-laugh-beam"></i>
        </button>
        <button class="icon col">
          <i class="fas fa-car-crash"></i>
        </button>
      </div>
      <div class="row">
        <button class="icon col">
          <i class="fas fa-home"></i>
        </button>
        <button class="icon col">
          <i class="far fa-kiss-wink-heart"></i>
        </button>
        <button class="icon col">
          <i class="fas fa-space-shuttle"></i>
        </button>
      </div>
    </div>
    <div
      id="movies"
      class="d-inline-flex row align-top movie-container"
    >
      <div
        v-for="(movie, id) in movies"
        :key="id"
        class="col-2"
      > 
        <div class="movie-poster">
            <router-link 
              :to="`/api/v1/movies/detail/${movie.id}/`"
            >
              <img 
                class="poster"
                :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" 
                alt=""
              >
              <span style="color:black">{{movie.title}}</span>
            </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {

  name : 'Movies',
  data () {
    return {
      URL : 'http://127.0.0.1:8000/api/v1/movies/',
      movie_id : '',
      keyword : '',
      page : Math.floor(Math.random(1,1000) * 100),
      movies : [],
    }
  },
  computed : {
    // movies () {
    //   return this.$store.getters.getMovies
    // },
    user () {
      return this.$store.getters.getUser
    },
   },
  created() {

    const GET_MOVIE_URL = `https://api.themoviedb.org/3/movie/popular?api_key=223815248626f4669e7ce900ef58a20d&language=ko-KR&page=${this.page}`
    axios.get(GET_MOVIE_URL)
    .then((res)=>{
      for (let i=0; i < 18;i ++){
        this.movies.push(res.data.results[i])
      }
    })
    // this.$store.dispatch('GET_MOVIES')
  },
  mounted() {

    document.addEventListener('scroll', () =>{
      const {scrollHeight, scrollTop, clientHeight} = document.documentElement
      if(scrollHeight- 50<= (scrollTop + clientHeight) ){
        this.loadMore()
      }
    })
  },
  methods : {
    loadMore() {
      this.page = Math.floor(Math.random(1,1000)*100)
      const GET_MOVIE_URL = `https://api.themoviedb.org/3/movie/popular?api_key=223815248626f4669e7ce900ef58a20d&language=ko-KR&page=${this.page}`
      axios.get(GET_MOVIE_URL)
      .then((res)=>{
        for (let i=0; i < 18; i ++){
          this.movies.push(res.data.results[i])
        }
      })
    },

    Search() {
      const SEARCH_URL = `https://api.themoviedb.org/3/search/movie/?api_key=223815248626f4669e7ce900ef58a20d&language=ko&query=${this.keyword}`
      axios.get(SEARCH_URL)
      .then((res)=>{
        this.movies = []
        for (let i = 0; i < res.data.results.length;i ++) {
          this.movies.push(res.data.results[i])
        }
      })
    },

  },

}

</script>

<style>
.modal,
.overlay {
  width: 100%;
  height: 100%;
  position:fixed;
  left: 0;
  top: 0;
}

.overlay{
  opacity: 0.5;
  background-color: black;
}

.modal-card {
  position: relative;
  max-width: 80%;
  margin: auto;
  margin-top: 30px;
  padding: 20px;
  background-color: white;
  min-height: 500px;
  z-index: 10;
  opacity: 1;
}
.poster:hover {
  transform : scale(1.05);
}

.searchbar {

  margin-top : 50px;
  font-size: 20px;
  height: 100%;
  border-radius: 20px;
  border: 1px solid black;
  background: transparent;
  outline: none;
  color: black;
  text-align: center;

}
.movie-container{
  margin-top : 50px;
}
.horror {
  color :red;
}
</style>