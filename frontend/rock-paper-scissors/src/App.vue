<template>
  <div id="nav">
    <router-link to="/">Login</router-link>
    <span>&nbsp;|&nbsp;</span>
    <router-link to="/register">Register</router-link>
    <span>&nbsp;|&nbsp;</span>
    <router-link v-if="loggedIn" to="/home">Home</router-link>
  </div>
  <router-view />
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { mapGetters } from "vuex";

export default defineComponent({
  name: "App",
  computed: {
    ...mapGetters(["loggedIn"]),
  },
});
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
