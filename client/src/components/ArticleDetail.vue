<template>
  <div>
    <h1>{{ article }}</h1>
  </div>
</template>

<script>
export default {
  name : "ArticleDetail",
  props : {
    article :{
      type : Object,
    }
  },
}
</script>

<style>

</style>