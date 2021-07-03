<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">

    <Users />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import Users from '@/components/Users.vue';

export default defineComponent({
  name: 'Home',
  components: {
    Users,
  },
});
</script>
