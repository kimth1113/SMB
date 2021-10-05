<template>
  <div id="app" class="container">
    <nav>
      <div class="row" >
        <div v-if="LoggedIn">
          <ul class="menu align-right" style="background-color:#ffffff59;">
            <li>
              <router-link class="navbarText" to="/api/v1/movies/"><h5>Movies</h5></router-link>
            </li>
            <li>
              <router-link class="navbarText" to="/api/v1/movies/recommend/"><h5>Recommend</h5></router-link>
            </li>
            <li>
              <router-link class="navbarText" to="/api/v1/community/"><h5>Community</h5></router-link>
            </li>
            <li>
              <router-link class="navbarText" to="/api/v1/mypage/"><h5>{{Username}}</h5></router-link>
            </li>
            <li>
              <router-link class="navbarText" to="/" @click.native="Logout"><h5>Logout</h5></router-link>
            </li>
          </ul>
        </div>
        <div v-else>
          <ul class="menu align-right">
            <li>
              <router-link class="navbarText" to="/"><h5>Signup</h5></router-link>
            </li>
            <li>
              <router-link class="navbarText" to="/login"><h5>Login</h5></router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <router-view/>
  </div>
</template>
<script>
export default {
  name : 'App',
  computed : {
    LoggedIn() {
      return this.$store.getters.LoggedIn
    },
    Username() {
      return this.$store.getters.getUser
    },
  },
  methods : {
    Logout() {
      this.$store.commit('LOGOUT')
      this.$router.push('/login')
    }
  },
}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: red;
}
.toLogin {
  font-size: 1px;
}
.navbarText {
  color : black
}
.menu {
  position: relative;
  margin-top : 100px
  

}
</style>
