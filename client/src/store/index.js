import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

axios.defaults.baseURL = 'http://127.0.0.1:8000/'
Vue.use(Vuex)
const api_key = '223815248626f4669e7ce900ef58a20d'

export default new Vuex.Store({
  state: {
    username : localStorage.getItem('username'),
    user_id : localStorage.getItem('user_id'),
    token : localStorage.getItem('token'),
    likes : null,
    like : null,
    userlikes : null,
    userreviews : null,

    movies : null,
    recommended_movie : null,
    manyReview : null,
    movie_detail : null,
    movie_reviews : [],

    detail_artcile : null,
    comments : null,
    articles: null,

    temp : null,
  },
  getters : {
    getUser(state) {
      return state.username
    },
    getUserId(state) {
      return state.user_id
    },
    getMovies(state) {
      return state.movies
    },
    LoggedIn(state) {
      return state.token ? true : false
    },
    getAritcles(state) {
      return state.articles
    },
    getMovieDetail(state) {
      return state.movie_detail
    },
    getDetailArticle(state) {
      return state.detail_artcile
    },
    getArticleComment(state){
      return state.comments
    },
    getRecommended(state) {
      return state.recommended_movie
    },
    getLike(state) {
      return state.like
    },
    getUserLikes(state){
      return state.userlikes
    },
    getMovieReviews(state) {
      return state.movie_reviews
    },
    getManyReview(state) {
      return state.manyReview
    },
    getUserReviews(state){
      return state.userreviews
    },
    getManyLike(state) {
      return state.likes
    }
  },
  mutations: {
    GETMOVIES(state, MOVIES) {
      state.movies = MOVIES
    },
    CREATE_USER (state, userForm) {
      state.user = userForm
    },
    AUTH_USER(state, token) {
      state.token = token
    },
    LOGOUT(state) {
      state.token = ''
      state.user= null
      localStorage.removeItem('token')
      localStorage.removeItem('username')
      localStorage.removeItem('user_id')
      localStorage.removeItem('likes')
    },
    GETARTICLES(state, ARTICLES) {
      state.articles = ARTICLES
    },
    RECOMMENDMOVIE(state, movies){
      state.recommended_movie = movies
    },
    GETMOVIEDETAIL(state, movie) {
      state.movie_detail = movie
    },
    DETAILARTICLE(state, article) {
      state.detail_artcile = article
    },
    ARTICLECOMMENT(state,comments) {
      state.comments = comments
    },
    MOVIELIKE(state, like) {
      state.like = like
    },
    GET_USER_DATA(state, user){
      state.user_id = user.id
      state.username = user.username
    },
    ARTICLECREATE(state,article) {
      state.articles.push(article)
    },
    CREATECOMMENT(state, comment){
      state.comments.push(comment)
    },
    DELETEARTICECOMMENT(state, comments) {
      state.comments = comments
    },
    DELETEARTICLE(state, articles){
      state.articles = articles
    },
    GETUSERDATA(state,userdata) {
      state.userlikes = userdata['likes']
    },
    USERLIKE(state, likes) {
      state.userlikes = likes
    },
    GETUSERLIKES(state, likes) {
      state.userlikes = likes
    },
    REVIEWCREATE(state, review) {
      state.movie_reviews = review

    },
    DETAILMOVIEREVIEWS(state, reviews) {
      state.movie_reviews = reviews
    },
    TEMP(state){
      state.temp = 1
    },
    MANYRATE(state, data) {
      state.manyReview = data
    },
    GETUSERREVIEWS(state, data) {
      state.userreviews = data
    },
    MANYLIKE(state, likes){
      state.likes = likes
    } 
  },
  actions: {
    async GET_MOVIES({commit}) {
      const GET_MOVIE_URL = `https://api.themoviedb.org/3/movie/popular?api_key=${api_key}&language=ko-KR&page=1`
      const res = await axios.get(GET_MOVIE_URL)
      commit('GETMOVIES', res.data.results)
    },
    async CREATE_USER({commit}, userForm) {
      const USER_CREATE_URL = 'api/v1/accounts/signup/'
      const data = userForm
      console.log(data)
      const res = await axios.post(USER_CREATE_URL, data)
      commit('CREATE_USER', res.data)
    },
    async AUTH_USER({commit}, userForm) {
      
      const LOGIN_URL = 'api/v1/accounts/login/'
      await axios.post(LOGIN_URL, {'name' : userForm['username']})
      .then((res)=>{
        localStorage.setItem('username', res.data.username)
        localStorage.setItem('user_id', res.data.id)
        commit('GET_USER_DATA', res.data)
      })

      const data = userForm
      return new Promise((resolve)=>{
        const AUTH_USER_URL = 'api/token/'
        axios.post(AUTH_USER_URL, data)
        .then((res)=>{
          const token = res.data.access
          localStorage.setItem('token', token)
          commit('AUTH_USER', token)
          resolve()
        })
        // const userId = this.getters.getUserId
        // const GET_USER_URL = `api/v1/movies/${userId}/likes/`
        // axios.get(GET_USER_URL)
        // .then((res)=>{
        //   commit('GETUSERLIKES', res.data)
        // })
      })
    },
    async GET_ARTICLES({commit}) {
      const ARTICLE_URL = 'api/v1/community/'
      axios.get(ARTICLE_URL)
      .then((res)=> {
        commit('GETARTICLES', res.data)
      })
    },
    async RECOMMEND_MOVIE({commit}){
      const MOVIE_URL = 'api/v1/movies/cnt/'
      axios.get(MOVIE_URL)
      .then((res)=>{
        commit('RECOMMENDMOVIE', res.data)
      })
    },
    async GET_MOVIE_DETAIL({commit}, id) {
      let flag = 0
      const likelist = this.getters.userlikes
      for (let i=0; i < likelist;i++) {
        if(likelist[i].movie_id == id) {
          flag = 1
          localStorage.setItem('likestatus', true)
        }
      }
      if(flag) {
        localStorage.setItem('likestatus', false)
      }
      const MOVIE_DETAIL_URL = `https://api.themoviedb.org/3/movie/${id}?api_key=${api_key}&language=ko`
      await axios.get(MOVIE_DETAIL_URL)
      .then((res)=> {
        commit('GETMOVIEDETAIL', res.data)
      })
    },
    async GET_ARTICLE_DETAIL({commit}, article_id) {
      const ARTICLE_DETAIL_URL = `api/v1/community/${article_id}/article_detail/`
      await axios.get(ARTICLE_DETAIL_URL)
      .then((res)=>{
        commit('DETAILARTICLE', res.data)
      })
    },
    async GET_ARTICLE_COMMENT({commit}, article_id) {
      const ARTICLE_COMMENT_URL = `api/v1/community/${article_id}/comment/`
      await axios.get(ARTICLE_COMMENT_URL)
      .then((res)=> {
        commit('ARTICLECOMMENT', res.data)
      })
    },
    async CREATE_ARTICLE_COMMENT({commit}, commentForm) {
      const article_id = commentForm['article_id']
      const CREATE_COMMENT_URL = `api/v1/community/${article_id}/comment/`
      const data = {
        'user' : this.getters.getUserId,
        'content' : commentForm['content']
      }
      await axios.post(CREATE_COMMENT_URL, data)
      .then((res)=> {
        commit('CREATECOMMENT', res.data)
      })
    },

    async ARTICLE_CREATE({commit}, articleForm){
      const ARTICLE_CREATE_URL = `api/v1/community/article/create/`
      const data = {
        'user' : this.state.user_id,
        'username' : this.state.username,
        'title' : articleForm.title,
        'content' : articleForm.content,
      }
      axios.post(ARTICLE_CREATE_URL, data)
      .then((res)=>{
        commit('ARTICLECREATE', res.data)
      })
    },
    async DELETE_ARTICE_COMMENT({commit}, deletecommentForm) {
      const article_id = deletecommentForm['article_id']
      const comment_id = deletecommentForm['comment_id']
      for (let i= 0; i < this.state.comments[i].length; i++) {
        if (this.state.comments[i].id == comment_id) {
          this.state.comments.splice(i,1)
        }
      }
      const DELETE_COMMENT_URL = `api/v1/community/${article_id}/comment/${comment_id}/`
      const res = await axios.post(DELETE_COMMENT_URL)
      commit('DELETEARTICECOMMENT', res.data)
    },
    async DELETE_ARTICLE({commit}, deletearticleForm) {
      const article_id = deletearticleForm['article_id']
      const DELETE_ARTICLE_URL = `api/v1/community/${article_id}/article_delete/`
      const data ={
        user_id : this.getters.getUserId
      }
      axios.post(DELETE_ARTICLE_URL, data)
      .then((res)=>{
        commit('DELETEARTICLE', res.data)
      })
      .catch(()=>{
        alert('접근이 불가능합니다.')
      })
    },

    async ARTICLE_UPDATE({commit}, articleForm) {
      const article_id = articleForm['article_id']
      const ARTICLE_DETAIL_URL = `api/v1/community/${article_id}/article_update/`

      await axios.post(ARTICLE_DETAIL_URL, articleForm)
      .then((res)=>{
        commit('DETAILARTICLE', res.data)
      })
      .catch(()=>{
        alert('접근이 불가능합니다.')
      })
    },
    async SEARCH_MOVIES({commit}, keyword) {
      const SEARCH_URL = `https://api.themoviedb.org/3/search/movie/?api_key=${api_key}&language=ko&query=${keyword}`
      await axios.get(SEARCH_URL)
      .then((res)=>{
        commit('GETMOVIES',res.data.results)
      })

    },

    async USER_LIKE({commit}, movie_id) {
      const POST_USER_LIKE_URL = `api/v1/movies/like/`
      const data = {
        'user_id' : this.getters.getUserId,
        'movie_id' : movie_id,
      }
      await axios.post(POST_USER_LIKE_URL, data)
      .then((res)=>{
        commit('GETUSERLIKES', res.data)
      })
    },
    async GET_USER_LIKES({commit}, userId) {
      const GET_USER_URL = `api/v1/movies/${userId}/likes/`
      axios.get(GET_USER_URL)
      .then((res)=>{
        commit('GETUSERLIKES', res.data)
      })
    },
    async REVIEW_CREATE({commit}, ReviewForm) {
      const REVIEW_CREATE_URL = 'api/v1/movies/review/create/'
      console.log(ReviewForm)
      axios.post(REVIEW_CREATE_URL,ReviewForm)
      .then((res)=>{
        commit('REVIEWCREATE', res.data)
      })

    },
    async MOVIE_REVIEW_LIST({commit}, movieId ) {
      const DETAIL_MOVIE_REVIEWS = `api/v1/movies/${movieId}/review/list/`
      axios.get(DETAIL_MOVIE_REVIEWS)
      .then((res)=>{
        commit('DETAILMOVIEREVIEWS', res.data)
      })
    },
    async REVIEW_DELETE({commit}, data) {
      const REVIEW_DELETE_URL = `api/v1/movies/review/delete/`
      axios.post(REVIEW_DELETE_URL,data)
      .then((res)=>{
        commit('DETAILMOVIEREVIEWS', res.data)
      })
    },
    async MOVIE_CNT_URL({commit}, movieId) {
      const MOVIE_CNT_URL = `api/v1/movies/cnt/`
      axios.post(MOVIE_CNT_URL ,{'movie_id': movieId})
      .then(()=>{
        commit('TEMP')
      })
    },
    async Many_Rate({commit}){
      const Many_Rate_URL = `api/v1/movies/manyrate/`
      axios.get(Many_Rate_URL)
      .then((res)=>{
        commit('MANYRATE', res.data)
      })
    },
    async GET_USER_REVIEWS({commit}) {
      const GET_USER_REVIEWS_URL = `api/v1/movies/userreviews/`
      const data = {
        user_id : this.getters.getUserId
      }
      axios.post(GET_USER_REVIEWS_URL, data)
      .then((res)=>{
        commit(`GETUSERREVIEWS`, res.data)
      })
    },
    async UPDATE_REVIEW({commit}, data ){
      const GET_UPDATE_REVIEW_URL = `api/v1/movies/review/update/`
      axios.post(GET_UPDATE_REVIEW_URL, data)
      .then((res)=>{
        console.log(res.data)
        commit('DETAILMOVIEREVIEWS', res.data)
      })
    },
    async Many_Like({commit}){
      const Many_Like_URL = `api/v1/movies/manylike/`
      axios.get(Many_Like_URL)
      .then((res)=>{
        commit('MANYLIKE', res.data)
      })
    }
  },
  modules: {
  }
})
