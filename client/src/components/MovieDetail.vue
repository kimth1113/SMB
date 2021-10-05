<template>
  <div class="d-inline-flex col-4 align-top flex-column align-items-center">
    <h3>{{movie.title}}</h3>
    <div 
      v-show="MovieCardView">
      <p>{{movie.overview}}</p>
    </div>
    <div class="d-flex justify-content-end">
      <button @click="MovieCardView=!MovieCardView">더보기</button>
    </div>
  </div>
</template>

<script>
export default {
  name : 'MovieDetail',
  components : {
  },
  data () {
    return {
      MovieCardView : false,
    }
  },
  props : {
    movie : {
      type:Object
    },
  },
}
</script>

<style scoped>
.movie:hover{
  background-color: aliceblue;
}

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
</style>