<template>
  <div class="wrapper">
    <div class="content">
      <div class="d-flex justify-content-center">
        <div class="align-items-center">
          <div class="col">
            <input type="text" autofocus placeholder="id" v-model="userForm.username">
          </div>
          <div class="col">
            <input type="password" placeholder="password" v-model="userForm.password">
          </div>
          <div class="col">
            <input @keyup.enter="Submit" type="password" placeholder="password_confirmation" v-model="userForm.password_confirmation">
          </div>
          <div>
            <button class="btn btn-light" @click="Submit">회원가입</button>
          </div>
          <router-link to="/login/">
            <span style="font-size:1rem;">아이디가 있으신가요?</span>
          </router-link>
      
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name :"Signup",
  data () {
    return {
      userForm : {
        username : '',
        password : '',
        password_confirmation : '',
      },
    }
  },
  methods : {
    Submit() {
      this.$store.dispatch('CREATE_USER', this.userForm)
      .then(()=>{
        this.$store.dispatch('AUTH_USER', this.userForm)
        .then(()=>{
          this.$router.push('/api/v1/movies/')
        })
      })
    }
  },
}
</script>

<style scoped>
.wrapper {
  display: grid;
  place-items: center;
  min-height: 100vh;
}

.content {
  font-family: system-ui, serif;
  font-size: 2rem;
  padding: 3rem;
  border-radius: 1rem;
  background: whitesmoke
}
</style>