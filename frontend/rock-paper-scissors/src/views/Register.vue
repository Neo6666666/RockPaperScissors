<template>
  <div class="register">
    <form @submit="submitForm">
      <input v-model="username" type="text" name="username" />
      <input v-model="password" type="password" name="password" />

      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script lang="ts">
import { useStore } from "vuex";
import { defineComponent, Ref, ref } from "vue";

export default defineComponent({
  name: "Login",
  setup() {
    const store = useStore();

    const username: Ref<string> = ref("");
    const password: Ref<string> = ref("");
    const submitForm = (e: Event) => {
      e.preventDefault();

      store.dispatch("register", {
        username: username.value,
        password: password.value,
      });
    };

    return {
      username,
      password,

      submitForm,
    };
  },
});
</script>
