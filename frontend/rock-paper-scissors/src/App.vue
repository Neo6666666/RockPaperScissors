<template>
  <div class="navbar">
    <router-link
      v-if="!loggedIn"
      class="navbar__link"
      active-class="navbar__link_active"
      to="/"
    >Login</router-link>
    <router-link
      v-if="!loggedIn"
      class="navbar__link"
      active-class="navbar__link_active"
      to="/register"
    >Register</router-link>
    <router-link
      v-if="loggedIn"
      class="navbar__link"
      active-class="navbar__link_active"
      to="/home"
    >Home</router-link>
    <button
      v-if="loggedIn"
      class="navbar__link"
      @click="logout"
    >Logout</button>
  </div>

  <router-view />
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { mapGetters } from "vuex";
import router from '@/router';

export default defineComponent({
  name: "App",
  computed: {
    ...mapGetters(["loggedIn"]),
  },
  methods: {
    logout() {
      localStorage.clear();
      router.push('/');
      console.log(123);
    }
  }
});
</script>

<style src="@/assets/styles/index.css"></style>
