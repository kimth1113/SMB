<template>
  <div class="wrapper">
    <div class="content">
      <div class="d-flex justify-content-center">
        <div class="align-items-center">
          <div class="col">
            <input type="text" autofocus placeholder="id" v-model="userForm.username">
          </div>
          <div class="col">
            <input type="password" placeholder="password"  @keyup.enter="Submit" v-model="userForm.password">
          </div>
          <div>
            <button class="btn btn-light" @click="Submit">로그인</button>
          </div>
          <router-link to="/">
            <span style="font-size:1rem;">아이디가 없으신가요?</span>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name : "Login",
  data () {
    return {
      userForm : {
        username : '',
        password : '',
      }
    }
  },
  methods : {
    Submit() {
      this.$store.dispatch('AUTH_USER', this.userForm)
      .then(()=>{
        this.$router.push('/api/v1/movies/')
      })
    },
  }

}
</script>

<style>
.label {
  background-color: transparent;
}

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