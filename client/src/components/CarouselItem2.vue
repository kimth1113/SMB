<template>
  <div class="carousel-item" data-bs-interval="2000">
    <img :src="`https://image.tmdb.org/t/p/w300/${this.backdrop}`" class="d-block w-100" alt="...">
  </div>
</template>

<script>
export default {
  name : 'CarouselItem2',
  props : {
    backdrop :String,
  }
}
</script>

<style>

</style>