import Vue from 'vue'
import VueRouter from 'vue-router'
import Movies from '../views/Movies.vue'
import Signup from '../views/Signup.vue'
import Login from '../views/Login.vue'
import Community from '../views/Community.vue'
import Recommendation from '../views/Recommendation.vue'
import MovieDetail from '../views/MovieDetail.vue'
import ArticleDetail from '../views/ArticleDetail.vue'
import ArticleCreate from '../views/ArticleCreate.vue'
import MyPage from '../views/MyPage.vue'
import ArticleUpdate from '../views/ArticleUpdate.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/api/v1/movies/',
    name: 'Movies',
    component: Movies
  },
  {
    path: '/',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/login/',
    name: 'Login',
    component: Login
  },
  {
    path: '/api/v1/community/',
    name: 'Community',
    component: Community
  },
  {
    path: '/api/v1/movies/recommend/',
    name: 'Recommendation',
    component: Recommendation
  },
  {
    path: '/api/v1/movies/detail/:id/',
    name: 'MovieDetail',
    component: MovieDetail,
    props :true,
  },
  {
    path: '/api/v1/commuity/:article_id/article_detail/',
    name: 'ArticleDetail',
    component: ArticleDetail,
    props :true,
  },
  {
    path: '/api/v1/commuity/article/create/',
    name: 'ArticleCreate',
    component: ArticleCreate,
  },
  {
    path: '/api/v1/mypage/',
    name: 'MyPage',
    component: MyPage,
  },
  {
    path: '/api/v1/commuity/:article_id/article_update/',
    name: 'ArticleUpdate',
    component: ArticleUpdate,
    props :true,
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
