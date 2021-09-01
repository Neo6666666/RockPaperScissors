<template>
  <div class="navbar">
    <router-link to="/">Login</router-link>
    <router-link to="/register">Register</router-link>
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

<style></style>
